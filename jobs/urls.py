from django.urls import path

from . import views
from jobs.views import JobView



urlpatterns = [
    path('', JobView.as_view(), name='job-view'),
]