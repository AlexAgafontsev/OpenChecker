from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ['id', 'title', 'description',
                  'company', 'experience_level', 'area',
                  'hh_url', 'salary_from', 'salary_to',
                  'currency', 'schedule', 'employment',
                  'key_skills', 'published', 'created',
                  'city', 'street', 'building', 'lat', 'long']


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'title', 'url']


class KeySkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeySkills
        fields = ['name']


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ['id', 'area_name']


class ProfRolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessionalRoles
        fields = ['id', 'name']


class SpecializationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specializations
        fields = ['id', 'name', 'profarea_id', 'profarea_name']





