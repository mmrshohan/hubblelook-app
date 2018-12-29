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
# Models from Mianhubblelook app
from mainhubblelook.models import MainModel, OfficalLetter
# froms Mianhubblelook app
from mainhubblelook.forms import Official_Letter_Form

from profiles.models import Profile, Team
from .forms import Edit_Profile_Form, TeamForm
from mainhubblelook.forms import Quick_word_form, Add_product_view, Article_form  


user = get_user_model


class ProfileView(ListView):

    template_name = "profile.html"
    queryset = MainModel.objects.all()
    context_object_name = 'posts'


    def get_context_data(self, **Kwargs):
        context = super(ProfileView, self).get_context_data(**Kwargs)
        context['official_letter'] = OfficalLetter.objects.all()
        context['edit'] = Profile.objects.all().first()
        return context


class ProfileCreateView(CreateView):         #Profile create view
    model = Profile
    form_class = Edit_Profile_Form
    template_name = "edit-profile.html"
    success_url = '/portfolio/'

# ---------  thought update and delete view ---------------------

#Micro Thoughts update view                     microthought update view
class MicroThoughtsUpdateView(UpdateView):
    model = MainModel
    form_class = Quick_word_form
    template_name = 'forms/quickword.html'
    success_url = '/'
#Micro Thoughts delete View                     microthought delete view

class MicroThoughtsDeleteView(DeleteView):
    model = MainModel
    form_class = Quick_word_form
    template_name = 'profile.html'
    success_url = '/'

# ---------  thought update and delete view end here ---------------------



# ---------  product update and delete view ---------------------

                                              #Product Update view 
class AddProductUpdateView(UpdateView):
    model = MainModel
    form_class = Add_product_view
    template_name = 'forms/addproduct_form.html'
    success_url = '/'

                                              #product  delete view 
class AddProductDeleteView(DeleteView):
    model = MainModel
    form_class = Add_product_view
    template_name = 'profile.html'
    success_url = "/"

# ---------  product update and delete view end here ---------------------


#Add product update UpdateView                   Article update view
class ArticleUpdateView(UpdateView):
    model = MainModel
    form_class = Article_form
    template_name = 'forms/article-form.html'
    success_url = '/'

#Add prodcuct delete View                        Article delete view
class ArticleDeleteView(DeleteView):
    model = MainModel
    form_class = Article_form
    template_name = 'profile.html'
    success_url = reverse_lazy('profiles:portfolio')

# ---------  All views for official letter ---------------------

class Offical_Letter_View(ListView):                    # Official letter list view 
    template_name = 'offical-letter-list-view.html'
    queryset = OfficalLetter.objects.all()
    context_object_name = 'letter_list'

class Offical_Letter_Create_View(CreateView):          # official letter create view 
    form_class = Official_Letter_Form
    model = OfficalLetter
    template_name = "official-letter-form.html"
    success_url = "/"


class Offical_Letter_Update_View(UpdateView):         # official letter update view
    model = OfficalLetter
    form_class = Official_Letter_Form
    template_name = 'official-letter-form.html'
    success_url = "/"

class Offical_Letter_Delete_View(DeleteView):      # official letter delete view
    model = OfficalLetter
    form_class = Official_Letter_Form
    template_name = 'offical-letter-list-view.html'
    success_url = "/"

# ---------  All views for official letter end here ---------------------



# ---------  post's sort view ---------------------
class MicroThoughtsSortView(ListView):
    template_name= "Sort-model/micro-thought-sort.html"
    queryset = MainModel.objects.all()
    context_object_name = 'posts'


class ProductSortView(ListView):
    template_name= "Sort-model/product-sort.html"
    queryset = MainModel.objects.all()
    context_object_name = 'posts'

class ArticleSortView(ListView):
    template_name= "Sort-model/article-sort.html"
    queryset = MainModel.objects.all()
    context_object_name = 'posts'

# ---------  post's sort view end here ---------------------

# ---------  Team page create and edit view ------------
class TeamPageView(TemplateView):

    template_name = "team/team.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['team'] = Team.objects.all().first()
        return context

class Team_Create_View(CreateView):         
    form_class = TeamForm
    model = Team
    template_name = "team/team-form.html"
    success_url = "/"

class Team_Update_View(UpdateView):
    model = Team
    form_class = TeamForm
    template_name = 'team/team-form.html'
    success_url = "/"

class Team_Delete_View(DeleteView):
    model = Team
    form_class = TeamForm
    template_name = 'team/team.html'
    success_url = "/"

#-------  Team view end here ---------------

class Customer_Care_View(TemplateView):
    template_name = 'customer-care.html'

class Settings_View(TemplateView):
    template_name = 'settings.html'