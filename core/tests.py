from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Post


class HomeViewTests(TestCase):
    def test_home_page_renders_successfully(self):
        response = self.client.get(reverse('core:home'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'BUCAM S.R.L.')

    def test_home_page_uses_published_posts(self):
        post = Post.objects.create(
            title='Custodia VIP para eventos corporativos',
            excerpt='Entrada administrada desde Django admin.',
            body='Contenido extendido',
            is_featured=True,
            published_at=timezone.now(),
        )

        response = self.client.get(reverse('core:home'))

        self.assertContains(response, 'Custodia VIP para eventos corporativos')
        self.assertContains(response, 'Entrada administrada desde Django admin.')
        self.assertContains(response, post.get_absolute_url())

    def test_post_detail_renders_published_post(self):
        post = Post.objects.create(
            title='Monitoreo estratégico',
            excerpt='Resumen del monitoreo.',
            body='Contenido de detalle del post.',
            published_at=timezone.now(),
        )

        response = self.client.get(post.get_absolute_url())

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Contenido de detalle del post.')
