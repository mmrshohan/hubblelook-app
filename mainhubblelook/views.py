from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.db.models import Q  # Q lookup for Search
from django.views.generic.base import ContextMixin, RedirectView
from django.views.generic import ListView, TemplateView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView, FormView
from .models import QuickWord, AddProduct, Article, UserContactForm
from profiles.models import Profile, OfficalLetter
from .forms import Quick_word_form, Add_product_view, Article_form, Contact_form


# template view 
class QuickWordView(ListView):

    template_name = "index.html"
    queryset = QuickWord.objects.all()
    context_object_name = 'quickword'

    def get_context_data(self, **Kwargs):
        context = super(QuickWordView, self).get_context_data(**Kwargs)
        thought = QuickWord.objects.all()
        add_product = AddProduct.objects.all()
        article = Article.objects.all()
        official_letter = OfficalLetter.objects.all()
        query = self.request.GET.get('q')
        if query:
            thought = thought.filter(Q(description__icontains=query)| Q(Initial_keyword_choices__icontains=query) |Q(topic__icontains=query))
            article = article.filter(Q(title__icontains=query) | Q(description__icontains=query) | Q(Initial_keyword_choices__icontains=query))
            add_product = add_product.filter(Q(product_name__icontains=query) | Q(Prices__icontains=query) | Q(details__icontains=query)
                | Q(title__icontains=query)| Q(launched_time__icontains=query) | Q(topic__icontains=query) )
            official_letter = official_letter.filter(Q(title__icontains=query)| Q(pub_time__icontains=query) |Q(letter__icontains=query) | Q(topic__icontains=query))

        context['addproduct'] = add_product
        context['article_view'] = article
        context['official_letter'] = official_letter
        context['quickword'] = thought
        
        return context




'''
Quickword form as users can post from here 
Addproduct form as users can post from here
article form as users can post from here

'''
class Offical_Letter_Detail_View(DetailView):   # official letter details view 
    template_name = 'official-letter.html'
    model = OfficalLetter
    queryset = OfficalLetter.objects.all()
    context_object_name = 'letter'


class QuickWordForm(CreateView):     # Microthought form view 
    form_class = Quick_word_form
    template_name = 'forms/quickword.html'
    success_url = '/home/'


class AddproductForm(CreateView):   #product form view 
    form_class = Add_product_view
    template_name = 'forms/addproduct_form.html'
    success_url = '/home/'

class Article_form(CreateView):    #Article form view 
    form_class = Article_form
    template_name = 'forms/article-form.html'
    success_url = '/home/'



# Product page view 
def Product_detials_View(request, id, slug):
    product = AddProduct.objects.get(id=id)
    context = {
    'addproduct': product,
    }
    return render(request, 'addproduct_details.html', context)
    
# article page view
def article_detials(request, id, slug):
    article = Article.objects.get(id=id)
    context = {
    'article': article,
    }
    return render(request, 'article-details.html', context)



#Contact View with form for customers 
class ContactView(CreateView):
    template_name= "Contact.html"
    form_class = Contact_form
    success_url = '/Contact-View/'



  #learn more template view      
class ExploreView(TemplateView):

	template_name= "explore.html"

 #about template view.
class AboutView(TemplateView):

	template_name= "about.html"


  #learn more template view      
class ProductView(TemplateView):

    template_name= "products.html"

 # Investment and contribution page View
class InvConView(TemplateView):

    template_name= "investmentandcontribution.html"



 #about template view.
class PrivacyAndTermsView(TemplateView):

    template_name= "Privacy-and-terms.html"













