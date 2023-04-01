from django.contrib import admin
from .models import *


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title', 'vacancy_id', 'published')


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('title', 'company_id')


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ('area_name', 'area_id')


@admin.register(ExperienceLevel)
class ExpAdmin(admin.ModelAdmin):
    list_display = ('name', 'exp_id')


@admin.register(Employment)
class EmploymentAdmin(admin.ModelAdmin):
    list_display = ('name', 'emp_id')


@admin.register(Specializations)
class SpecAdmin(admin.ModelAdmin):
    list_display = ('name', 'spec_id')


@admin.register(ProfessionalRoles)
class ProfAdmin(admin.ModelAdmin):
    list_display = ('name', 'prof_id')


@admin.register(KeySkills)
class KeySkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'pk')


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('name', 'schedule_id')


