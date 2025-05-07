from django.contrib import admin

from .models import *


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "code")


class LecturerAdmin(admin.ModelAdmin):
    list_display = ("name", "department", "title", "university")


class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "supervisor", "co_supervisor","program", "evaluation_type")


class NominationAdmin(admin.ModelAdmin):
    list_display = ("student", "examiner1", "examiner2", "examiner3", "chairperson", "research_title", "is_locked")


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Lecturer, LecturerAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Nomination, NominationAdmin)
