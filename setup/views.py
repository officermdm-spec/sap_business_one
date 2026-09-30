from django.contrib import messages
from .forms import VendorForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Vendor


def create_vendor(request):
    if request.method == 'POST':
        form = VendorForm(request.POST)
        if form.is_valid():
            vendor = form.save()
            messages.success(request, f'Vendor {vendor.vendor_code} was created successfully.')
            return redirect('create_vendor')
    else:
        form = VendorForm()

    return render(request, 'setup/create_vendor.html', {'form': form})


@login_required
def vendor_list(request):
    vendors = Vendor.objects.order_by('vendor_code')
    return render(
        request,
        'setup/vendor_list.html',
        {'title': 'Vendor List', 'module': 'Setup', 'vendors': vendors},
    )