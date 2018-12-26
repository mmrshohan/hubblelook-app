from django.db import models
from django.conf import settings
from django.urls import reverse
from ckeditor.fields import RichTextField #Ckeditor for edit 
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify


class Profile(models.Model):
	PUBLIC = 'Public'
	PRIVATE = 'Private'
	INITIATIVE ='Initiative'
	PRIVATE_STARTUP = 'Private and Startup'
	INITIAL_KEYWORD = (
		(PUBLIC, 'Public'),
		(PRIVATE, 'Private'),
		(INITIATIVE, 'Initiative'),
		(PRIVATE_STARTUP, 'Private and Startup'),
		)
	Type_of_account = models. NullBooleanField('Personal account', help_text="by default this is Business account")
	user_photo = models.ImageField(upload_to='user_image', blank=True)
	user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
	occupation = models.CharField(max_length=400, null=False)
	name = models.CharField(max_length=200, null=False, blank=False, default=None)
	title = models.CharField(max_length=100, null=True, blank=True)
	url = models.URLField(max_length=200, null=True, blank=True)
	additional_url = models.URLField(max_length=200, null=True, blank=True )
	Headquarter = models.CharField(max_length=1000, null=True, blank=True)
	stock_market = models.CharField(max_length=200, null=True, blank=True)
	established = models.DateField(auto_now=False, auto_now_add=False, default=None)
	investors = RichTextField(null=True, blank=True)
	about_details = RichTextField(null=False, blank=False, default=None)
	Type_of_company = models.CharField(
	 max_length=20,
	 null=True, 
	 blank=True, 
	 choices=INITIAL_KEYWORD, 
	 default=PRIVATE_STARTUP) 


	def __str__(self):
		return self.name

		

class Team(models.Model):
	description = models.CharField(max_length=1200, null=True, blank=True) 
	team = models.TextField(null=True, blank=True)
	user = models.OneToOneField(User, on_delete=models.CASCADE)

class About(models.Model):
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
	about_this_company = models.TextField(null=True, blank=True)


class Investment(models.Model):
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
	investment = models.TextField(null=True, blank=True)





