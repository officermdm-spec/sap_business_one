from django import forms

from .models import Vendor,Country


class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ["vendor_name", "company_name", "company_email", "phone_number", "bank_name", "bank_account_number", "company_address", "is_active"]
        widgets = {
            "vendor_name": forms.TextInput(
                attrs={
                    "autocomplete": "organization",
                    "class": "block w-full rounded-md border border-slate-300 px-3 py-2.5 text-sm text-slate-900 outline-none transition placeholder:text-slate-400 focus:border-teal-600 focus:ring-2 focus:ring-teal-600/20",
                    "placeholder": "Enter vendor name",
                }
            ),
            "company_name": forms.TextInput(
                attrs={
                    "autocomplete": "organization",
                    "class": "block w-full rounded-md border border-slate-300 px-3 py-2.5 text-sm text-slate-900 outline-none transition placeholder:text-slate-400 focus:border-teal-600 focus:ring-2 focus:ring-teal-600/20",
                    "placeholder": "Enter company name",
                }
            ),
            "company_email": forms.EmailInput(
                attrs={
                    "autocomplete": "email",
                    "class": "block w-full rounded-md border border-slate-300 px-3 py-2.5 text-sm text-slate-900 outline-none transition placeholder:text-slate-400 focus:border-teal-600 focus:ring-2 focus:ring-teal-600/20",
                    "placeholder": "Enter company email",
                }
            ),
            "bank_name": forms.TextInput(
                attrs={
                    "class": "block w-full rounded-md border border-slate-300 px-3 py-2.5 text-sm text-slate-900 outline-none transition placeholder:text-slate-400 focus:border-teal-600 focus:ring-2 focus:ring-teal-600/20",
                    "placeholder": "Enter bank name",
                }
            ),
            "bank_account_number": forms.TextInput(
                attrs={
                    "class": "block w-full rounded-md border border-slate-300 px-3 py-2.5 text-sm text-slate-900 outline-none transition placeholder:text-slate-400 focus:border-teal-600 focus:ring-2 focus:ring-teal-600/20",
                    "placeholder": "Enter bank account number",
                }
            ),
            "company_address": forms.Textarea(
                attrs={
                    "class": "block w-full rounded-md border border-slate-300 px-3 py-2.5 text-sm text-slate-900 outline-none transition placeholder:text-slate-400 focus:border-teal-600 focus:ring-2 focus:ring-teal-600/20",
                    "placeholder": "Enter company address",
                    "rows": 3,
                }
            ),
            "phone_number": forms.TextInput(
                attrs={
                    "autocomplete": "tel",
                    "class": "block w-full rounded-md border border-slate-300 px-3 py-2.5 text-sm text-slate-900 outline-none transition placeholder:text-slate-400 focus:border-teal-600 focus:ring-2 focus:ring-teal-600/20",
                    "placeholder": "Enter phone number",
                }
            ),
            "is_active": forms.CheckboxInput(
                attrs={
                    "class": "h-4 w-4 rounded border-slate-300 text-teal-600 focus:ring-teal-600",
                }
            ),
        }
        
        # Create Country form
class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['country_code', 'country_name', 'is_active']
        widgets = {
            'country_code': forms.TextInput(attrs={
                'class': 'w-full rounded-md border border-slate-300 px-3 py-2 text-slate-800 focus:border-teal-600 focus:outline-none focus:ring-1 focus:ring-teal-600',
                'placeholder': 'Enter country code'
            }),
            'country_name': forms.TextInput(attrs={
                'class': 'w-full rounded-md border border-slate-300 px-3 py-2 text-slate-800 focus:border-teal-600 focus:outline-none focus:ring-1 focus:ring-teal-600',
                'placeholder': 'Enter country name'
            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'h-4 w-4 rounded border-slate-300 text-teal-700 focus:ring-teal-600'
            }),
        }