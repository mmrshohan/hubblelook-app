from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from . import views
from .views import ( 
    ProfileView, 
    Offical_Letter_View, Offical_Letter_Create_View, Offical_Letter_Update_View, 
    Offical_Letter_Delete_View,
    ProfileCreateView,
    #ProfileUpdateView,
    MicroThoughtsSortView, 
    ProductSortView, 
    ArticleSortView, 
    AddProductUpdateView, AddProductDeleteView,
    MicroThoughtsDeleteView, MicroThoughtsUpdateView, 
    ArticleUpdateView, ArticleDeleteView, 
    TeamPageView, Team_Create_View, Team_Update_View, Team_Delete_View
    )


app_name = 'profiles'

urlpatterns = [
    path('<username>/', ProfileView.as_view(), name='portfolio'),
    #offical letter
    #Micro thought delete view
    path('<username>/micro-thoughts/delete/<int:pk>', MicroThoughtsDeleteView.as_view(), name='micro-thoughts-delete'),
    path('<username>/products/', ProductSortView.as_view(), name='Product-sort'),
    path('<username>/articles/', ArticleSortView.as_view(), name='Article-sort'),
    path('<username>/micro-thoughts/', MicroThoughtsSortView.as_view(), name='Micro-thought-sort'),
    #edit profile update 
    path('<username>/create', ProfileCreateView.as_view(), name='create-profile'),

    #Microthought Post update/delete view 
    path('quick_word/update/<int:pk>', MicroThoughtsUpdateView.as_view(), name='micro-thoughts-update'),
    path('quick_word/delete/<int:pk>', MicroThoughtsDeleteView.as_view(), name='micro-thoughts-delete'),

    #AddProduct Post update/delete view 
    path('product/update/<int:pk>', AddProductUpdateView.as_view(), name='Add-product-update'),
    path('product/delete/<int:pk>', AddProductDeleteView.as_view(), name='Add-product-delete'),

    #Article Post update/delete view 
    path('article/update/<int:pk>', ArticleUpdateView.as_view(), name='article-update'),
    path('article/delete/<int:pk>', ArticleDeleteView.as_view(), name='article-delete'),

    path('<username>/official-letter-list-view', Offical_Letter_View.as_view(), name='letter-list-view'),
    path('<username>/create-official-letter', Offical_Letter_Create_View.as_view(), name='create-official-letter'),


    #Team page View
    path('<username>/team/', TeamPageView.as_view(), name='team-page'),
    path('<username>/team-form/', Team_Create_View.as_view(), name='team-form'),
    path('<username>/team-update/<int:pk>', Team_Update_View.as_view(), name='team-form-update'),
    path('<username>/team-delete/<int:pk>', Team_Delete_View.as_view(), name='team-form-delete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)