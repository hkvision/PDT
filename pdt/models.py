from django.db import models
from django.db.models import Sum, Count
from django.shortcuts import get_object_or_404
from datetime import tzinfo, timedelta, datetime
from django.utils.timezone import utc

# Create your models here.

class ReportManager(models.Manager):
	def newReport(self, estmSLOC, estmEffort):
		tid = TimeMetric(start=datetime.utcnow().replace(tzinfo=utc), end=datetime.utcnow().replace(tzinfo=utc),interrupt=timedelta(0), delta=timedelta(0))
		sid = SizeMetric(estmSLOC=estmSLOC, estmEffort=timedelta(days=30*float(estmEffort)), actSLOC=0, actEffort=timedelta(0), SperE=0.0)
		did = DefectMetric()
		tid.save()
		sid.save()
		did.save()
		report = Report(tid=tid, sid=sid, did=did)
		report.save()
		return report

class Report(models.Model):
	# id is added by default
	tid = models.ForeignKey('TimeMetric', default=-1)
	sid = models.ForeignKey('SizeMetric', default=-1)
	did = models.ForeignKey('DefectMetric', default=-1)

	objects = ReportManager()

	def update(self, delta, actSLOC, actEffort):
		self.tid.update(delta)
		self.sid.update(actSLOC, actEffort)
		self.save()
		return

class TimeMetric(models.Model):
	# id is added by default
	start = models.DateTimeField()
	end = models.DateTimeField()
	delta = models.DurationField()
	interrupt = models.DurationField()

	def update(self, delta):
		self.end = datetime.utcnow().replace(tzinfo=utc)
		self.delta = delta
		self.interrupt = (self.end - self.start) - delta
		self.save()
		return

	def __str__(self):
		return "Time Metrics"

class SizeMetric(models.Model):
	# id is added by default
	estmSLOC = models.IntegerField(default=0)
	actSLOC = models.IntegerField(default=0)
	estmEffort = models.DurationField(default=timedelta(0))
	actEffort = models.DurationField(default=timedelta(0))
	SperE = models.FloatField(default=0.0)

	def update(self, actSLOC, actEffort):
		self.actSLOC = actSLOC
		self.actEffort = actEffort
		month = actEffort.days / 30 + actEffort.seconds / (30*24*2600) # +1: protect against zero-division-error
		if month == 0:
			self.SperE = -1
		else:
			self.SperE = float(actSLOC) / month
		self.save()
		return

# Defect Metric:
# required:
# 1. total # of defect injected/removed
# 2. injection rate per person-hour
# 3. removal rate per person-hour of defect removal
# 4. defect density per KSLOC
# 5. yield
class DefectMetric(models.Model):
	# id is added by default
	injected = models.IntegerField(default=0)
	removed = models.IntegerField(default=0)
	rate = models.FloatField(default=0.0)
	density = models.FloatField(default=0.0)
	dyield = models.FloatField(default=0.0)

	def set(self, injected, removed, dyield, delta, KSLOC):
		self.injected = injected
		self.removed = removed
		self.dyield = dyield
		if delta == 0:
			self.rate = -1.0
		else:
			self.rate = injected / delta
		if KSLOC == 0:
			self.density = -1
		else:
			self.density = injected / KSLOC
		self.save()
		return


class Stage(models.Model):
	# ID is auto generated
	name = models.CharField(max_length=100, default="--")
	desc = models.TextField(default="(None)")
	status = models.CharField(max_length=20, default="default")
	report = models.ForeignKey('Report', default=-1)

	def getInfo(self):
		return {"name": self.name, "desc": self.desc, "status": self.status, "report": self.report}

	def setDefect(self, injected, removed, dyield):
		delta = self.report.tid.delta.seconds / 3600
		KSLOC = self.report.sid.actSLOC / 1000
		self.report.did.set(injected, removed, dyield, delta, KSLOC);
		return

	def __str__(self):
		return self.name

	class Meta:
		abstract = True

class ProjectManager(models.Manager):
	def newProject(self, name, desc, mID, currIter, eSLOC, eEffort):
		if Project.objects.filter(manager=mID, name=name):
			return False
		report = Report.objects.newReport(eSLOC, eEffort)
		project = Project(name=name, desc=desc, report=report, manager=get_object_or_404(Manager, id=mID), currIter=currIter, status="ongoing")
		project.save()
		return True

	def getProjectList(self, mID):
		return self.filter(manager=mID)

class Project(Stage):
	currIter = models.ForeignKey('Iteration', default=2) # 2 is the dummy iteration
	manager = models.ForeignKey('Manager', default=-1)
	developerList = models.ManyToManyField('Developer')

	objects = ProjectManager()

	def updateIter(self, itr):
		self.currIter = itr
		self.save()
		return

	def close(self):
		pid = self.id
		if Phase.objects.hasOpenPhase(pid):
			return False
		delta = Phase.objects.sumDelta(self.id)
		actSLOC = self.currIter.report.sid.actSLOC
		actEffort = delta
		self.report.update(delta, actSLOC, actEffort)
		self.status = 'past'
		self.save()
		return True

class PhaseManager(models.Manager):
	def newPhase(self, name, desc, projID, eSLOC, eEffort):
		if Phase.objects.filter(projID=projID, name=name):
			return False
		report = Report.objects.newReport(eSLOC, eEffort)
		phase = Phase(name=name, desc=desc, report=report, projID=get_object_or_404(Project, id=projID), status="ongoing")
		phase.save()
		return True


	def getPhaseList(self, projID):
		return self.filter(projID=projID).order_by('id')

	def sumDelta(self, projID):
		phases = self.filter(projID=projID)
		sumDur = timedelta(0)
		for phase in phases:
			sumDur += phase.report.tid.delta
		return sumDur

	def hasOpenPhase(self, projID):
		phases = self.filter(projID=projID)
		for phase in phases:
			if phase.status == 'ongoing':
				return True
		return False


class Phase(Stage):
	projID = models.ForeignKey('Project', default=-1)
	objects = PhaseManager()

	def getCurrIter(self):
		return self.projID.currIter

	def close(self):
		pid = self.id
		if Iteration.objects.hasOpenIter(pid):
			return False
		delta = Iteration.objects.sumDelta(self.id)
		actSLOC = self.projID.currIter.report.sid.actSLOC
		actEffort = delta
		self.report.update(delta, actSLOC, actEffort)
		self.status = 'past'
		self.save()
		return True

class IterationManager(models.Manager):
	def newIteration(self, name, desc, phase, eSLOC, eEffort):
		if self.hasOpenIter(phase):
			return "Please close the current iteration first."
		if self.filter(phaseID=phase, name=name):
			return "Iteration duplicated."
		report = Report.objects.newReport(eSLOC, eEffort)
		iteration = Iteration(name=name, desc=desc, report=report, phaseID=phase, status="ongoing")
		iteration.save()
		phase.projID.currIter = iteration
		phase.projID.save()
		return True

	def iterMap(self, phaseName, currIterID, relativeID):
		project = Project.objects.filter(currIter=currIterID)[0]
		phase = Phase.objects.filter(projID=project.id).filter(name=phaseName)[0]
		absIter = Iteration.objects.filter(phaseID=phase.id).filter(name=relativeID)[0]
		return absIter

	def iterCnt(self, phaseID):
		return self.filter(phaseID=phaseID).count()

	def getIterList(self, phaseID):
		return self.filter(phaseID = phaseID).order_by('id')

	def sumDelta(self, phaseID):
		itrs = self.filter(phaseID=phaseID)
		sumDur = timedelta(0)
		for itr in itrs:
			sumDur += itr.report.tid.delta
		return sumDur

	def hasOpenIter(self, phaseID):
		itrs = self.filter(phaseID=phaseID)
		for itr in itrs:
			if itr.status == 'ongoing':
				return True
		return False

class Iteration(Stage):
	phaseID = models.ForeignKey('Phase', default=-1)
	objects = IterationManager()

	def close(self, actSLOC):
		pid = self.id
		delta = TimeRecord.objects.sumDelta(self.id)
		actEffort = delta
		self.report.update(delta, actSLOC, actEffort)
		self.status = 'past'
		self.save()
		return True

class TimeRecordManager(models.Manager):
	def sumDelta(self, iID):
		if self.filter(iterID=iID).count() == 0:
			return timedelta(0)
		return self.filter(iterID=iID).aggregate(sumdur=Sum('duration'))['sumdur']

	def sumDebug(self, iID):
		if self.filter(iterID=iID).filter(type='defectRemoval').count() == 0:
			return timedelta(0)
		return self.filter(iterID=iID).filter(type='defectRemoval').aggregate(sumdur=Sum('duration'))['sumdur']

class TimeRecord(models.Model):
	# id is added by default but not used
	devID = models.ForeignKey('Developer', default=-1)
	iterID = models.ForeignKey('Iteration', default=-1)
	duration = models.DurationField()

	objects = TimeRecordManager()

class DefectRecordManager(models.Manager):
	def setYield(self, projID, lastIterID):
		phaseList = Phase.objects.getPhaseList(projID)
		phasePrev = 0
		phaseYields = [] # format: [ [ [phaseName, phaseYield], [[iterName, iterYield]] ] ]
		removedProjTotal = 0
		injectedProjTotal = 0
		# the last iteration is assumed to have a yield of 80%
		lookupEstm = self.getEstm(lastIterID)
		for phase in phaseList:
			iterList = Iteration.objects.getIterList(phase.id)
			iterYields = []
			removedPhaseTotal = 0
			injectedPhaseTotal = 0
			iterPrev = phasePrev
			for iteration in iterList:
				removed = self.removed(iteration.id)
				curr = self.injected(iteration.id)
				if int(iteration.id) in lookupEstm:
					curr += lookupEstm[int(iteration.id)]
				if (iterPrev + curr) == 0:
					iterYield = 0
				else:
					iterYield = removed / (iterPrev + curr)
				iteration.setDefect(curr, removed, iterYield)
				iterYields.append([iteration.name, iterYield])
				iterPrev = iterPrev + curr - removed
				# update the phase count
				removedPhaseTotal += removed
				injectedPhaseTotal += curr
			if (phasePrev + injectedPhaseTotal) == 0:
				phaseYield = 0
			else:
				phaseYield = removedPhaseTotal / (phasePrev + injectedPhaseTotal)
			phase.setDefect(injectedPhaseTotal, removedPhaseTotal, phaseYield)
			phaseYields.append([[phase.name, phaseYield], iterYields])
			phasePrev = phasePrev + injectedPhaseTotal - removedPhaseTotal
			# update the project count
			removedProjTotal += removedPhaseTotal
			injectedProjTotal += injectedPhaseTotal
		if injectedProjTotal == 0:
			projectYield = 0
		else:
			projectYield = removedProjTotal / injectedProjTotal
		project = get_object_or_404(Project, pk=projID)
		project.setDefect(injectedProjTotal, removedProjTotal, projectYield)
		return

	def injected(self, iterID):
		return self.filter(injectIter=iterID).count()

	def removed(self, iterID):
		return self.filter(removeIter=iterID).count()

	def getEstm(self, iterID):
		# the last iteration is assumed to have a yield of 80%
		# return format: [{'designation': 'Salesman', 'dcount': 2}, {'designation': 'Manager', 'dcount': 2}]
		lookup = {}
		for each in self.filter(removeIter=iterID).values('injectIter').annotate(iterCnt=Count('injectIter')):
			lookup[each['injectIter']] = each['iterCnt'] / 4
		return lookup

class DefectRecord(models.Model):
	injectIter = models.ForeignKey('Iteration', related_name='injectIter', default=-1)
	removeIter = models.ForeignKey('Iteration', related_name='removeIter', default=-1)
	devID = models.ForeignKey('Developer', default=-1)
	dtype = models.CharField(max_length=20, default="default")
	desc = models.TextField(default="(None)")

	objects = DefectRecordManager()

class User(models.Model):
	# UID is added by default
	# default value is 0
	pin = models.CharField(max_length=20, default="default")
	name = models.CharField(max_length=100, default="default")
	email = models.EmailField(default="none@se.com")
	online = models.BooleanField(default=False)

	class Meta:
		abstract = True

class Manager(User):
	def login(self):
		self.online = 1
		self.save()
		return

class Developer(User):
	iteration = models.ManyToManyField('Iteration')