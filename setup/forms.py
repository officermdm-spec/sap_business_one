from django import forms

from .models import Vendor


class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ["vendor_name", "company_name", "company_email", "phone_number", "company_address"]
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
        }