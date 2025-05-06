from django.urls import path
from academy import views
# from .views import fetch_placements


urlpatterns = [
    path('courses/',views.courses,name="courses"),
    path('detail/<int:id>/',views.detail,name="detail"),
    path('contact/', views.contact, name='contact'),
    path('', views.home, name='home'),
    path("download-datascience-brochure/", views.download_datascience_brochure, name="download_datascience_brochure"),
    path('carrier/',views.carrier,name='carrier'),
    
]

  # path('companytieups/', views.companytieups, name='companytieups'),
    
    # path('experts/', views.experts, name='experts'),

    # path('courselist/<int:course_id>/', views.course_placements, name='courselist'),









   # path('courselist/<int:course_id>/',views.course_placements,name="courselist"),
  
    # path('fetch-placements/', fetch_placements, name='fetch_placements'),