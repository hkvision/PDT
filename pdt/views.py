from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, render_to_response, redirect
from django import forms
from datetime import tzinfo, timedelta, datetime
from django.template import RequestContext
from .models import *
from django.contrib.auth import authenticate, login, logout


######################
####    Manager   ####
######################

# the home page for manager
def index(request, mID):
    url = 'pdt/index0.html'
    manager = Manager.objects.filter(id=mID)[0]
    if manager.online == 1:
        projectLst = Project.objects.getProjectList(mID)
        developerList = Developer.objects.all()
        context = {"projectLst": projectLst, 'mID':manager, 'developerLst':developerList}
        return render(request, url, context)
    else:
        return HttpResponseRedirect('http://localhost:8000/pdt/login')

def newProject(request):
    mID = request.POST['mID']
    name = request.POST['name']
    eSLOC = request.POST['eSLOC']
    eEffort = request.POST['eEffort']
    desc = request.POST['desc']
    if mID and name and eSLOC and eEffort:
        if not desc:
            desc = '(No Description)'
        if Project.objects.newProject(name, desc, mID, dummyIter, eSLOC, eEffort):
            return index(request, mID)
        else:
            return HttpResponse("Error: failed to create project\"" + name + "\".")
    else:
        return HttpResponse('Missing Information')

# par: eSLOC, eEffort, desc, name
def newPhase(request):
    projID = request.POST['projID']
    name = request.POST['name']
    eSLOC = request.POST['eSLOC']
    eEffort = request.POST['eEffort']
    desc = request.POST['desc']
    if name and eSLOC and eEffort:
        if not desc:
            desc = '(No Description)'
        if Phase.objects.newPhase(name, desc, projID, eSLOC, eEffort):
            return viewProject(request, projID)
        else:
            return HttpResponse("Failure: phase\"" + name + "\" already exist.")
    else:
        return HttpResponse('Missing Information')

def newIteration(request):
    phaseID = request.POST['phaseID']
    name = len(Iteration.objects.getIterList(phaseID))+1
    eSLOC = request.POST['eSLOC']
    eEffort = request.POST['eEffort']
    desc = request.POST['desc']
    phase = get_object_or_404(Phase, id=phaseID)
    if name and eSLOC and eEffort:
        if not desc:
            desc = '(No Description)'
        ret = Iteration.objects.newIteration(name, desc, phase, eSLOC, eEffort)
        if ret == True:
            return viewProject(request, phase.projID.id)
        else:
            return HttpResponse(ret)
    else:
        return HttpResponse('Missing Information.')

# used for testing the calculation of yield
def test(request):
    dis = DefectRecord.objects.setYield(25, 31)
    return HttpResponse(dis)

# the page for a project
def viewProject(request, projID):
    project = get_object_or_404(Project, pk=projID)
    mID = project.manager
    info = project.getInfo()
    phaseList = Phase.objects.getPhaseList(projID)
    pairList = []
    for phase in phaseList:
        iterList = Iteration.objects.getIterList(phase.id)
        pair = PhaseIterPair(phase, iterList)
        pairList.append(pair)
    context = {"project": project, "time":project.report.tid, "pairList":pairList, 'mID':mID}
    return render(request, 'pdt/projTemplate.html', context)

def endProject(request):
    # do not need to input actual SLOC: the same as the last iteration
    projID = int(request.POST['projID'])
    project = get_object_or_404(Project, pk=projID)
    if project.close():
        genYield(project)
        return viewProject(request, projID)
    else:
        return HttpResponse("Fail to close project: open phase")

def endPhase(request):
    # do not need to input actual SLOC: the same as the last iteration
    phaseID = int(request.POST['phaseID'])
    phase = get_object_or_404(Phase, pk=phaseID)
    if phase.close():
        return viewProject(request, phase.projID.id)
    else:
        return HttpResponse("Fail to close phase: open iteration")

def endIteration(request):
    actSLOC = request.POST['aSLOC']
    iterID = int(request.POST['iterID'])
    iteration = get_object_or_404(Iteration, pk=iterID)
    if iteration.close(actSLOC):
        return viewProject(request, iteration.phaseID.projID.id)
    else:
        return HttpResponse("Fail to close iteration")

# calculate the yield
def genYield(project):
    DefectRecord.objects.setYield(project.id, project.currIter.id)
    y = project.report.did.dyield
    y1 = project.currIter.report.did.dyield
    return

# the page for the final report of a project
def finalReport(request, projID):
    project = get_object_or_404(Project, pk=projID)
    mID = project.manager
    phaseList = Phase.objects.getPhaseList(projID)
    pairList = []
    for phase in phaseList:
        iterList = Iteration.objects.getIterList(phase.id)
        pair = PhaseIterPair(phase, iterList)
        pairList.append(pair)
    context = {"project": project, "pairList":pairList, 'mID':mID}
    return render(request, 'pdt/finalReport.html', context)

# Dummy objects for defaults
dummyReport = get_object_or_404(Report, pk=7)
dummyIter = get_object_or_404(Iteration, pk=2)

# helper class to organize data
class PhaseIterPair:
    def __init__(self, phase, iterList):
        self.phase = phase
        self.iterList = iterList



######################
####   Developer  ####
######################

def info(request, devId):
    if request.method == 'POST':
        t = request.POST['t']

        time = int(t)/1000
        
        dev = int(request.POST['d'])
        itr = int(request.POST['i'])
        devline = Developer.objects.get(pk=dev)
        itrline = Iteration.objects.get(pk=itr)
        
        record = TimeRecord(devID = devline,iterID = itrline, duration=timedelta(seconds=time) )
        record.save()
        p = Project.objects.all()
        d = Developer.objects.get(pk=request.POST['d'])
        return render(request, 'timer/starter.html', {'p': p,'d':d})

    elif request.method == 'GET':
        defect = DefectRecord.objects.all().filter(devID=devId)
        p = Project.objects.filter(developer__id=devId)
        d = Developer.objects.get(pk=devId)
        r = TimeRecord.objects.all().filter(devID=devId)
        return render(request, 'timer/starter.html', {'p': p,'d':d,'r':r, 'defect':defect})

def defectrecords(request, devID, iterID):
    if request.method =='POST':
        desc = request.POST['description']
        dtype = request.POST['type']
        phaseName = phaseMap[request.POST['phase']]
        injectRelativeIter = request.POST['iteration']
        injectIter = Iteration.objects.iterMap(phaseName, iterID, injectRelativeIter)
        removeIter = Iteration.objects.get(pk=iterID)
        developer = Developer.objects.get(pk=devID)
        defectrecord = DefectRecord(devID=developer, injectIter=injectIter, removeIter=removeIter, dtype=dtype, desc=desc)
        defectrecord.save()

        p = Project.objects.filter(developer__id=devId)
        d = Developer.objects.get(pk=devID)
        r = TimeRecord.objects.all().filter(devID=devID)
        context = {'p': p,'d':d,'r':r}
        return render(request, 'timer/starter.html', context)
        
    elif request.method == 'GET':
        return render(request, 'timer/starter.html')

phaseMap = {'0':'Inception', '1':'Elaboration', '2':'Construction', '3':'Transition'}



######################
####     Login    ####
######################

# define user form
class UserForm(forms.Form):
    name = forms.CharField(label='Name ',max_length=100)
    pin = forms.CharField(label='PIN ',widget=forms.PasswordInput())

# login
def login(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            # get UID and PIN
            name = uf.cleaned_data['name']
            pin = uf.cleaned_data['pin']
            # validate in the database
            managerLst = Manager.objects.filter(name__exact = name,pin__exact = pin)
            if managerLst:
                manager = managerLst[0]
                manager.login()
                url = 'http://localhost:8000/pdt/index/'+str(manager.id)
                return redirect(url)
            else:
                developer = Developer.objects.filter(name__exact = name,pin__exact = pin)
                if developer:
                    url = 'http://localhost:8000/pdt/info/'+str(developer[0].id)+'/'
                    return redirect(url)
                else:
                    return render_to_response('login/login2.html',{'uf':uf}, RequestContext(request))
    else:
        uf = UserForm()
    return render_to_response('login/login.html', {'uf':uf}, RequestContext(request))

def aboutus(request, tick):
    if tick == '2':
        return render(request, 'pdt/aboutus2.html', {})
    else:
        return render(request, 'pdt/aboutus.html', {})