from django.urls import path, include
from django.contrib import admin, auth
from staffing import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from .views import StaffingListView, SoldierListView, SoldierDetailView, WorkerListView, WorkerDetailView,  List_vacantListView, List_vacantDetailView, All_staffListView, All_staffDetailView,  List_vacantDelete
from . import views
from staffing import views
from django.urls import path, re_path
from django.db.models import Sum, Min,Max, Avg


app_name = 'staffing'

urlpatterns = [
	#url(r'^$', views.index, name='index'),
	path('', views.index, name='index'),
    path('support/', views.support, name='support'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('staffing/', StaffingListView.as_view(), name='staffing'),

    path(r'^staffing/soldier/$', views.SoldierListView.as_view(), name='soldier'),
    path(r'^staffing/soldier/(?P<pk>\d+)$', views.SoldierDetailView.as_view(), name='soldier-detail'),
    path(r'^staffing/soldier/(?P<pk>\d+)/update/$', views.SoldierUpdate.as_view(), name='soldier_update'),

    path(r'^staffing/worker/$', views.WorkerListView.as_view(), name='worker',),
    path(r'^staffing/worker/(?P<pk>\d+)$', views.WorkerDetailView.as_view(), name='worker-detail'),
    path(r'^staffing/worker/(?P<pk>\d+)/update/$', views.WorkerUpdate.as_view(), name='worker_update'),

    path(r'^staffing/vacant/$', views.VacantListView.as_view(), name='vacant',),
    path(r'^staffing/vacant/(?P<pk>\d+)$', views.VacantDetailView.as_view(), name='vacant-detail'),
    path(r'^staffing/vacant/create', views.vacant_create, name='vacant_create'),
    path(r'^staffing/vacant/(?P<pk>\d+)/update/$', views.VacantUpdate.as_view(), name='vacant_update'),
    path(r'^staffing/vacant/(?P<pk>\d+)/delete/$', views.VacantDelete.as_view(), name='delete_vacant'),

    path(r'^staffing/list_vacant/$', views.List_vacantListView.as_view(), name='list_vacant',),
    path(r'^staffing/list_vacant/(?P<pk>\d+)$', views.List_vacantDetailView.as_view(), name='list_vacant-detail'),
    path(r'^staffing/list_vacant/create', views.list_vacant_create, name='list_vacant_create'),
    path(r'^staffing/list_vacant/(?P<pk>\d+)/update/$', views.List_vacantUpdate.as_view(), name='list_vacant_update'),
    path(r'^staffing/list_vacant/(?P<pk>\d+)/delete/$', views.List_vacantDelete.as_view(), name='delete_list_vacant'),

    path(r'^staffing/all_staff/$', views.All_staffListView.as_view(), name='all_staff',),
    path(r'^staffing/all_staff/(?P<pk>\d+)$', views.All_staffDetailView.as_view(), name='all_staff-detail'),
    path(r'^staffing/all_staff/(?P<pk>\d+)/update/$', views.All_staffUpdate.as_view(), name='all_staff_update'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()