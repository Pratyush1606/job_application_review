from django.db import models

# Create your models here.
class Candidate(models.Model):
    candidate_id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    status = models.CharField(max_length=20, default="applied")

