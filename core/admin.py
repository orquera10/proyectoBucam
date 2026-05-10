from django.contrib import admin

from .models import Post, PostGalleryImage


class PostGalleryImageInline(admin.TabularInline):
    model = PostGalleryImage
    extra = 0
    can_delete = True
    show_change_link = True
    fields = ('image', 'video', 'alt_text', 'order')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = (PostGalleryImageInline,)
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
    fieldsets = (
        (
            None,
            {
                'fields': (
                    'title',
                    'slug',
                    'eyebrow',
                    'excerpt',
                    'body',
                    'banner_image',
                    'body_image',
                ),
            },
        ),
        (
            'Publicacion',
            {
                'fields': (
                    'tone',
                    'is_featured',
                    'is_published',
                    'published_at',
                ),
            },
        ),
        (
            'Sistema',
            {
                'fields': ('created_at', 'updated_at'),
            },
        ),
    )


@admin.register(PostGalleryImage)
class PostGalleryImageAdmin(admin.ModelAdmin):
    list_display = ('post', 'alt_text', 'media_kind', 'order', 'created_at')
    list_filter = ('post', 'created_at')
    search_fields = ('post__title', 'alt_text')
    ordering = ('post', 'order', 'created_at')

    @admin.display(description='tipo')
    def media_kind(self, obj):
        return 'Video' if obj.is_video else 'Imagen'
