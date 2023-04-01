import uuid

from django.db import models


class Company(models.Model):
    company_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    url = models.URLField(null=True, blank=True)
    logo_url = models.URLField(null=True, blank=True)
    def __str__(self):
        return "%s" % (self.title)


class Area(models.Model):
    area_id = models.IntegerField(primary_key=True)
    area_name = models.CharField(max_length=100)
    def __str__(self):
        return "%s" % (self.area_name)


class ExperienceLevel(models.Model):
    exp_id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100)
    def __str__(self):
        return "%s" % (self.name)


class Employment(models.Model):
    emp_id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100)
    def __str__(self):
        return "%s" % (self.name)


class Specializations(models.Model):
    spec_id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100)
    profarea_id = models.CharField(max_length=100)
    profarea_name = models.CharField(max_length=100)
    def __str__(self):
        return "%s" % (self.name)


class ProfessionalRoles(models.Model):
    prof_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__(self):
        return "%s" % (self.name)


class KeySkills(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return "%s" % (self.name)


class Schedule(models.Model):
    schedule_id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100)
    def __str__(self):
        return "%s" % (self.name)


class Vacancy(models.Model):
    vacancy_id = models.IntegerField(primary_key=True, blank=False)
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, db_constraint=False)
    experience_level = models.ForeignKey(ExperienceLevel, on_delete=models.SET_NULL, null=True)
    professional_role = models.ForeignKey(ProfessionalRoles, on_delete=models.SET_NULL, null=True)
    area = models.ForeignKey(Area, on_delete=models.SET_NULL, null=True, db_constraint=False)
    hh_url = models.URLField()
    salary_from = models.IntegerField(null=True, blank=True)
    salary_to = models.IntegerField(null=True, blank=True)
    currency = models.CharField(max_length=100, null=True, blank=True)
    schedule = models.ForeignKey(Schedule, on_delete=models.SET_NULL, null=True)
    employment = models.ForeignKey(Employment, on_delete=models.SET_NULL, null=True)
    key_skills = models.ManyToManyField(KeySkills, null=True)
    published = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    street = models.CharField(max_length=100, null=True, blank=True)
    building = models.CharField(max_length=100, null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    long = models.FloatField(null=True, blank=True)

    def __str__(self):
        return "%s" % (self.title)


