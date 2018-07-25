from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import CreateView, FormView
from jobs.models import JobApplyView

# Create your views here.
# Simple job view
class JobView(ListView):
    template_name = "jobs.html"
    queryset = JobApplyView.objects.all()
    context_object_name = 'job'