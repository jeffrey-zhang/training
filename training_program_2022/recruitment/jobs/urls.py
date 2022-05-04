from django.urls import re_path
from jobs import views

urlpatterns = [
    re_path(r'^joblist/', views.joblist, name='joblist'),
    re_path(r'^job/(?P<job_id>\d+)/$', views.detail, name='detail'),
]
