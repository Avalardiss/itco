from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from.models import Soldier, Worker, Vacant, List_vacant, All_staff
from import_export import resources

class MyAdminSite(AdminSite):

    def get_app_list(self, request):
        app_dict = self._build_app_dict(request)
        app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())
        return app_list

admin.site = MyAdminSite()
admin.site.register(Group, GroupAdmin)
admin.site.register(User, UserAdmin)

@admin.register(Soldier)
class SoldierAdmin(ImportExportModelAdmin):
    list_display = ("id", "name", "all_state", "all_nal", "all_nekomplekt", "all_percent", "off_state", "off_nal", "off_nekomplekt", "off_percent", "prap_state", "prap_nal", "prap_nekomplekt", "prap_percent", "kontrakt_state", "kontrakt_nal", "kontrakt_nekomplekt", "kontrakt_percent", "srok_state", "srok_nal", "srok_nekomplekt", "srok_percent")
    change = ("id", "name", "all_state", "all_nal", "all_nekomplekt", "all_percent", "off_state", "off_nal", "off_nekomplekt", "off_percent", "prap_state", "prap_nal", "prap_nekomplekt", "prap_percent", "kontrakt_state", "kontrakt_nal", "kontrakt_nekomplekt", "kontrakt_percent", "srok_state", "srok_nal", "srok_nekomplekt", "srok_percent")
    ordering = ("id",)
    search_fields = ("name", "all_state", "all_nal", "all_nekomplekt", "all_percent", "off_state", "off_nal", "off_nekomplekt", "off_percent", "prap_state", "prap_nal", "prap_nekomplekt", "prap_percent", "kontrakt_state", "kontrakt_nal", "kontrakt_nekomplekt", "kontrakt_percent", "srok_state", "srok_nal", "srok_nekomplekt", "srok_percent")
    list_filter = ("name", "all_state", "all_nal", "all_nekomplekt", "all_percent", "off_state", "off_nal", "off_nekomplekt", "off_percent", "prap_state", "prap_nal", "prap_nekomplekt", "prap_percent", "kontrakt_state", "kontrakt_nal", "kontrakt_nekomplekt", "kontrakt_percent", "srok_state", "srok_nal", "srok_nekomplekt", "srok_percent")
admin.site.register(Soldier, SoldierAdmin)

@admin.register(Worker)
class WorkerAdmin(ImportExportModelAdmin):
    list_display = ("id", "name", "all_state", "all_nal", "all_nekomplekt", "all_percent", "off_state", "off_nal", "off_nekomplekt", "off_percent", "prap_state", "prap_nal", "prap_nekomplekt", "prap_percent", "sotr_state", "sotr_nal", "sotr_nekomplekt", "sotr_percent")
    ordering = ("id",)
    search_fields = ("name", "all_state", "all_nal", "all_nekomplekt", "all_percent", "off_state", "off_nal", "off_nekomplekt", "off_percent", "prap_state", "prap_nal", "prap_nekomplekt", "prap_percent", "sotr_state", "sotr_nal", "sotr_nekomplekt", "sotr_percent")
    list_filter = ("name", "all_state", "all_nal", "all_nekomplekt", "all_percent", "off_state", "off_nal", "off_nekomplekt", "off_percent", "prap_state", "prap_nal", "prap_nekomplekt", "prap_percent", "sotr_state", "sotr_nal", "sotr_nekomplekt", "sotr_percent")
admin.site.register(Worker, WorkerAdmin)

@admin.register(All_staff)
class All_staffAdmin(ImportExportModelAdmin):
    list_display = ("id", "name", "all_state", "all_nal", "all_nekomplekt", "all_percent", "off_state", "off_nal", "off_nekomplekt", "off_percent", "prap_state", "prap_nal", "prap_nekomplekt", "prap_percent", "kontrakt_state", "kontrakt_nal", "kontrakt_nekomplekt", "kontrakt_percent", "srok_state", "srok_nal", "srok_nekomplekt", "srok_percent")
    change = ("id", "name", "all_state", "all_nal", "all_nekomplekt", "all_percent", "off_state", "off_nal", "off_nekomplekt", "off_percent", "prap_state", "prap_nal", "prap_nekomplekt", "prap_percent", "kontrakt_state", "kontrakt_nal", "kontrakt_nekomplekt", "kontrakt_percent", "srok_state", "srok_nal", "srok_nekomplekt", "srok_percent")
    ordering = ("id",)
    search_fields = ("name", "all_state", "all_nal", "all_nekomplekt", "all_percent", "off_state", "off_nal", "off_nekomplekt", "off_percent", "prap_state", "prap_nal", "prap_nekomplekt", "prap_percent", "kontrakt_state", "kontrakt_nal", "kontrakt_nekomplekt", "kontrakt_percent", "srok_state", "srok_nal", "srok_nekomplekt", "srok_percent")
    list_filter = ("name", "all_state", "all_nal", "all_nekomplekt", "all_percent", "off_state", "off_nal", "off_nekomplekt", "off_percent", "prap_state", "prap_nal", "prap_nekomplekt", "prap_percent", "kontrakt_state", "kontrakt_nal", "kontrakt_nekomplekt", "kontrakt_percent", "srok_state", "srok_nal", "srok_nekomplekt", "srok_percent")
admin.site.register(All_staff, All_staffAdmin)

@admin.register(Vacant)
class VacantAdmin(ImportExportModelAdmin):
    list_display = ("id", "nomer", "name", "location", "vacant_position", "rank_state", "tariff", "vus", "date_vacant", "candidate")
    ordering = ("id",)
    search_fields = ("name", "location", "vacant_position", "rank_state", "tariff", "vus", "date_vacant", "candidate")
    list_filter = ("name", "location", "vacant_position", "rank_state", "tariff", "vus", "date_vacant", "candidate")
admin.site.register(Vacant, VacantAdmin)

@admin.register(List_vacant)
class List_vacantAdmin(ImportExportModelAdmin):
    list_display = ("id", "name", "name_group", "classifier", "military_position_state", "date_vacant", "rank_state", "tariff", "vus", "name_candidate", "rank")
    ordering = ("id",)
    search_fields = ("name", "name_group", "classifier", "military_position_state", "date_vacant", "rank_state", "tariff", "vus", "name_candidate", "rank")
    list_filter = ("name", "name_group", "classifier", "military_position_state", "date_vacant", "rank_state", "tariff", "vus", "name_candidate", "rank")
admin.site.register(List_vacant, List_vacantAdmin)