from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.first_view, name='first_view'),
]