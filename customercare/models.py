from django.db import models
from ckeditor.fields import RichTextField #Ckeditor for edit 
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify


# Create your models here.

class KnowledgeCenter(models.Model):
	title = models.CharField(max_length=200, null=False, blank=False)
	topic = models.CharField(max_length=20, null=True, blank=True)
	slug = models.SlugField(max_length=500, null=True, blank=True)
	details = RichTextField()
	written_by = models.CharField(max_length=20, null=False, blank=False)
	helpfull = models.BooleanField()


	def __str__(self):
		return self.title

@receiver(pre_save, sender=KnowledgeCenter)
def pre_save_slug(sender, **kwargs):
	slug = slugify(kwargs['instance'].title)
	kwargs['instance'].slug = slug

