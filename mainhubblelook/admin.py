from django.contrib import admin
from .models import QuickWord, AddProduct, Article, UserContactForm


admin.site.register(QuickWord) 
admin.site.register(AddProduct)
admin.site.register(Article)
admin.site.register(UserContactForm)