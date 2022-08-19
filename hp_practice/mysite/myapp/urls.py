from . import views
from django.urls import path, include, re_path


urlpatterns = [
    path('',views.index_template, name='index'),]
