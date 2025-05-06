from django.shortcuts import render, get_object_or_404
from .models import Blog, Category

def all_blog(request):
    category_name = request.GET.get('category', None)  # URL se category fetch karega
    if category_name:
        blogs = Blog.objects.filter(category__name=category_name)  # Specific category ke blogs fetch karega
    else:
        blogs = Blog.objects.all()  # Sab blogs fetch karega

    categories = Category.objects.all()  # Saari categories dikhane ke liye
    return render(request, 'blog/blog.html', {'blogs': blogs, 'categories': categories})

def blog_details(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    categories = Category.objects.all()  # Ye line categories fetch karega
    return render(request, 'blog/blog_detail.html', {'blog': blog, 'categories': categories})

def aboutus(request):
    return render(request,"blog/aboutus.html")
