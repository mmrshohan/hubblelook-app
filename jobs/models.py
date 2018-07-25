from django.db import models


# Create your models here.

class JobApplyView(models.Model):
	type_of_job = models.CharField(max_length=100, null=False, blank=False)
	apply_job = models.EmailField(max_length=100)
	job_location = models.CharField(max_length=200)
	qualification = models.CharField(max_length=500)
	job_details = models. CharField(max_length=1000, null=False, blank=False)

	def __str__(self):
		return self.type_of_job