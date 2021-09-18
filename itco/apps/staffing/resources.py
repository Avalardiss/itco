from.models import Soldier, Worker, Vacant, List_vacant, All_staff
from import_export import resources

class SoldierResource(resources.ModelResource):
    class Meta:
        model = Soldier

class WorkerResource(resources.ModelResource):
    class Meta:
        model = Worker

class All_staffResource(resources.ModelResource):
    class Meta:
        model = All_staff

class VacantResource(resources.ModelResource):
    class Meta:
        model = Vacant

class List_vacantResource(resources.ModelResource):
    class Meta:
        model = List_vacant
