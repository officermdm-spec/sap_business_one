from django.db import models
from django.conf import settings

class Vendor(models.Model):
	vendor_code = models.CharField(max_length=20, unique=True, blank=True, editable=False)
	vendor_name = models.CharField(max_length=150)
	company_name = models.CharField(max_length=150, blank=True, null=True)
	phone_number = models.CharField(max_length=20, )
	created_at = models.DateTimeField(auto_now_add=True)
	created_by = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.PROTECT,
		related_name="vendors_created",
	)
	updated_at = models.DateTimeField(auto_now=True)
	updated_by = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.PROTECT,
		related_name="vendors_updated",
		default=None,
		null=True,
	)

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		if not self.vendor_code:
			self.vendor_code = f"VEN{self.pk:05d}"
			type(self).objects.filter(pk=self.pk).update(vendor_code=self.vendor_code)

	def __str__(self):
		return f"{self.vendor_code} - {self.vendor_name}"
