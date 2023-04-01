from rest_framework import generics, permissions
from django.contrib.auth.models import User
from . import serializers
from .models import *


class VacancyList(generics.ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = serializers.VacancySerializer


class CompanyList(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = serializers.CompanySerializer


class KeySkillsList(generics.ListAPIView):
    queryset = KeySkills.objects.all()
    serializer_class = serializers.KeySkillsSerializer


class AreaList(generics.ListAPIView):
    queryset = Area.objects.all()
    serializer_class = serializers.AreaSerializer


class ProfRolesList(generics.ListAPIView):
    queryset = ProfessionalRoles.objects.all()
    serializer_class = serializers.ProfRolesSerializer


class SpecializationList(generics.ListAPIView):
    queryset = Specializations.objects.all()
    serializer_class = serializers.SpecializationsSerializer

