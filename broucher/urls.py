from django.urls import path
from .import views

urlpatterns=[
    path('broucher/<int:id>/',views.broucher,name="broucher")
]



