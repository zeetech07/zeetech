from django.db import models
from academy.models import Course
# Create your models here.
class Broucher(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    broucher_desc=models.TextField()
    file=models.FileField(upload_to='brouchers/')
    broucher_uploaded_at=models.DateTimeField(auto_now_add=True)
    
