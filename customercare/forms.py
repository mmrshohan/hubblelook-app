from django import forms 
from .models import KnowledgeCenter



class Knowledge_center_form(forms.ModelForm):
	class Meta:
		model = KnowledgeCenter
		fields = ['title', 'details', 'written_by']