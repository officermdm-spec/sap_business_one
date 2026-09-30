from django import forms

from .models import Vendor


class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ["vendor_name", "company_name"]
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
        }