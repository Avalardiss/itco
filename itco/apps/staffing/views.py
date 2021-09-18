from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import generic
from .models import Soldier, Worker, Vacant, List_vacant, All_staff
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from .permissions import AuthorPermissionsMixin, MembersPermissionsMixin
from tablib import Dataset
from .resources import SoldierResource, WorkerResource, VacantResource, List_vacantResource
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
from django.db.models import Sum, Min,Max, Avg


##--------------------сложение данных таблиц и вывод в общую ---------------------##
class СountingListView(LoginRequiredMixin, ListView):
    model = Soldier
    template_name = 'soldier.html'
    context_object_name = 'counting'



@login_required
def index(request):
	num_visits=request.session.get('num_visits', 0)
	request.session['num_visits'] = num_visits+1
	return render(request, 'index.html', context={'num_visits':num_visits})

@login_required
def support(request):
    return render(request, 'support.html')

@login_required
def change_password(request):
    pass

class StaffingListView(LoginRequiredMixin, ListView):
	model = Soldier
	model = Worker
	model = Vacant
	model = List_vacant
	template_name = 'staffing.html'
	login_url = '/accounts/login/'
	redirect_field_name = 'redirect_to'


################  ЗА ВОЙСКА  ################################

class SoldierListView(LoginRequiredMixin, generic.ListView):
    #permission_required = 'staffing.view_soldier'
    model = Soldier
    context_object_name = 'soldier'
    soldier = Soldier.objects.all().order_by('id')
    template_name = 'soldier.html'
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    @login_required
    def soldier(self):
        self._published = self.published
        return render(request, "soldier.html", {'soldier':id}, {'pub_date':pub_date})
    def get_context_data(self, *args, **kwargs):
        context = super(SoldierListView, self).get_context_data(*args, **kwargs)
        context['all_state'] = Soldier.objects.aggregate(Sum('all_state'))
       # context.update()
        return context



class SoldierDetailView(LoginRequiredMixin, generic.DetailView):
    #permission_required = 'staffing.view_soldier'
    model = Soldier
    template_name = 'soldier_detail.html'
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    @login_required
    def soldier_detail_view(request,pk):
    	try:
    		id=Soldier.objects.get(pk=pk)
    	except Soldier.DoesNotExist:
    		raise Http404("No information found for the troops")
    	return render(request, 'soldier_detail.html', context={'soldier':id,})


class SoldierUpdate(MembersPermissionsMixin, UpdateView):
    #permission_required = 'staffing.change_soldier'
    model = Soldier
    template_name = 'soldier_form.html'
    fields = ['name', 'all_state', 'all_nal', 'all_nekomplekt', 'all_percent', 'off_state', 'off_nal', 'off_nekomplekt', 'off_percent', 'prap_state', 'prap_nal', 'prap_nekomplekt', 'prap_percent', 'kontrakt_state', 'kontrakt_nal', 'kontrakt_nekomplekt', 'kontrakt_percent', 'srok_state', 'srok_nal', 'srok_nekomplekt', 'srok_percent']
    class Meta:
    	model = Soldier
    	fields = ['name', 'all_state', 'all_nal', 'all_nekomplekt', 'all_percent', 'off_state', 'off_nal', 'off_nekomplekt', 'off_percent', 'prap_state', 'prap_nal', 'prap_nekomplekt', 'prap_percent', 'kontrakt_state', 'kontrakt_nal', 'kontrakt_nekomplekt', 'kontrakt_percent', 'srok_state', 'srok_nal', 'srok_nekomplekt', 'srok_percent']    

##########################  ЗА ТЕРРО ###################################

class WorkerListView(LoginRequiredMixin, generic.ListView):
    #permission_required = 'staffing.view_worker'
    model = Worker
    context_object_name = 'worker'
    worker = Worker.objects.all().order_by('id')
    template_name = 'worker.html'
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    @login_required
    def worker(self):
        self._published = self.published
        return render(request, "worker.html", {'worker':id}, {'pub_date':pub_date})


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    #permission_required = 'staffing.view_worker'
    model = Worker
    template_name = 'worker_detail.html'
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    @login_required
    def worker_detail_view(request,pk):
    	try:
    		id=Worker.objects.get(pk=pk)
    	except Worker.DoesNotExist:
    		raise Http404("No information found for the TERRO")
    	return render(request, 'worker_detail.html', context={'worker':id,})


class WorkerUpdate(MembersPermissionsMixin, UpdateView):
    #permission_required = 'staffing.change_worker'
    model = Worker
    template_name = 'worker_form.html'
    fields = ['name', 'all_state', 'all_nal', 'all_nekomplekt', 'all_percent', 'off_state', 'off_nal', 'off_nekomplekt', 'off_percent', 'prap_state', 'prap_nal', 'prap_nekomplekt', 'prap_percent', 'sotr_state', 'sotr_nal', 'sotr_nekomplekt', 'sotr_percent']
    class Meta:
    	model = Worker
    	fields = ['name', 'all_state', 'all_nal', 'all_nekomplekt', 'all_percent', 'off_state', 'off_nal', 'off_nekomplekt', 'off_percent', 'prap_state', 'prap_nal', 'prap_nekomplekt', 'prap_percent', 'sotr_state', 'sotr_nal', 'sotr_nekomplekt', 'sotr_percent']


##########################  ЗА ПЕРЕЧЕНЬ ВАКАНТНЫХ ДОЛЖНОСТЕЙ ###################################

class VacantListView(LoginRequiredMixin, generic.ListView):
    #permission_required = 'staffing.view_vacant'
    model = Vacant
    context_object_name = 'vacant'
    vacant = Vacant.objects.all().order_by('id')
    template_name = 'vacant.html'
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    @login_required
    def vacant(self):
        return render(request, "vacant.html", {'vacant':id})

class VacantDetailView(LoginRequiredMixin, generic.DetailView):
    #permission_required = 'staffing.view_vacant'
    model = Vacant
    template_name = 'vacant_detail.html'
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    @login_required
    def vacant_detail_view(request,pk):
    	try:
    		id=Vacant.objects.get(pk=pk)
    	except Vacant.DoesNotExist:
    		raise Http404("No information found for the Vacant")
    	return render(request, 'vacant_detail.html', context={'vacant':id,})


# сохранение данных в бд
@login_required
def vacant_create(request):
    model = Vacant

    if request.method == "POST":
        objects_list = Vacant()
        objects_list.author = request.user
        objects_list.nomer = request.POST.get("nomer")
        objects_list.name = request.POST.get("name")
        objects_list.location = request.POST.get("location")
        objects_list.vacant_position = request.POST.get("vacant_position")
        objects_list.rank_state = request.POST.get("rank_state")
        objects_list.tariff = request.POST.get("tariff")
        objects_list.vus = request.POST.get("vus")
        objects_list.date_vacant = request.POST.get("date_vacant")
        objects_list.candidate = request.POST.get("candidate")  
        objects_list.save()
        objects_list.members.add(request.user)            
        return HttpResponseRedirect("/staffing/vacant/")
    else:
        return render(request, "vacant_create.html")

class VacantUpdate(MembersPermissionsMixin, UpdateView):
    #permission_required = 'staffing.change_vacant'
    model = Vacant
    template_name = 'vacant_form.html'
    fields = ['nomer', 'name', 'location', 'vacant_position', 'rank_state', 'tariff', 'vus', 'date_vacant', 'candidate']
    class Meta:
    	model = Vacant
    	fields = ['nomer', 'name', 'location', 'vacant_position', 'rank_state', 'tariff', 'vus', 'date_vacant', 'candidate']


# удаление данных из бд
class VacantDelete(MembersPermissionsMixin, DeleteView):
    model = Vacant
    success_url = '/staffing/vacant/'

    def delete_vacant(request, pk):
        try:
            vacant = Vacant.objects.get(pk=pk)
            vacant.delete()
            return HttpResponseRedirect("/staffing/vacant/")
        except Vacant.DoesNotExist:
            return HttpResponseNotFound("<h2>Данные не найдены</h2>")


##########################  ЗА СПИСОК ВАКАНТОВ ###################################

class List_vacantListView(LoginRequiredMixin, generic.ListView):
    #permission_required = 'staffing.view_list_vacant'
    model = List_vacant
    context_object_name = 'list_vacant'
    list_vacant = List_vacant.objects.all().order_by('id')
    template_name = 'list_vacant.html'
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    @login_required
    def list_vacant(self):
        return render(request, "list_vacant.html", {'list_vacant':id})


# сохранение данных в бд
@login_required
def list_vacant_create(request):
    model = List_vacant

    if request.method == "POST":
        objects_list = List_vacant()
        objects_list.author = request.user
        objects_list.name = request.POST.get("name")
        objects_list.name_group = request.POST.get("name_group")
        objects_list.classifier = request.POST.get("classifier")
        objects_list.military_position_state = request.POST.get("military_position_state")
        objects_list.date_vacant = request.POST.get("date_vacant")
        objects_list.rank_state = request.POST.get("rank_state")
        objects_list.tariff = request.POST.get("tariff")
        objects_list.vus = request.POST.get("vus")
        objects_list.name_candidate = request.POST.get("name_candidate")  
        objects_list.rank = request.POST.get("rank") 
        objects_list.save()
        objects_list.members.add(request.user)            
        return HttpResponseRedirect("/staffing/list_vacant/")
    else:
        return render(request, "list_vacant_create.html")




class List_vacantDetailView(LoginRequiredMixin, generic.DetailView):
    #permission_required = 'staffing.view_list_vacant'
    model = List_vacant
    template_name = 'list_vacant_detail.html'
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    @login_required
    def list_vacant_detail_view(request,pk):
        try:
            id=List_vacant.objects.get(pk=pk)
        except List_vacant.DoesNotExist:
            raise Http404("No information found for the List_vacant")
        return render(request, 'list_vacant_detail.html', context={'list_vacant':id,})


class List_vacantUpdate(MembersPermissionsMixin, UpdateView):
    #permission_required = 'staffing.change_list_vacant'
    model = List_vacant
    template_name = 'list_vacant_form.html'
    fields = ['name', 'name_group', 'classifier', 'military_position_state', 'date_vacant', 'rank_state', 'tariff', 'vus', 'name_candidate', 'rank']
    class Meta:
        model = List_vacant
        fields = ['name', 'name_group', 'classifier', 'military_position_state', 'date_vacant', 'rank_state', 'tariff', 'vus', 'name_candidate', 'rank']


# удаление данных из бд

class List_vacantDelete(MembersPermissionsMixin, DeleteView):
    model = List_vacant
    success_url = '/staffing/list_vacant/'

    def delete_list_vacant(request, pk):
        try:
            list_vacant = List_vacant.objects.get(pk=pk)
            list_vacant.delete()
            return HttpResponseRedirect("/staffing/list_vacant/")
        except List_vacant.DoesNotExist:
            return HttpResponseNotFound("<h2>Данные не найдены</h2>")

################  ЗА ЦО ВНГ РФ  ################################

class All_staffListView(LoginRequiredMixin, generic.ListView):
    model = All_staff
    context_object_name = 'all_staff'
    all_staff = All_staff.objects.all().order_by('id')
    template_name = 'all_staff.html'
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    @login_required
    def all_staff(self):
        self._published = self.published
        return render(request, "all_staff.html", {'all_staff':id}, {'pub_date':pub_date})

class All_staffDetailView(LoginRequiredMixin, generic.DetailView):
    #permission_required = 'staffing.view_soldier'
    model = All_staff
    template_name = 'all_staff_detail.html'
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    @login_required
    def all_staff_detail_view(request,pk):
        try:
            id=All_staff.objects.get(pk=pk)
        except All_staff.DoesNotExist:
            raise Http404("No information found")
        return render(request, 'all_staff_detail.html', context={'all_staff':id,})


class All_staffUpdate(MembersPermissionsMixin, UpdateView):
    #permission_required = 'staffing.change_soldier'
    model = All_staff
    template_name = 'all_staff_form.html'
    fields = ['name', 'all_state', 'all_nal', 'all_nekomplekt', 'all_percent', 'off_state', 'off_nal', 'off_nekomplekt', 'off_percent', 'prap_state', 'prap_nal', 'prap_nekomplekt', 'prap_percent', 'kontrakt_state', 'kontrakt_nal', 'kontrakt_nekomplekt', 'kontrakt_percent', 'srok_state', 'srok_nal', 'srok_nekomplekt', 'srok_percent']
    class Meta:
        model = All_staff
        fields = ['name', 'all_state', 'all_nal', 'all_nekomplekt', 'all_percent', 'off_state', 'off_nal', 'off_nekomplekt', 'off_percent', 'prap_state', 'prap_nal', 'prap_nekomplekt', 'prap_percent', 'kontrakt_state', 'kontrakt_nal', 'kontrakt_nekomplekt', 'kontrakt_percent', 'srok_state', 'srok_nal', 'srok_nekomplekt', 'srok_percent']


# ---------------- Импорт - экспорт -----------------------#

def export_data(request):
    if request.method == 'POST':
        # Get selected option from form
        file_format = request.POST['file-format']
        soldier_resource = SoldierResource()
        worker_resource = WorkerResource()
        vacant_resource = VacantResource()
        list_vacant_resource = List_vacantResource()
        dataset = soldier_resource.export()
        dataset = worker_resource.export()
        dataset = vacant_resource.export()
        dataset = list_vacant_resource.export()
        if file_format == 'CSV':
            response = HttpResponse(dataset.csv, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="exported_data.csv"'
            return response        
        elif file_format == 'JSON':
            response = HttpResponse(dataset.json, content_type='application/json')
            response['Content-Disposition'] = 'attachment; filename="exported_data.json"'
            return response
        elif file_format == 'XLS (Excel)':
            response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="exported_data.xls"'
            return response   

    return render(request, 'export.html')



def import_data(request):
    if request.method == 'POST':
        file_format = request.POST['file-format']
        soldier_resource = SoldierResource()
        worker_resource = WorkerResource()
        vacant_resource = VacantResource()
        list_vacant_resource = List_vacantResource()
        dataset = Dataset()
        new_soldiers = request.FILES['importData']
        new_workers = request.FILES['importData']
        new_vacants = request.FILES['importData']
        new_list_vacants = request.FILES['importData']

        if file_format == 'CSV':
            imported_data = dataset.load(new_soldiers.read().decode('utf-8'),format='csv')
            result = soldier_resource.import_data(dataset, dry_run=True)                                                                 
        elif file_format == 'JSON':
            imported_data = dataset.load(new_soldiers.read().decode('utf-8'),format='json')
            # Testing data import
            result = soldier_resource.import_data(dataset, dry_run=True) 

        if not result.has_errors():
            # Import now
            soldier_resource.import_data(dataset, dry_run=False)



        if file_format == 'CSV':
            imported_data = dataset.load(new_workers.read().decode('utf-8'),format='csv')
            result = worker_resource.import_data(dataset, dry_run=True)                                                                 
        elif file_format == 'JSON':
            imported_data = dataset.load(new_workers.read().decode('utf-8'),format='json')
            # Testing data import
            result = worker_resource.import_data(dataset, dry_run=True) 

        if not result.has_errors():
            # Import now
            worker_resource.import_data(dataset, dry_run=False)


        if file_format == 'CSV':
            imported_data = dataset.load(new_vacants.read().decode('utf-8'),format='csv')
            result = vacant_resource.import_data(dataset, dry_run=True)                                                                 
        elif file_format == 'JSON':
            imported_data = dataset.load(new_vacants.read().decode('utf-8'),format='json')
            # Testing data import
            result = vacant_resource.import_data(dataset, dry_run=True) 

        if not result.has_errors():
            # Import now
            vacant_resource.import_data(dataset, dry_run=False)


        if file_format == 'CSV':
            imported_data = dataset.load(new_list_vacants.read().decode('utf-8'),format='csv')
            result = list_vacant_resource.import_data(dataset, dry_run=True)                                                                 
        elif file_format == 'JSON':
            imported_data = dataset.load(new_list_vacants.read().decode('utf-8'),format='json')
            # Testing data import
            result = list_vacant_resource.import_data(dataset, dry_run=True) 

        if not result.has_errors():
            # Import now
            list_vacant_resource.import_data(dataset, dry_run=False)

    return render(request, 'import.html')    

# ----------------end Импорт - экспорт -----------------------#


