from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField #Ckeditor for edit 
from django.db.models.signals import pre_save
from django import forms
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

''' Quickword allows users to post in a very short manner. Any model chages about Quickword should
change in here'''





class QuickWord(models.Model):
	I_THINK = 'I think'
	GOOD_PART_OF = 'Feedback'
	BAD_PART_OF ='Good part'
	PROTOTYPE = 'Bad part'
	FEEDBACK = 'Prototype'
	REVIEW = 'Review'
	ASK = 'Ask'
	FINACIAL_MARKET = 'Financial market'
	INITIAL_KEYWORD = (
		(I_THINK, 'I THINK'),
		(FEEDBACK, 'FEEDBACK'),
		(GOOD_PART_OF, 'GOOD PART'),
		(BAD_PART_OF, 'BAD PART'),
		(PROTOTYPE, 'PROTOTYPE'),
		(REVIEW, 'REVIEW'),
		(ASK, 'ASK'), 
		(FINACIAL_MARKET, 'FINANCIAL MARKET')
		)
	
	pub_time = models.DateTimeField('Publish time', auto_now=True, auto_now_add=False)
	description = models.CharField(max_length=150, blank=False, null=False) 
	likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='likes')
	topic = models.CharField(max_length=2000, null=True, blank=True)
	Initial_keyword_choices = models.CharField(
	 max_length=100,
	 null=True, 
	 blank=True, 
	 choices=INITIAL_KEYWORD, 
	 default=I_THINK) 

	def __str__(self):
		return self.description

	class Meta:
		verbose_name = "Micro Thought"
		ordering = ['-pub_time']




''' Add product is very simplest way to adding the product description, any changes if needed
 to do this is the model we have to change '''

class AddProduct(models.Model):
	
	
	product_tumbline = models.ImageField(null=True, blank=True)
	slug = models.SlugField(max_length=500, null=True, blank=True)
	product_name = models.CharField(max_length=50)
	launched_time = models.DateField(auto_now=False, auto_now_add=False)
	pub_time = models.DateTimeField('Publish time', auto_now=True, auto_now_add=False)
	causel = models.ImageField(null=True, blank=True)
	product_url = models.URLField (max_length=100)
	title = models.CharField(max_length=100)
	Prices = models.IntegerField(null=True, blank=True)
	details = RichTextField(null=False, default=None)
	topic = models.CharField(max_length=2000, null=True, blank=True)

	

	def __str__(self):
		return self.product_name

	class Meta:
		verbose_name = "Product"
		ordering = ['-pub_time']

@receiver(pre_save, sender=AddProduct)
def pre_save_name_slug(sender, **kwargs):
	slug = slugify(kwargs['instance'].product_name)
	kwargs['instance'].slug = slug

''' This is short articel, main intention to incourage user's to read with out speading lots of time, 
any changes related to article should change in here '''

class Article(models.Model):
	GENERAL = 'General'
	PRODUCT = 'Product'
	ECONOMICS ='Economics'
	MARKET = 'Market'
	FINANCIAL_MARKET = 'Financial market'
	INITIAL_KEYWORD = (
		(GENERAL, 'GENERAL'),
		(PRODUCT, 'PRODUCT'),
		(ECONOMICS, 'ECONOMICS'),
		(MARKET, 'MARKET'),
		(FINANCIAL_MARKET, 'FINANCIAL MARKET'),
		)
	Initial_keyword_choices = models.CharField(max_length=10, null=True,
	 blank=True, 
	 choices=INITIAL_KEYWORD, 
	 default=GENERAL
	 )
	title = models.CharField(max_length=500, null=False, blank=False)
	slug = models.SlugField(max_length=500, null=True, blank=True)
	description = RichTextField()
	article_pub_time = models.DateTimeField(auto_now=True, auto_now_add=False)
	topic = models.CharField(max_length=2000, null=True, blank=True)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "Micro Article"
		ordering = ['-article_pub_time']

@receiver(pre_save, sender=Article)
def pre_save_slug(sender, **kwargs):
	slug = slugify(kwargs['instance'].title)
	kwargs['instance'].slug = slug


# Contact form model 

class UserContactForm(models.Model):

	name = models.CharField(max_length=200, null=False, blank=False)
	email = models.EmailField(max_length=200, null=False, blank=False)
	topic = models.CharField(max_length=200, null=False, blank=False, help_text='Do not write more than 200 words')
	write = models.TextField(null=False, blank=False)

	def __str__(self):
		return self.topic 







