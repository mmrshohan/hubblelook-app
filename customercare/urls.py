from django.urls import path
from . import views
from customercare.views import KnowledgeCenterView, CustomerCareArticle




urlpatterns = [
    path('', KnowledgeCenterView.as_view(), name='customecare-view'),
    path('articles/<int:id>/<slug:slug>', views.CustomerCareArticle, name='customecare-article'),
]