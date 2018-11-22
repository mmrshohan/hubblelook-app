from django.contrib import admin
from .models import UserContactForm, MainModel, OfficalLetter

admin.site.register(MainModel) 
admin.site.register(OfficalLetter)
admin.site.register(UserContactForm)