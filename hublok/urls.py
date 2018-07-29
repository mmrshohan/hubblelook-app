"""hublok URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from mainhubblelook.views import ( ExploreView, 
 AboutView, 
 InvConView, 
 ContactView, 
 ProductView,
 PrivacyAndTermsView 
 )

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('', include('mainhubblelook.urls')),
    path('accounts/', include('allauth.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('profile/', include('profiles.urls')),
    path('knowledge/', include('customercare.urls')),   # Customer support page
    path('jobs/', include('jobs.urls')),

    #footer URL 
    path('learn/', ExploreView.as_view(), name='explore'),
    path('about/', AboutView.as_view(), name='about'),
    path('products/', ProductView.as_view(), name='products'),
    path('privacy_and_terms/', PrivacyAndTermsView.as_view(), name='Privacy-View'),
    path('investment_and_contribution/', InvConView.as_view(), name='InvCon-view'),
    path('contact/', ContactView.as_view(), name='Contact-View'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)