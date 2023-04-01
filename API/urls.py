"""OpenChecker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:

Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views



urlpatterns = [
    path('vacancies/', views.VacancyList.as_view()),
    path('companies/', views.CompanyList.as_view()),
    path('keyskills/', views.KeySkillsList.as_view()),
    path('areas/', views.AreaList.as_view()),
    path('prof_roles/', views.ProfRolesList.as_view()),
    path('specializations/', views.SpecializationList.as_view()),
]
