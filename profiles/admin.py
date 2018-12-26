from django.contrib import admin
from .models import Profile, Team, About, Investment

# Register your models here.
admin.site.register(Profile)
admin.site.register(About)
admin.site.register(Team)
admin.site.register(Investment)
