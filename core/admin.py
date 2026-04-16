from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'is_published',
        'is_featured',
        'tone',
        'published_at',
    )
    list_filter = ('is_published', 'is_featured', 'tone', 'published_at')
    search_fields = ('title', 'excerpt', 'body', 'eyebrow')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('-published_at', '-created_at')
    readonly_fields = ('created_at', 'updated_at')
