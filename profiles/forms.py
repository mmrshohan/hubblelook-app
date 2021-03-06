from django import forms 
from .models import Profile, Team


# user profile create/update form 
class Edit_Profile_Form(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['name', 
		'Type_of_account',
		 'user_photo', 
		 'title',
		  'url',
		   'Type_of_company',
		   'Headquarter',
		   'stock_market',
		    'established',
		     'about_details' ]



# team form
class TeamForm(forms.ModelForm):
	class Meta:
		model = Team
		fields = ['user', 'description', 'team']