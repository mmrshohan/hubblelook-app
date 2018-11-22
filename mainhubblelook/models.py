from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField #Ckeditor for edit 
from django.db.models.signals import pre_save
from django import forms
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

class MainModel(models.Model):
	I_THINK = 'I think'
	GOOD_PART = 'Good part'
	BAD_PART ='Bad part'
	PROTOTYPE = 'Prototype'
	FEEDBACK = 'Feedback'
	INFO = 'Info'
	REVIEW = 'Review'
	ASK = 'Ask'
	FINACIAL_MARKET = 'Financial market'
	EVENT_OR_HAPPENING = 'event or happening'
	INITIAL_KEYWORD_FOR_THOUGHTS = (
		(I_THINK, 'I THINK'),
		(FEEDBACK, 'FEEDBACK'),
		(GOOD_PART, 'GOOD PART'),
		(BAD_PART, 'BAD PART'),
		(PROTOTYPE, 'PROTOTYPE'),
		(INFO, 'INFO'),
		(REVIEW, 'REVIEW'),
		(ASK, 'ASK'), 
		(FINACIAL_MARKET, 'FINANCIAL MARKET'),
		(EVENT_OR_HAPPENING, 'EVENT OR HAPPENING')
		)
	# Global User field, publish time and topic field 
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	pub_time = models.DateTimeField('Publish time', auto_now=True)
	topic = models.CharField(max_length=2000, null=True, blank=True)
	# thought model
	micro_thought = models.CharField(max_length=200, null=True, blank=True) 
	Initial_keyword_for_thoughts = models.CharField(
	 max_length=300,
	 null=True, 
	 blank=True, 
	 choices=INITIAL_KEYWORD_FOR_THOUGHTS, 
	 default=I_THINK
	 ) 
	## end of microthought Model 

    # Product model
	product_tumbline = models.ImageField(null=True, blank=True)
	product_slug = models.SlugField(max_length=500, null=True, blank=True)
	product_name = models.CharField(max_length=50, null=True, blank=True)
	product_title = models.CharField(max_length=100, null=True, blank=True)
	launched_time = models.DateField(auto_now=False, null=True, blank=True)
	causel = models.ImageField(null=True, blank=True)
	product_url = models.URLField (max_length=100, null=True, blank=True)
	Prices = models.IntegerField(null=True, blank=True)
	product_details = RichTextField(null=True, blank=True)
	## end of Product model 

	#article model
	GENERAL = 'General'
	PRODUCT = 'Product'
	ECONOMICS ='Economics'
	MARKET = 'Market'
	FINANCIAL_MARKET = 'Financial market'
	INITIAL_KEYWORD_FOR_ARTICLES = (
		(GENERAL, 'GENERAL'),
		(PRODUCT, 'PRODUCT'),
		(ECONOMICS, 'ECONOMICS'),
		(MARKET, 'MARKET'),
		(FINANCIAL_MARKET, 'FINANCIAL MARKET'),
		)
	Initial_keyword_for_articles = models.CharField(max_length=10, null=True,
	 blank=True, 
	 choices=INITIAL_KEYWORD_FOR_ARTICLES, 
	 default=GENERAL
	 )
	article_title = models.CharField(max_length=500, null=True, blank=True)
	slug = models.SlugField(max_length=500, null=True, blank=True)
	micro_article = RichTextField(null=True, blank=True)
	## end of article model 

	class Meta:
		ordering = ['-pub_time']

@receiver(pre_save, sender=MainModel)
def pre_save_slug(sender, **kwargs):
	slug = slugify(kwargs['instance'].article_title)
	kwargs['instance'].slug = slug


@receiver(pre_save, sender=MainModel)
def pre_save_name_slug(sender, **kwargs):
	slug = slugify(kwargs['instance'].product_name)
	kwargs['instance'].product_slug = slug


class OfficalLetter(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
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


# Contact form model 

class UserContactForm(models.Model):

	name = models.CharField(max_length=200, null=False, blank=False)
	email = models.EmailField(max_length=200, null=False, blank=False)
	topic = models.CharField(max_length=200, null=False, blank=False, help_text='Do not write more than 200 words')
	write = models.TextField(null=False, blank=False)

	def __str__(self):
		return self.topic 







