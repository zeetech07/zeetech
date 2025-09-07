from django.shortcuts import render, get_object_or_404
from .models import Blog, Category

from django.shortcuts import render

def all_blog(request):
    return render(request, 'blog/blog.html')

from django.shortcuts import render

def static_page(request, template):
    return render(request, template)

def blog_details(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    categories = Category.objects.all()  # Ye line categories fetch karega
    return render(request, 'blog/blog_detail.html', {'blog': blog, 'categories': categories})

def aboutus(request):
    return render(request,"blog/aboutus.html")
