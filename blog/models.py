
# Create your models here.
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="blogs")
    description = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    # content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    details = models.TextField(blank=True, null=True)  # New field for more details

    def __str__(self):
        return self.title
