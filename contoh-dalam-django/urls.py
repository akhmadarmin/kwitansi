from django.urls import path
from . import views

urlpatterns = [
    path('nota-pembayaran/', views.kwitansi, name='nota-pembayaran'),
]
