from django import forms 
from .models import QuickWord, AddProduct, Article, UserContactForm


''' Thought Post form view   '''
class Quick_word_form(forms.ModelForm):
	class Meta:
		model = QuickWord
		fields = ['description', 'Initial_keyword_choices', 'topic']
		widgets={'description': forms.Textarea(attrs={'size': 10})}
	
  

''' Add Product form view   ''' 
class Add_product_view(forms.ModelForm):
	class Meta:
		model = AddProduct
		fields = ['product_name', 'title', 'launched_time', 'Prices', 'causel', 'details', 'topic']

''' Article form view   '''
class Article_form(forms.ModelForm):
	class Meta:
		model = Article
		fields = ['title', 'description', 'Initial_keyword_choices', 'topic' ]


''' User Contact form view   '''
class Contact_form(forms.ModelForm):
	class Meta:
		model = UserContactForm
		fields = ['name', 'email', 'topic', 'write' ]
