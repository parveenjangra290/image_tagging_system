from django.contrib import admin
from .models import Tag, Images

@admin.register(Tag)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    search_fields = ('name',)


@admin.register(Images)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('image_name', 'description')