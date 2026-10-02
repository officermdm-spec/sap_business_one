from django.contrib import messages
from .forms import VendorForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Vendor


@login_required
def create_vendor(request):    
    if request.method == 'POST':
        form = VendorForm(request.POST)
        if form.is_valid():
            vendor = form.save(commit=False)
            vendor.created_by = request.user
            vendor.save()
            messages.success(request, f'Vendor {vendor.vendor_code} was created successfully.')
            return redirect('create_vendor')
    else:
        form = VendorForm()

    return render(request, 'setup/create_vendor.html', {'form': form})


@login_required
def vendor_list(request):
    search_code = request.GET.get('search_code', '').strip()
    vendors = Vendor.objects.order_by('vendor_code')
    if search_code:
        vendors = vendors.filter(vendor_code__icontains=search_code)

    return render(
        request,
        'setup/vendor_list.html',
        {
            'title': 'Vendor List',
            'module': 'Setup',
            'vendors': vendors,
            'search_code': search_code,
        },
    )
    
@login_required
def vendor_detail(request, pk):
    vendor = get_object_or_404(Vendor, pk=pk)
    return render(
        request,
        'setup/vendor_detail.html',
        {'title': 'Vendor Details', 'module': 'Setup', 'vendor': vendor},
    )
    