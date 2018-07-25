from django import forms 
from .models import Profile, OfficalLetter



class Edit_Profile_Form(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['name', 
		'Type_of_account',
		 'user_photo', 
		 'title',
		  'url',
		   'Type_of_company',
		    'established',
		     'about_details' ]

class Official_Letter_Form(forms.ModelForm):
	class Meta:
		model = OfficalLetter
		fields = ['title', 'to_whom', 'letter', 'letter_from' ]