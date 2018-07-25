from django.shortcuts import render
from django.urls import reverse
from django.urls import reverse_lazy

from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, TemplateView
from django.views.generic.base import ContextMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from mainhubblelook.models import QuickWord, AddProduct, Article
from profiles.models import Profile, OfficalLetter
from .forms import Edit_Profile_Form, Official_Letter_Form
from mainhubblelook.forms import Quick_word_form, Add_product_view, Article_form


'''
class Edit_Profile_View(TemplateView):
	template_name = "edit-profile.html"
'''

class ProfileView(ListView):

    template_name = "profile.html"
    queryset = QuickWord.objects.all()
    context_object_name = 'quickword'


    def get_context_data(self, **Kwargs):
        context = super(ProfileView, self).get_context_data(**Kwargs)
        context['addproduct'] = AddProduct.objects.all()
        context['article_view'] = Article.objects.all()
        context['edit'] = Profile.objects.all().last()
        context['official_letter'] = OfficalLetter.objects.all()
        return context


class Edit_Profile_View(CreateView):          #  Edit create view
    form_class = Edit_Profile_Form
    model = Profile
    template_name = "edit-profile.html"
    success_url = '/profile/'

class Edit_profile_Update_View(UpdateView):   # Edit update view
    form_class = Edit_Profile_Form
    model = Profile
    template_name = "edit-profile.html"
    success_url = "/profile/"


#Micro Thoughts update view                     microthought update view
class MicroThoughtsUpdateView(UpdateView):
    model = QuickWord
    form_class = Quick_word_form
    template_name = 'forms/quickword.html'
    success_url = '/'
#Micro Thoughts delete View                     microthought delete view

class MicroThoughtsDeleteView(DeleteView):
    model = QuickWord
    form_class = Quick_word_form
    template_name = 'profile.html'
    success_url = reverse_lazy('profile')

#Add product update UpdateView                   addProduct Update view 
class AddProductUpdateView(UpdateView):
    model = AddProduct
    form_class = Add_product_view
    template_name = 'forms/addproduct_form.html'
    success_url = '/profile/'

#Add prodcuct delete View                        addproduct  delete view 
class AddProductDeleteView(DeleteView):
    model = AddProduct
    form_class = Add_product_view
    template_name = 'profile.html'
    success_url = reverse_lazy('profile')


#Add product update UpdateView                   Article update view
class ArticleUpdateView(UpdateView):
    model = Article
    form_class = Article_form
    template_name = 'forms/article-form.html'
    success_url = '/profile/'

#Add prodcuct delete View                        Article delete view
class ArticleDeleteView(DeleteView):
    model = Article
    form_class = Article_form
    template_name = 'profile.html'
    success_url = reverse_lazy('profile')


class Offical_Letter_View(ListView):                    # Official letter list view 
    template_name = 'offical-letter-list-view.html'
    queryset = OfficalLetter.objects.all()
    context_object_name = 'letter_list'


# Product page view 
def Offical_Letter_Detail_View(request, id, slug, username):       #official letter details view 
    letter = OfficalLetter.objects.get(id=id)
    context = {
    'letter': letter,
    }
    return render(request, 'official-letter-view.html', context)    

class Offical_Letter_Create_View(CreateView):          # official letter create view 
    form_class = Official_Letter_Form
    model = OfficalLetter
    template_name = "official-letter-form.html"
    success_url = "/offical-letter-view/"


class Offical_Letter_Update_View(UpdateView):         # official letter update view
    model = OfficalLetter
    form_class = Official_Letter_Form
    template_name = 'official-letter-form.html'
    success_url = "/offical-letter-view/"

class Offical_Letter_Delete_View(DeleteView):      # official letter delete view
    model = OfficalLetter
    form_class = Official_Letter_Form
    template_name = 'offical-letter-list-view.html'
    success_url = reverse_lazy( 'offical-letter-view')





'''
sort views are created to see how many post has been
posted by that user in details 
'''
class MicroThoughtsSortView(ListView):
    template_name= "Sort-model/micro-thought-sort.html"
    queryset = QuickWord.objects.all()
    context_object_name = 'quickword'


class ProductSortView(ListView):
    template_name= "Sort-model/product-sort.html"
    queryset = AddProduct.objects.all()
    context_object_name = 'addproduct'

class ArticleSortView(ListView):
    template_name= "Sort-model/article-sort.html"
    queryset = Article.objects.all()
    context_object_name = 'article_view'








	
