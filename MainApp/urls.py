from django.urls import path 
from . import views
from django.contrib.auth.views import LogoutView 

from INV.views import (invoice_management, invoice_cetak)

app_name = 'MainApp' 

urlpatterns = [
    # MainApp
    path('login/', views.login_view, name='login'),
    path('', views.home, name='home'), 
    path('logout/',LogoutView.as_view(next_page='MainApp:login'), name="logout"),
    path('klien/', views.klien_management, name='klien'),
    path('klien/add/', views.klien_management, name='klien_add', kwargs={'tipe_req': 'add'}),
    path('klien/<int:pk>/', views.klien_management, name='klien_update', kwargs={'tipe_req': 'update'}),
    path('kwitansi/<int:pk_src>/', views.kwitansi_cetak, name='kwitansi'),

    # INV
    path('invoice/', invoice_management, name='invoice'),
    path('invoice/add/', invoice_management, name='invoice_add', kwargs={'tipe_req': 'add'}),
    path('invoice/<int:pk>/', invoice_management, name='invoice_update', kwargs={'tipe_req': 'update'}),
    path('invoice/<int:pk>/cetak', invoice_cetak, name='invoice_cetak'),
]