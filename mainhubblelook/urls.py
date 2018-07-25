from django.urls import path
from . import views
from mainhubblelook.views import IndexView


urlpatterns = [
    path('', IndexView.as_view(), name='home'), 


]