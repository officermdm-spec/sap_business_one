from django.test import TestCase
from django.urls import reverse

from .models import Vendor


class VendorEntryTests(TestCase):
	def test_post_creates_vendor_with_generated_code(self):
		response = self.client.post(
			reverse("create_vendor"),
			{"vendor_name": "Northwind Supplies"},
			follow=True,
		)

		vendor = Vendor.objects.get(vendor_name="Northwind Supplies")
		self.assertEqual(vendor.vendor_code, f"VEN{vendor.pk:05d}")
		self.assertContains(response, vendor.vendor_code)
