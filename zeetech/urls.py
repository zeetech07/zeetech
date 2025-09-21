"""
URL configuration for zeetech project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# 
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static 
from. import views
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template.loader import render_to_string

def sitemap_xml_view(request):
    xml_content = render_to_string("sitemap.xml")
    return HttpResponse(xml_content, content_type="application/xml")


def robots_txt_view(request):
    content = render_to_string("robots.txt")
    return HttpResponse(content, content_type="text/plain")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('academy.urls')), 
    # path('',views.home,name="home"),
    path('academy/',include('academy.urls')),
    path('broucher/',include('broucher.urls')),
    path('blog/',include('blog.urls')),
    path('contact/',include('contact.urls')),
    path('sitemap/', TemplateView.as_view(template_name='sitemap.html'), name='sitemap'),
    path('sitemap.xml', sitemap_xml_view, name='sitemap1'),
    path('robots.txt', robots_txt_view, name='robots_txt'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])