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
    path('official-letter-details/<int:id>/<slug:slug>', views.Offical_Letter_Detail_View, name='letter-details'),
    # article detials view
    path('article-details/<int:id>/<slug:slug>', views.article_detials, name='details'),
    #product page view
    path('product-details/<int:id>/<slug:slug>', views.Product_detials_View, name='add-product-view'),    
    # form view 
    path('quick-word/', QuickWordForm.as_view(), name='quick-word'),
    path('add-product/', AddproductForm.as_view(), name='add-product-form'),
    path('article/', Article_form.as_view(), name='article-form'), 

]