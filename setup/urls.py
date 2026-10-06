from django.urls import path
from . import views

urlpatterns = [
    path('create_vendor/', views.create_vendor, name='create_vendor'),
    path('vendor_list/', views.vendor_list, name='vendor_list'),
    path('vendor/<int:pk>/', views.vendor_detail, name='vendor_detail'),
    path('create_country/', views.create_country, name='create_country')
]