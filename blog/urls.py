from django.urls import path
from . import views

urlpatterns = [
    path('all_blog/', views.all_blog, name='all_blog'),
    path('blog_detail/<int:blog_id>/', views.blog_details, name='blog_detail'),  
    path('aboutus/', views.aboutus, name='aboutus'),  
    ]