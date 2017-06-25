from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # the index for manager
    url(r'^index/(?P<mID>[0-9]*)$', views.index, name='index'),
    # project page
    url(r'projPage/(?P<projID>[0-9]+)/$', views.viewProject, name='viewProject'),
    # create new project
    url(r'newProject/', views.newProject, name='newProject'),
    # create new phase
    url(r'newPhase/', views.newPhase, name='newPhase'),
    # create new iteration
    url(r'newIteration/', views.newIteration, name='newIteration'),
    # end project
    url(r'^endProject/$', views.endProject, name='endProject'),
    # end phase
    url(r'^endPhase/$', views.endPhase, name='endPhase'),
    # end iteration
    url(r'^endIteration/$', views.endIteration, name='endIteration'),
    # timer
    url(r'^info/(?P<devId>[0-9]+)/$', views.info, name='info'),
    # defect
    url(r'^defectrecords/(?P<devID>[0-9]+)/(?P<iterID>[0-9]+)/$', views.defectrecords, name='defectrecords'),
    # login
    url(r'login$', views.login, name='login'),
    # aboutus
    url(r'^aboutus(?P<tick>[2]*)', views.aboutus, name='aboutus'),
    # final report
    url(r'^finalReport/(?P<projID>[0-9]+)/$', views.finalReport, name='finalReport')
    # to test defect
    # url(r'^defect$', views.test, name='yield'),
 ]

urlpatterns += staticfiles_urlpatterns()