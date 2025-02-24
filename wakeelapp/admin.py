from django.contrib import admin
from .models import (
    BlogCategory,
    Blogs,
    VideoCategory,
    Videos,
)

@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at"]
    

@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):
    list_display = ["title", "slug"]


@admin.register(VideoCategory)
class VideoCategoryAdmin(admin.ModelAdmin):
        list_display = ["name", "created_at"]

@admin.register(Videos)
class VideosAdmin(admin.ModelAdmin):
    list_display = ["title", "slug"]
