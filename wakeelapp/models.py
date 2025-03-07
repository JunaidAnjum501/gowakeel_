from django.db import models
from cloudinary.models import CloudinaryField


class BlogCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Blogs(models.Model):
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE,related_name="blogs")
    title = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.SlugField(max_length=255, unique=True)
    image = CloudinaryField()

    def __str__(self):
        return self.title


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class VideoCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Videos(models.Model):
    category = models.ForeignKey(VideoCategory, on_delete=models.CASCADE, related_name="videos")
    title = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField(upload_to="videos")
    link = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_embed_url(self):
        return f"{self.link}"


