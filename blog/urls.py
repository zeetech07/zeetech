from django.urls import path
from . import views

urlpatterns = [
    path('all_blog/', views.all_blog, name='all_blog'),
    path('blog_detail/<int:blog_id>/', views.blog_details, name='blog_detail'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('data_analyst/', views.static_page, {'template': 'blogs/data_analyst.html'}, name='data_analyst'),
    path('data_science/', views.static_page, {'template': 'blogs/data_science.html'}, name='data_science'),
    path('digital_marketing/', views.static_page, {'template': 'blogs/digital_marketing.html'}, name='digital_marketing'),
    path('python_full_stack/', views.static_page, {'template': 'blogs/python_full_stack.html'}, name='python_full_stack'),
    path('software_testing/', views.static_page, {'template': 'blogs/software_testing.html'}, name='software_testing'),
    path('stock_marketing/', views.static_page, {'template': 'blogs/stock_marketing.html'}, name='stock_marketing'),
    path('graphic_designing/', views.static_page, {'template': 'blogs/graphic_designing.html'}, name='graphic_designing'),
    path('cloud_computing/', views.static_page, {'template': 'blogs/cloud_computing.html'}, name='cloud_computing'),
    path('360°/', views.static_page, {'template': 'blogs/360_degree.html'}, name='360_degree'),
]