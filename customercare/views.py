
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import CreateView, FormView
from django.contrib.messages.views import SuccessMessageMixin
from customercare.forms import Knowledge_center_form
from customercare.models import KnowledgeCenter 
from django.db.models import Q  # Q lookup for Search 
from django.contrib import messages # to deliver message

# Create your views here.

class KnowledgeCenterView(ListView):
	template_name = 'customercare.html'
	queryset = KnowledgeCenter.objects.all()
	context_object_name = 'blogs'

	# Customer care search facility

	def get_context_data(self, *args, **Kwargs):
		context = super(KnowledgeCenterView, self).get_context_data(*args, **Kwargs)
		query = self.request.GET.get("q")
		qs = KnowledgeCenter.objects.filter()
		if query:
			qs = qs.filter(
				Q(title__icontains=query) | Q(details__icontains=query) | Q(topic__icontains=query) | Q(slug__icontains=query)
				)
			
		context['blogs'] = qs
		return context



def CustomerCareArticle(request, id, slug):
    blogs = KnowledgeCenter.objects.get(id=id)
    context = {
    'blogs': blogs,
    }
    return render(request, 'Customercare-article.html', context)










