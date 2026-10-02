from django.db import models
from django.contrib.auth.models import AbstractUser

# --- Custom User & User Rights Model ---
class User(AbstractUser):
    is_vendor = models.BooleanField(default=False)
    is_client_reader = models.BooleanField(default=False, help_text="Can only view reports if restricted")

    def __str__(self):
        return self.username

class UserModuleRight(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='rights')
    # Setup Rights
    can_view_vendor_entry = models.BooleanField(default=True)
    can_view_vendor_report = models.BooleanField(default=True)
    def __str__(self):
        return f"Rights for {self.user.username}"



