from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Post


def home(request):
    posts = Post.objects.filter(
        is_published=True,
        published_at__lte=timezone.now(),
    )
    featured_posts = list(posts.filter(is_featured=True)[:5])
    recent_posts = list(posts[:6])

    fallback_services = [
        {
            'eyebrow': 'Cobertura 24/7',
            'title': 'Custodia VIP con protocolos de respuesta inmediata',
            'description': 'Equipos entrenados para traslados, eventos, ejecutivos y protección de activos sensibles.',
            'tone': 'primary',
            'image_url': '',
            'published_at': None,
        },
        {
            'eyebrow': 'Unidad especializada',
            'title': 'Custodia femenina con presencia profesional y visión integral',
            'description': 'Perfiles preparados para entornos corporativos, recepciones ejecutivas y acompañamiento estratégico.',
            'tone': 'secondary',
            'image_url': '',
            'published_at': None,
        },
        {
            'eyebrow': 'Monitoreo inteligente',
            'title': 'Videovigilancia e instalación de tecnología de control',
            'description': 'Diseñamos, instalamos y supervisamos sistemas de CCTV, alarmas y puestos de monitoreo.',
            'tone': 'accent',
            'image_url': '',
            'published_at': None,
        },
    ]

    capabilities = [
        'Guardias habilitados y supervisión en terreno',
        'Cobertura para industrias, consorcios y eventos',
        'Monitoreo con protocolos y reportes de incidentes',
        'Tecnología de acceso, CCTV y control perimetral',
    ]

    metrics = [
        {'value': '24/7', 'label': 'Centro operativo y soporte permanente'},
        {'value': '15+', 'label': 'Años de experiencia en seguridad privada'},
        {'value': '100%', 'label': 'Planes adaptados a la operación del cliente'},
    ]

    fallback_recent = [
        {
            'title': 'Protección de instalaciones y control de accesos',
            'excerpt': 'Diseñamos anillos de seguridad con presencia visible, control documental y protocolos de ingreso.',
            'published_at': None,
        },
        {
            'title': 'Cobertura ejecutiva para traslados y eventos',
            'excerpt': 'Acompañamiento profesional para personas expuestas, comitivas y reuniones de alta sensibilidad.',
            'published_at': None,
        },
        {
            'title': 'Puestos de monitoreo y análisis preventivo',
            'excerpt': 'Integración de cámaras, reportes y alertas para anticipar incidentes y responder con velocidad.',
            'published_at': None,
        },
    ]

    context = {
        'featured_services': featured_posts or fallback_services,
        'capabilities': capabilities,
        'metrics': metrics,
        'recent_highlights': recent_posts or fallback_recent,
    }
    return render(request, 'core/home.html', context)


def post_detail(request, slug):
    post = get_object_or_404(
        Post,
        slug=slug,
        is_published=True,
        published_at__lte=timezone.now(),
    )
    recent_posts = Post.objects.filter(
        is_published=True,
        published_at__lte=timezone.now(),
    ).exclude(pk=post.pk)[:3]
    return render(
        request,
        'core/post_detail.html',
        {
            'post': post,
            'recent_posts': recent_posts,
        },
    )
