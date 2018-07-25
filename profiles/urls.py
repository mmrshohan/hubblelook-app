from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from . import views
from profiles.views import ( 
    ProfileView, 
    Offical_Letter_View, Offical_Letter_Create_View, Offical_Letter_Detail_View, Offical_Letter_Update_View, 
    Offical_Letter_Delete_View,
    Edit_Profile_View, 
    Edit_profile_Update_View, 
    MicroThoughtsSortView, 
    ProductSortView, 
    ArticleSortView, 
    AddProductUpdateView, AddProductDeleteView,
    MicroThoughtsDeleteView, MicroThoughtsUpdateView, 
    ArticleUpdateView, ArticleDeleteView
    )



urlpatterns = [
    path('<username>/', ProfileView.as_view(), name='profile'),
    #offical letter 
    path('<username>/official_letter/', Offical_Letter_View.as_view(), name='offical-letter-view'),
    path('<username>/official_letter_form/', Offical_Letter_Create_View.as_view(), name='offical-letter-form'),
    path('<username>/official_letter/details/<int:id>/<slug:slug>', views.Offical_Letter_Detail_View, name='offical-letter-details-view'),
    path('official_letter/update/<int:pk>', Offical_Letter_Update_View.as_view(), name='offical-letter-update-view'),
    path('official_letter/delete/<int:pk>', Offical_Letter_Delete_View.as_view(), name='offical-letter-delete-view'),

    path('<username>/micro-thoughts/', MicroThoughtsSortView.as_view(), name='Micro-thought-sort'),
    path('<username>/products/', ProductSortView.as_view(), name='Product-sort'),
    path('<username>/articles/', ArticleSortView.as_view(), name='Article-sort'),
    #edit profile update 
    path('<username>/edit/', Edit_Profile_View.as_view(), name='edit-profile'),
    path('edit/update/<username>/<int:pk>', Edit_profile_Update_View.as_view(), name='edit-profile-update'),
    #Microthought Post update/delete view 
    path('quick_word/update/<int:pk>', MicroThoughtsUpdateView.as_view(), name='micro-thoughts-update'),
    path('quick_word/delete/<int:pk>', MicroThoughtsDeleteView.as_view(), name='micro-thoughts-delete'),

    #AddProduct Post update/delete view 
    path('add_product/update/<int:pk>', AddProductUpdateView.as_view(), name='Add-product-update'),
    path('add_product/delete/<int:pk>', AddProductDeleteView.as_view(), name='Add-product-delete'),

    #AddProduct Post update/delete view 
    path('article/update/<int:pk>', ArticleUpdateView.as_view(), name='article-update'),
    path('article/delete/<int:pk>', ArticleDeleteView.as_view(), name='article-delete'),


] 