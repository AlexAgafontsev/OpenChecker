from .models import *
import django
from django.db.utils import IntegrityError

def create_company(data):
    company_id = int(data['employer']['id'])
    title = data['employer']['name']
    url = data['employer']['alternate_url']
    try:
        logo_url = data['employer']['logo_urls']['original']
    except:
        logo_url = None
    try:
        Company.objects.get_or_create(
        company_id=company_id,
        defaults={
        'title':title,
        'url':url,
        'logo_url':logo_url},
        )
    except django.db.utils.IntegrityError:
        print(id)
    return Company.pk


def create_area(data):
    area_id = data['area']['id']
    area_name = data['area']['name']
    area_id = int(area_id)
    Area.objects.get_or_create(
        area_id=area_id,
        area_name=area_name
    )
    return Area.pk


def create_exp_level(data):
    exp_id = data['experience']['id']
    name = data['experience']['name']
    ExperienceLevel.objects.get_or_create(
        exp_id=exp_id,
        name=name
    )
    return ExperienceLevel.pk


def create_employment(data):
    emp_id = data['employment']['id']
    name = data['employment']['name']
    Employment.objects.get_or_create(
        emp_id=emp_id,
        name=name
    )
    return Employment.pk


# def create_specialization(data):
#     id = int(data['employment']['id'])
#     name = data['employment']['name']
#     Employment.objects.get_or_create(
#         id=id,
#         name=name
#     )
#     return Employment.pk


def create_prof_roles(data):
    prof_id = int(data['professional_roles'][0]['id'])
    name = data['professional_roles'][0]['name']
    ProfessionalRoles.objects.get_or_create(
        prof_id=prof_id,
        name=name
    )
    return ProfessionalRoles.pk


def create_key_skill(data):
    key_skills_list = data['key_skills']
    for skills in key_skills_list:
        name = skills['name']
        KeySkills.objects.get_or_create(
            name=name
        )
        return KeySkills.pk


def create_schedule(data):
    schedule_id = data['schedule']['id']
    name = data['schedule']['name']
    Schedule.objects.get_or_create(
        schedule_id=schedule_id,
        name=name
    )
    return Schedule.pk


def create_vacancy(data):
    try:
        vacancy_id = int(data['id'])
    except KeyError:
        print(data)
    title = data['name']
    description = data['description']
    if data['type']['id'] != 'open':
        return
    else:
        create_company(data)
        company_id = int(data['employer']['id'])
    create_exp_level(data)
    experience_level_id = data['experience']['id']
    create_prof_roles(data)
    prof_id = data['professional_roles'][0]['id']
    create_area(data)
    area_id = int(data['area']['id'])
    hh_url = data['alternate_url']
    try:
        salary_from = data['salary']['from']
    except:
        salary_from = None
    try:
        salary_to = data['salary']['to']
    except:
        salary_to = None
    try:
        currency = data['salary']['currency']
    except:
        currency = None
    create_schedule(data)
    schedule_id = data['schedule']['id']
    create_employment(data)
    employment_id = data['employment']['id']
    # key_skills =
    published = data['published_at']
    created = data['created_at']
    try:
        city = data['address']['city']
    except TypeError:
        city = None
    try:
        street = data['address']['street']
    except TypeError:
        street = None
    try:
        building = data['address']['building']
    except TypeError:
        building = None
    try:
        lat = data['address']['lat']
        long = data['address']['lng']
    except TypeError:
        lat = None
        long = None

    vacancy = Vacancy.objects.get_or_create(
        vacancy_id=vacancy_id,
        defaults={
        "title":title,
        "description":description,
        "company":Company(company_id=company_id),
        'experience_level':ExperienceLevel(exp_id=experience_level_id),
        'professional_role':ProfessionalRoles(prof_id=prof_id),
        "area":Area(area_id=area_id),
        "hh_url":hh_url,
        "salary_from":salary_from,
        "salary_to":salary_to,
        "currency":currency,
        'schedule':Schedule(schedule_id=schedule_id),
        'employment':Employment(emp_id=employment_id),
        # key_skills:,
        "published":published,
        "created":created,
        "city":city,
        "street":street,
        "building":building,
        'lat':lat,
        'long':long,}
    )
    return Vacancy.pk