from django.urls import path

from .views import home, post_detail

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('entradas/<slug:slug>/', post_detail, name='post_detail'),
]
