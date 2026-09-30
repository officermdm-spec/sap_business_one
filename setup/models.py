from django.db import models


class Vendor(models.Model):
	vendor_code = models.CharField(max_length=20, unique=True, blank=True, editable=False)
	vendor_name = models.CharField(max_length=150)

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		if not self.vendor_code:
			self.vendor_code = f"VEN{self.pk:05d}"
			type(self).objects.filter(pk=self.pk).update(vendor_code=self.vendor_code)

	def __str__(self):
		return f"{self.vendor_code} - {self.vendor_name}"
