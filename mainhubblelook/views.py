from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.db.models import Q  # Q lookup for Search
from django.views.generic.base import ContextMixin, RedirectView
from django.views.generic import ListView, TemplateView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView, FormView
from .models import MainModel, UserContactForm, OfficalLetter
from profiles.models import Profile
from .forms import Quick_word_form, Add_product_view, Article_form, Contact_form, Official_Letter_Form


# template view and search view
# this view passes all data to the homepage
class QuickWordView(ListView):

    template_name = "index.html"
    queryset = MainModel.objects.all()
    context_object_name = 'posts'

    def get_context_data(self, **Kwargs):
        context = super(QuickWordView, self).get_context_data(**Kwargs)
        official_letter = OfficalLetter.objects.all()
        main_model = MainModel.objects.all()
        query = self.request.GET.get('q')
        if query:
            add_product = main_model.filter(Q(product_name__icontains=query) | Q(Prices__icontains=query) | Q(details__icontains=query)
                | Q(title__icontains=query)| Q(launched_time__icontains=query) | Q(topic__icontains=query) )
            official_letter = official_letter.filter(Q(title__icontains=query)| Q(pub_time__icontains=query) |Q(letter__icontains=query))
        elif query != query:
            raise messages.info(request, 'not match search result found')

        context['official_letter'] = official_letter
        context['main_model'] = main_model

        return context




'''
Quickword form as users can post from here 
Addproduct form as users can post from here
article form as users can post from here

'''

# Product page view 
def Offical_Letter_Detail_View(request, id, slug):
    letter = OfficalLetter.objects.get(id=id)
    context = {
    'official_letter': letter,
    }
    return render(request, 'official-letter-view.html', context)


class QuickWordForm(CreateView):     # Microthought form view 
    form_class = Quick_word_form
    template_name = 'forms/quickword.html'
    success_url = '/'


class AddproductForm(CreateView):   #product form view 
    form_class = Add_product_view
    template_name = 'forms/addproduct_form.html'
    success_url = '/'

class Article_form(CreateView):    #Article form view 
    form_class = Article_form
    template_name = 'forms/article-form.html'
    success_url = '/'



# Product page view 
def Product_detials_View(request, id, slug):
    product = MainModel.objects.get(id=id)
    context = {
    'addproduct': product,
    }
    return render(request, 'addproduct_details.html', context)
    
# article page view
def article_detials(request, id, slug):
    
    article = MainModel.objects.get(id=id)
    context = {
    'article': article,
    }
    return render(request, 'article-details.html', context)


#single page template view
#Contact View with form for customers 
class ContactView(CreateView):
    template_name= "footer/Contact.html"
    form_class = Contact_form
    success_url = '/Contact-View/'


 #Why Hubblelook template view.
class WhyHubblelookView(TemplateView):
    
    template_name= "why-hubblelook.html"


  #learn more template view      
class ExploreView(TemplateView):

	template_name= "footer/explore.html"

 #about template view.
class AboutView(TemplateView):

	template_name= "footer/about.html"


  #learn more template view      
class ProductView(TemplateView):

    template_name= "footer/products.html"

 # Investment and contribution page View
class InvConView(TemplateView):

    template_name= "footer/investmentandcontribution.html"



 #about template view.
class PrivacyAndTermsView(TemplateView):

    template_name= "footer/Privacy-and-terms.html"













