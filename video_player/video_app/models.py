"""
Model for video app.
"""

from django.db import models
from core.models import BaseModel
from django.core.validators import FileExtensionValidator 
from django.conf import settings

class Category(BaseModel):
    title = models.CharField(max_length=255,null=True)
    slug = models.SlugField(null=True)
    image = models.ImageField(upload_to='cat/image',null=True)

    def __str__(self) -> str:
        return self.title

class Product(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    slug = models.SlugField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255,blank=True,null=True)
    image = models.ImageField(upload_to='image', null=True)
    video = models.FileField(upload_to='videos',null=True,
            validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    
    class Meta:
        ordering = ['created_at']

    def __str__(self) -> str:
        return f'{self.user} {self.title}'