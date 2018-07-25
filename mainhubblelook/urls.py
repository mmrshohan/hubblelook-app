from django.urls import path
from . import views
from mainhubblelook.views import ( QuickWordView,
 #ArticleDetailsView, 
 Product_detials_View, 
 QuickWordForm, 
 AddproductForm, 
 Article_form, 
 Offical_Letter_Detail_View, 
 article_detials,


 )
	

urlpatterns = [
    path('', QuickWordView.as_view(), name='home'), 
     # official letter detials view
    path('official_letter/details/<int:pk>', Offical_Letter_Detail_View.as_view(), name='offical-letter-details-view'),
    # article and add_product detials view
    path('article_details/<int:id>/<slug:slug>', views.article_detials, name='details'),
    #path('article_details/<int:pk>', ArticleDetailsView.as_view(), name='details'), # article details page view
    #product page view
    path('product_details/<int:id>/<slug:slug>', views.Product_detials_View, name='add-product-view'),    
    # form view 
    path('quick_word/', QuickWordForm.as_view(), name='quick-word'),
    path('add_product/', AddproductForm.as_view(), name='add-product-form'),
    path('article/', Article_form.as_view(), name='article-form'), 

]