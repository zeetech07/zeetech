from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 
from . import views

urlpatterns=[
    path('contactus/',views.contactus,name="contactus"),
    path('councelling/',views.councelling,name="councelling"),
   
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])