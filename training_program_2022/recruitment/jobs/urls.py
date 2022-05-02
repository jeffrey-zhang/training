from django.urls import re_path
from jobs import views

urlpatterns = [
    re_path(r'^joblist/', views.joblist, name='joblist'),
]
