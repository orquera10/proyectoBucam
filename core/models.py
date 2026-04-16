from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify


class Post(models.Model):
    class Tone(models.TextChoices):
        PRIMARY = 'primary', 'Primary'
        SECONDARY = 'secondary', 'Secondary'
        ACCENT = 'accent', 'Accent'

    title = models.CharField(max_length=180)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    excerpt = models.TextField(max_length=280)
    body = models.TextField(blank=True)
    image = models.ImageField(upload_to='posts/', blank=True)
    eyebrow = models.CharField(max_length=80, blank=True)
    tone = models.CharField(
        max_length=20,
        choices=Tone.choices,
        default=Tone.PRIMARY,
    )
    is_featured = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    published_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_at', '-created_at']
        verbose_name = 'entrada'
        verbose_name_plural = 'entradas'

    def __str__(self):
        return self.title

    @property
    def description(self):
        return self.excerpt

    @property
    def image_url(self):
        if self.image:
            return self.image.url
        return ''

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)[:180] or 'entrada'
            slug = base_slug
            counter = 2
            while Post.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f'{base_slug[:170]}-{counter}'
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('core:post_detail', kwargs={'slug': self.slug})
