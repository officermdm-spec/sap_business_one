from django.contrib import admin

from .models import Vendor


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
	list_display = ("vendor_code", "vendor_name")
	search_fields = ("vendor_code", "vendor_name")
