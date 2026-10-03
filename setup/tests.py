from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Vendor


class VendorEntryTests(TestCase):
	def setUp(self):
		self.user = get_user_model().objects.create_user(username="vendor-user", password="test-pass")
		self.client.force_login(self.user)

	def test_post_creates_vendor_with_generated_code(self):
		response = self.client.post(
			reverse("create_vendor"),
			{"vendor_name": "Northwind Supplies"},
			follow=True,
		)

		vendor = Vendor.objects.get(vendor_name="Northwind Supplies")
		self.assertEqual(vendor.vendor_code, f"VEN{vendor.pk:05d}")
		self.assertContains(response, vendor.vendor_code)

	def test_find_loads_vendor_and_shows_its_view_link(self):
		vendor = Vendor.objects.create(vendor_name="Northwind Supplies", created_by=self.user)

		response = self.client.post(
			reverse("create_vendor"),
			{"action": "find", "vendor_code": vendor.vendor_code.lower()},
		)

		self.assertEqual(response.context["found_vendor"], vendor)
		self.assertEqual(response.context["form"]["vendor_name"].value(), vendor.vendor_name)
		self.assertContains(response, reverse("vendor_detail", args=[vendor.pk]))

	def test_update_saves_changes_to_the_found_vendor(self):
		vendor = Vendor.objects.create(vendor_name="Northwind Supplies", created_by=self.user)

		response = self.client.post(
			reverse("create_vendor"),
			{
				"action": "update",
				"vendor_id": vendor.pk,
				"vendor_code": vendor.vendor_code,
				"vendor_name": "Northwind Trading",
			},
			follow=True,
		)

		vendor.refresh_from_db()
		self.assertEqual(vendor.vendor_name, "Northwind Trading")
		self.assertEqual(Vendor.objects.count(), 1)
		self.assertContains(response, "updated successfully")

	def test_delete_removes_only_the_found_vendor(self):
		vendor = Vendor.objects.create(vendor_name="Northwind Supplies", created_by=self.user)
		other_vendor = Vendor.objects.create(vendor_name="Contoso Parts", created_by=self.user)

		response = self.client.post(
			reverse("create_vendor"),
			{"action": "delete", "vendor_id": vendor.pk, "vendor_code": vendor.vendor_code},
			follow=True,
		)

		self.assertFalse(Vendor.objects.filter(pk=vendor.pk).exists())
		self.assertTrue(Vendor.objects.filter(pk=other_vendor.pk).exists())
		self.assertContains(response, "deleted successfully")
