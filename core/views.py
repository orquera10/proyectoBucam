from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from django.conf import settings
from django.utils import timezone

from .models import Post


NAV_PAGES = [
    {'slug': 'home', 'title': 'Inicio', 'url_name': 'core:home'},
    {'slug': 'mission', 'title': 'Mision y vision', 'url_name': 'core:mission'},
    {'slug': 'about', 'title': 'Quienes somos', 'url_name': 'core:about'},
    {'slug': 'services', 'title': 'Servicios', 'url_name': 'core:services'},
    {'slug': 'technology', 'title': 'Tecnologia', 'url_name': 'core:technology'},
]


TICKER_FALLBACK = [
    {
        'title': 'Protegemos lo que mas importa.',
        'excerpt': 'Servicios integrales de seguridad privada con enfoque preventivo.',
    },
    {
        'title': 'Cobertura operativa 24/7.',
        'excerpt': 'Respuesta coordinada y seguimiento permanente para cada servicio.',
    },
    {
        'title': 'Tecnologia aplicada a la seguridad.',
        'excerpt': 'Monitoreo, videovigilancia y soluciones adaptadas a cada cliente.',
    },
]


INFO_PAGES = {
    'mission': {
        'title': 'Mision y vision',
        'eyebrow': 'Direccion institucional',
        'intro': 'Protegemos lo que mas importa.',
        'lead': 'En BUCAM S.R.L. trabajamos con el firme proposito de brindar servicios integrales de seguridad fisica, electronica y digital, orientados a la proteccion de personas, bienes e instituciones, bajo los mas altos estandares de legalidad, profesionalismo y compromiso etico.',
        'sections': [
            {
                'title': 'Mision',
                'body': 'Nuestra mision es ofrecer soluciones confiables y personalizadas que garanticen tranquilidad, prevencion y resguardo, a traves de un equipo humano capacitado y de la incorporacion constante de tecnologia de vanguardia.',
            },
            {
                'title': 'Vision',
                'body': 'Nuestra vision es consolidarnos como una empresa lider en seguridad privada en la Argentina, reconocida por su capacidad de respuesta, su responsabilidad social y su enfoque preventivo, innovador y humano.',
            },
        ],
    },
    'about': {
        'title': 'Quienes somos',
        'eyebrow': 'Identidad BUCAM',
        'intro': 'Comprometidos con tu seguridad.',
        'lead': 'BUCAM S.R.L. es una empresa legalmente habilitada, con sede en la Provincia de Jujuy y cobertura en todo el territorio nacional. Nos especializamos en brindar servicios de seguridad privada, custodia de personas y bienes, videovigilancia y soluciones tecnologicas, tanto para el sector publico como privado.',
        'sections': [
            {
                'title': 'Compromiso operativo',
                'body': 'Nuestra mision es garantizar la proteccion integral mediante un enfoque profesional, etico y actualizado, que priorice la prevencion, la excelencia operativa y el respeto a los derechos fundamentales.',
            },
            {
                'title': 'Equipo y estructura',
                'body': 'Contamos con un equipo humano calificado, en constante formacion, y una estructura organizativa solida, orientada a la mejora continua y a la construccion de vinculos de confianza con nuestros clientes.',
            },
        ],
    },
    'services': {
        'title': 'Servicios',
        'eyebrow': 'Coberturas disponibles',
        'intro': 'Seguridad integral, adaptada a cada cliente.',
        'lead': 'Brindamos soluciones de seguridad pensadas para distintos entornos operativos, combinando personal capacitado, vigilancia preventiva, monitoreo y asesoramiento especializado.',
        'sections': [
            {
                'title': 'Seguridad fisica y vigilancia',
                'body': 'Personal capacitado para control de accesos, rondas preventivas, patrullajes, vigilancia en eventos y espacios publicos o privados.',
            },
            {
                'title': 'Custodia de bienes y personas',
                'body': 'Custodios especializados en traslados seguros, proteccion ejecutiva y resguardo de cargas o activos sensibles.',
            },
            {
                'title': 'Monitoreo y videovigilancia',
                'body': 'Instalacion de camaras, alarmas, sensores y sistemas de seguridad electronica con monitoreo remoto y soporte tecnico.',
            },
            {
                'title': 'Soluciones en ciberseguridad',
                'body': 'Asesoramiento, implementacion y monitoreo de sistemas de proteccion digital para datos sensibles, redes y plataformas.',
            },
            {
                'title': 'Asesoramiento tecnico y auditoria de riesgos',
                'body': 'Relevamientos de seguridad, diseno de planes preventivos y formacion en normativas vigentes para empresas e instituciones.',
            },
        ],
    },
    'technology': {
        'title': 'Tecnologia',
        'eyebrow': 'Soporte tecnico',
        'intro': 'Innovacion al servicio de la seguridad.',
        'lead': 'En BUCAM integramos tecnologia de ultima generacion para garantizar prevencion, respuesta inmediata y control permanente. Todo nuestro equipamiento esta orientado a preservar la confidencialidad, privacidad y seguridad de nuestros clientes, bajo estrictos estandares tecnicos y legales.',
        'sections': [
            {
                'title': 'Videovigilancia inteligente',
                'body': 'Implementamos camaras de seguridad IP y analogicas para control visual continuo, respaldo de incidentes y supervision de puntos criticos.',
            },
            {
                'title': 'Alarmas y control de accesos',
                'body': 'Integramos alarmas con sensores de movimiento, humo y apertura, junto con sistemas de control de accesos para reforzar la proteccion de areas sensibles.',
            },
            {
                'title': 'Monitoreo y gestion centralizada',
                'body': 'Sumamos monitoreo remoto 24/7, plataformas de gestion de incidentes e infraestructura de conectividad segura para sostener un control permanente y una respuesta coordinada.',
            },
            {
                'title': 'Ciberseguridad adaptable',
                'body': 'Incorporamos servicios de ciberseguridad pensados para proteger datos, redes y plataformas segun las necesidades de cada entorno operativo.',
            },
        ],
    },
}


def get_shared_context(current_page):
    ticker_items = list(
        Post.objects.filter(
            is_published=True,
            published_at__lte=timezone.now(),
        )[:6]
    )
    return {
        'nav_pages': NAV_PAGES,
        'current_page': current_page,
        'brand_banner_url': f"{settings.MEDIA_URL}bucamBanner.png",
        'favicon_url': f"{settings.MEDIA_URL}logobanner.png",
        'ticker_items': ticker_items or TICKER_FALLBACK,
    }


def home(request):
    posts = Post.objects.filter(
        is_published=True,
        published_at__lte=timezone.now(),
    )
    search_query = request.GET.get('q', '').strip()
    if search_query:
        posts = posts.filter(title__icontains=search_query)
    featured_posts = list(posts.filter(is_featured=True)[:5])
    recent_posts = list(posts[:6])
    posts_paginator = Paginator(posts, 6)
    posts_page = posts_paginator.get_page(request.GET.get('page'))

    fallback_services = [
        {
            'eyebrow': 'Cobertura 24/7',
            'title': 'Custodia VIP con protocolos de respuesta inmediata',
            'description': 'Equipos entrenados para traslados, eventos, ejecutivos y proteccion de activos sensibles.',
            'tone': 'primary',
            'banner_image_url': '',
            'published_at': None,
        },
        {
            'eyebrow': 'Unidad especializada',
            'title': 'Custodia femenina con presencia profesional y vision integral',
            'description': 'Perfiles preparados para entornos corporativos, recepciones ejecutivas y acompanamiento estrategico.',
            'tone': 'secondary',
            'banner_image_url': '',
            'published_at': None,
        },
        {
            'eyebrow': 'Monitoreo inteligente',
            'title': 'Videovigilancia e instalacion de tecnologia de control',
            'description': 'Disenamos, instalamos y supervisamos sistemas de CCTV, alarmas y puestos de monitoreo.',
            'tone': 'accent',
            'banner_image_url': '',
            'published_at': None,
        },
    ]

    capabilities = [
        'Guardias habilitados y supervision en terreno',
        'Cobertura para industrias, consorcios y eventos',
        'Monitoreo con protocolos y reportes de incidentes',
        'Tecnologia de acceso, CCTV y control perimetral',
    ]

    metrics = [
        {'value': '24/7', 'label': 'Centro operativo y soporte permanente'},
        {'value': '15+', 'label': 'Anos de experiencia en seguridad privada'},
        {'value': '100%', 'label': 'Planes adaptados a la operacion del cliente'},
    ]

    fallback_recent = [
        {
            'title': 'Proteccion de instalaciones y control de accesos',
            'excerpt': 'Disenamos anillos de seguridad con presencia visible, control documental y protocolos de ingreso.',
            'published_at': None,
        },
        {
            'title': 'Cobertura ejecutiva para traslados y eventos',
            'excerpt': 'Acompanamiento profesional para personas expuestas, comitivas y reuniones de alta sensibilidad.',
            'published_at': None,
        },
        {
            'title': 'Puestos de monitoreo y analisis preventivo',
            'excerpt': 'Integracion de camaras, reportes y alertas para anticipar incidentes y responder con velocidad.',
            'published_at': None,
        },
    ]

    context = {
        'featured_services': featured_posts or fallback_services,
        'capabilities': capabilities,
        'metrics': metrics,
        'recent_highlights': recent_posts or fallback_recent,
        'posts_page': posts_page,
        'search_query': search_query,
    }
    context.update(get_shared_context('home'))
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
    context = {
        'post': post,
        'recent_posts': recent_posts,
    }
    context.update(get_shared_context(''))
    return render(request, 'core/post_detail.html', context)


def info_page(request, page_slug):
    page = INFO_PAGES[page_slug].copy()
    context = {'page': page}
    context.update(get_shared_context(page_slug))
    return render(request, 'core/info_page.html', context)
