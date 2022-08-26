from importlib.metadata import requires
from django.db import models


# Create your models here.
class Candidate(models.Model):
    candidate_id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    status = models.CharField(max_length=20, default="applied")


class CandidateAcademic(models.Model):
    candidate_id = models.ForeignKey(to=Candidate,
                                     related_name='candidate_acad',
                                     on_delete=models.CASCADE)
    education = models.CharField(max_length=50)
    degree = models.CharField(max_length=50)
    major = models.CharField(max_length=50)
    graduation_year = models.IntegerField()
    gpa = models.FloatField()
    gpa_max = models.FloatField()


class CandidateProfessionalExp(models.Model):
    candidate_id = models.ForeignKey(to=Candidate,
                                     related_name='candidate_prof_exp',
                                     on_delete=models.CASCADE)
    company = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    currently_working = models.BooleanField(default=False)
    description = models.TextField(max_length=250, blank=True)