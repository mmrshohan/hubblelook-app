from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField #Ckeditor for edit 
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
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
	occupation = models.CharField(max_length=400, null=False)
	#followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followers', blank=True)
	#following = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='following', blank=True)
	#activated = models.BooleanField(default=False)
	name = models.CharField(max_length=200, null=False, blank=False, default=None)
	title = models.CharField(max_length=100, null=True, blank=True)
	url = models.URLField(max_length=200, null=True, blank=True)
	additional_url = models.URLField(max_length=200, null=True, blank=True )
	established = models.DateField(auto_now=False, auto_now_add=False, default=None)
	about_details = RichTextField(null=False, blank=False, default=None)
	Type_of_company = models.CharField(
	 max_length=20,
	 null=True, 
	 blank=True, 
	 choices=INITIAL_KEYWORD, 
	 default=PRIVATE_STARTUP) 


	def __str__(self):
		return self.name

		

class OfficalLetter(models.Model):
	title = models.CharField(max_length=1000, null=False, blank=False)
	slug = models.SlugField(max_length=1000, null=True, blank=True)
	to_whom = models.CharField(max_length=300, null=True, blank=True)
	letter = RichTextField()
	pub_time = models.DateTimeField('Publish time', auto_now=True)
	letter_from = models.CharField(max_length=500, null=True, blank=True)

	#def get_absolute_url(self):
	#	return reverse('offical-letter-view', kwargs={'username': self.username})

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-pub_time']

@receiver(pre_save, sender=OfficalLetter)
def pre_save_slug(sender, **kwargs):
	slug = slugify(kwargs['instance'].title)
	kwargs['instance'].slug = slug



