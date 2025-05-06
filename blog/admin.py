from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Blog,Category
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display=['title','category','description','image','created_at',]
admin.site.register(Blog,BlogAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display=['name']
admin.site.register(Category,CategoryAdmin)