from django import forms 
from .models import QuickWord, AddProduct, Article, UserContactForm


''' Thought Post form view   '''
class Quick_word_form(forms.ModelForm):
	class Meta:
		model = QuickWord
		fields = ['micro_thought', 'Initial_keyword_choices', 'topic']
		widgets={'micro_thought': forms.Textarea(attrs={'size': 10, 'placeholder': 'Do not write more than 200 words'})}
	
  

''' Add Product form view   ''' 
class Add_product_view(forms.ModelForm):
	class Meta:
		model = AddProduct
		fields = ['product_name', 'title', 'launched_time', 'Prices', 'causel', 'details', 'topic']

''' Article form view   '''
class Article_form(forms.ModelForm):
	class Meta:
		model = Article
		fields = ['title', 'micro_article', 'Initial_keyword_choices', 'topic' ]


''' User Contact form view   '''
class Contact_form(forms.ModelForm):
	class Meta:
		model = UserContactForm
		fields = ['name', 'email', 'topic', 'write' ]
