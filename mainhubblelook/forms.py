from django import forms 
from .models import MainModel, UserContactForm, OfficalLetter


''' Thought Post form view   '''
class Quick_word_form(forms.ModelForm):
	class Meta:
		model = MainModel
		fields = ['micro_thought', 'Initial_keyword_for_thoughts', 'topic']
		widgets={'micro_thought': forms.Textarea(attrs={'size': 10, 'placeholder': 'Do not write more than 200 words'})}
	
''' Add Product form view   ''' 
class Add_product_view(forms.ModelForm):
	class Meta:
		model = MainModel
		fields = ['product_name', 'product_title', 'product_url', 'launched_time', 'Prices', 'causel', 'product_details', 'topic']

''' Article form view   '''
class Article_form(forms.ModelForm):
	class Meta:
		model = MainModel
		fields = ['article_title', 'micro_article', 'Initial_keyword_for_articles', 'topic' ]


''' User Contact form view   '''
class Contact_form(forms.ModelForm):
	class Meta:
		model = UserContactForm
		fields = ['name', 'email', 'topic', 'write' ]

''' Official letter form   '''
class Official_Letter_Form(forms.ModelForm):
	class Meta:
		model = OfficalLetter
		fields = [ 'title', 'to_whom', 'letter', 'letter_from' ]































































