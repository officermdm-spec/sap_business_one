from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('signup/', views.signup_view, name='signup'),
    
    # Setup Module
    path('setup/vendor-entry/', views.vendor_entry, name='vendor_entry'),
    path('setup/vendor-report/', views.vendor_report, name='vendor_report'),
    
    # Purchase Module
    path('purchase/mpr-entry/', views.mpr_entry, name='mpr_entry'),
    path('purchase/mpr-report/', views.mpr_report, name='mpr_report'),
    path('purchase/po-entry/', views.po_entry, name='po_entry'),
    path('purchase/po-report/', views.po_report, name='po_report'),
]