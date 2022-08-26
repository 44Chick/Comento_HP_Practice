from . import views
from django.urls import path, include, re_path

urlpatterns = [
    path('',views.index_template, name='index'),
    path('product/',views.product_view, name="product"),
    path('<int:content_id>/', views.detail, name='detail'),
    path('comment/<int:content_id>/', views.comment_create, name='comment_create'),
    path('comment/create/<int:content_id>/', views.comment_create, name='comment_create'), 
    path('comment/update/<int:comment_id>/', views.comment_update, name='comment_update'), 
    path('comment/delete/<int:comment_id>/', views.comment_delete, name='comment_delete'), 
    ]

