from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Post


NAV_PAGES = [
    {'slug': 'home', 'title': 'Inicio', 'url_name': 'core:home'},
    {'slug': 'mission', 'title': 'Mision y vision', 'url_name': 'core:mission'},
    {'slug': 'about', 'title': 'Quienes somos', 'url_name': 'core:about'},
    {'slug': 'services', 'title': 'Servicios', 'url_name': 'core:services'},
    {'slug': 'technology', 'title': 'Tecnologia', 'url_name': 'core:technology'},
]


INFO_PAGES = {
    'mission': {
        'title': 'Mision y vision',
        'eyebrow': 'Direccion institucional',
        'intro': 'Trabajamos para ofrecer cobertura profesional, presencia operativa y procesos claros que den confianza desde el primer contacto.',
        'lead': 'Nuestra mision es prevenir riesgos y responder con rapidez. Nuestra vision es consolidar una empresa de seguridad privada confiable, moderna y adaptable a cada operacion.',
        'sections': [
            {
                'title': 'Mision',
                'body': 'Brindar servicios de seguridad privada con personal capacitado, seguimiento continuo y protocolos concretos para personas, instalaciones y operaciones sensibles.',
            },
            {
                'title': 'Vision',
                'body': 'Ser una referencia regional en proteccion integral, combinando factor humano, supervision cercana y tecnologia para anticipar incidentes y mejorar resultados.',
            },
            {
                'title': 'Compromisos',
                'body': 'Priorizamos la prevencion, la comunicacion con el cliente, la presencia profesional y la mejora operativa constante en cada servicio contratado.',
            },
        ],
    },
    'about': {
        'title': 'Quienes somos',
        'eyebrow': 'Identidad BUCAM',
        'intro': 'BUCAM S.R.L. desarrolla soluciones de seguridad privada con enfoque operativo, atencion personalizada y una presentacion institucional sobria.',
        'lead': 'Somos un equipo orientado a la prevencion, el control de accesos, la custodia especializada y la coordinacion de coberturas segun el nivel de riesgo de cada cliente.',
        'sections': [
            {
                'title': 'Perfil de la empresa',
                'body': 'Acompanamos organizaciones, consorcios, eventos y operaciones ejecutivas con planes de cobertura claros, recursos asignados y seguimiento profesional.',
            },
            {
                'title': 'Forma de trabajo',
                'body': 'Analizamos contexto, definimos puntos criticos, asignamos personal y establecemos protocolos de comunicacion para sostener una respuesta ordenada.',
            },
            {
                'title': 'Valor diferencial',
                'body': 'Combinamos trato directo, capacidad de adaptacion y foco en la imagen del servicio para representar correctamente a cada cliente en terreno.',
            },
        ],
    },
    'services': {
        'title': 'Servicios',
        'eyebrow': 'Coberturas disponibles',
        'intro': 'Armamos propuestas a medida para vigilancia, custodia y monitoreo con presencia profesional y protocolos de accion.',
        'lead': 'Cada servicio puede adaptarse al tipo de instalacion, cantidad de accesos, exposicion publica, horarios criticos y necesidades de reporte.',
        'sections': [
            {
                'title': 'Vigilancia fisica',
                'body': 'Cobertura fija para ingresos, recorridas, control perimetral y supervision de movimientos en plantas, edificios, comercios y predios.',
            },
            {
                'title': 'Custodia especializada',
                'body': 'Proteccion para ejecutivos, traslados, eventos y activos sensibles con evaluacion previa y coordinacion operativa.',
            },
            {
                'title': 'Control y recepcion',
                'body': 'Puestos de acceso, control documental, acreditaciones, asistencia en recepciones y protocolos de ingreso y egreso.',
            },
        ],
    },
    'technology': {
        'title': 'Tecnologia',
        'eyebrow': 'Soporte tecnico',
        'intro': 'La tecnologia complementa el trabajo en terreno con herramientas de monitoreo, registro y respuesta temprana.',
        'lead': 'Integramos recursos que ayudan a detectar desvios, documentar incidentes y sostener una supervision continua segun el tipo de cobertura.',
        'sections': [
            {
                'title': 'Videovigilancia',
                'body': 'Instalacion y seguimiento de camaras para puntos de acceso, perimetros, sectores criticos y respaldo visual de incidentes.',
            },
            {
                'title': 'Control de accesos',
                'body': 'Soluciones para administrar ingresos, registrar movimientos y reforzar protocolos en areas sensibles o de circulacion restringida.',
            },
            {
                'title': 'Monitoreo y reportes',
                'body': 'Esquemas de observacion, alertas y consolidacion de novedades para mejorar tiempos de respuesta y trazabilidad operativa.',
            },
        ],
    },
}


def get_shared_context(current_page):
    return {
        'nav_pages': NAV_PAGES,
        'current_page': current_page,
    }


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
            'description': 'Equipos entrenados para traslados, eventos, ejecutivos y proteccion de activos sensibles.',
            'tone': 'primary',
            'image_url': '',
            'published_at': None,
        },
        {
            'eyebrow': 'Unidad especializada',
            'title': 'Custodia femenina con presencia profesional y vision integral',
            'description': 'Perfiles preparados para entornos corporativos, recepciones ejecutivas y acompanamiento estrategico.',
            'tone': 'secondary',
            'image_url': '',
            'published_at': None,
        },
        {
            'eyebrow': 'Monitoreo inteligente',
            'title': 'Videovigilancia e instalacion de tecnologia de control',
            'description': 'Disenamos, instalamos y supervisamos sistemas de CCTV, alarmas y puestos de monitoreo.',
            'tone': 'accent',
            'image_url': '',
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
    context.update(get_shared_context('services'))
    return render(request, 'core/post_detail.html', context)


def info_page(request, page_slug):
    page = INFO_PAGES[page_slug].copy()
    context = {'page': page}
    context.update(get_shared_context(page_slug))
    return render(request, 'core/info_page.html', context)
