from django.contrib import admin
from .models import Broucher
# Register your models here.

class BroucherAdmin(admin.ModelAdmin):
    list_display=['course','title','broucher_desc']
admin.site.register(Broucher,BroucherAdmin)