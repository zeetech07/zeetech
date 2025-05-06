from django.shortcuts import render
from academy.models import Footer,Course
from cities_light.models import City
from academy.models import CarrierOpportunities

# import random


def home(request):
    courses=Course.objects.filter(course_name__in=["Data Science","Python full stack developer"]).prefetch_related('technologies')
    
    # print(courses)
     
    # ✅ Carrier ka data bhi home page par bhej raha
    cities = City.objects.filter(country__code2="IN")
    count=City.objects.count()
    print(count)
    
    context={
        'courses':courses,
        'cities':cities,

    }
  
    return render(request,'home/home.html',context)
    
