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
    # Purchase Rights
    can_view_mpr_entry = models.BooleanField(default=True)
    can_view_mpr_report = models.BooleanField(default=True)
    can_view_po_entry = models.BooleanField(default=True)
    can_view_po_report = models.BooleanField(default=True)

    def __str__(self):
        return f"Rights for {self.user.username}"


# --- Vendor Entry Model ---
class Vendor(models.Model):
    company_name = models.CharField(max_length=200)
    contact_person = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name


# --- Purchase Module Models ---
class MPR(models.Model): # Material Purchase Requisition
    mpr_number = models.CharField(max_length=50, unique=True)
    requested_by = models.ForeignKey(User, on_delete=models.CASCADE)
    item_details = models.TextField()
    status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"MPR: {self.mpr_number}"

class PurchaseOrder(models.Model): # PO Entry
    po_number = models.CharField(max_length=50, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    mpr = models.ForeignKey(MPR, on_delete=models.SET_NULL, null=True, blank=True)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"PO: {self.po_number}"