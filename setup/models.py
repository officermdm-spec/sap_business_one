from django.db import models
from django.conf import settings

class Vendor(models.Model):
	vendor_code = models.CharField(max_length=20, unique=True, blank=True, editable=False)
	vendor_name = models.CharField(max_length=150)
	company_name = models.CharField(max_length=150, blank=True, null=True)
	company_email = models.EmailField(blank=True, null=True)
	phone_number = models.CharField(max_length=20, blank=True, null=True)
	bank_name = models.CharField(max_length=100, blank=True, null=True)
	bank_account_number = models.CharField(max_length=50, blank=True, null=True)
	company_address = models.TextField(blank=True, null=True)
	is_active = models.BooleanField(default=True)
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


class Country(models.Model):
    country_code = models.CharField(max_length=10,unique=True,blank=True)
    country_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.country_name} ({self.country_code})"

    def save(self, *args, **kwargs):
        if not self.country_code:
            super().save(*args, **kwargs)

            self.country_code = f"CTR{self.pk:05d}"

            type(self).objects.filter(
                pk=self.pk
            ).update(
                country_code=self.country_code
            )
        else:
            super().save(*args, **kwargs)

