from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView, UpdateView, DeleteView


class IndexView(TemplateView):
	template_name = 'index.html'


# Create your views here.
