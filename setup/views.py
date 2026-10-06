from django.contrib import messages
from .forms import CountryForm, VendorForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Vendor


@login_required
def create_vendor(request):
    lookup_code = ''
    found_vendor = None
    form = VendorForm()

    if request.method == 'POST':
        action = request.POST.get('action', 'save')
        lookup_code = request.POST.get('vendor_code', '').strip()

        if action == 'find':
            found_vendor = Vendor.objects.filter(vendor_code__iexact=lookup_code).first()
            if found_vendor:
                form = VendorForm(instance=found_vendor)
            else:
                messages.error(request, f'No vendor found with code {lookup_code or "(empty)"}.')
        elif action in ('update', 'delete'):
            vendor_id = request.POST.get('vendor_id')
            if not vendor_id:
                messages.error(request, 'Find a vendor before updating or deleting it.')
            else:
                found_vendor = get_object_or_404(Vendor, pk=vendor_id)
                if action == 'delete':
                    code = found_vendor.vendor_code
                    found_vendor.delete()
                    messages.success(request, f'Vendor {code} was deleted successfully.')
                    return redirect('create_vendor')

                form = VendorForm(request.POST, instance=found_vendor)
                if form.is_valid():
                    vendor = form.save(commit=False)
                    vendor.updated_by = request.user
                    vendor.save()
                    messages.success(request, f'Vendor {vendor.vendor_code} was updated successfully.')
                    return redirect('create_vendor')
                lookup_code = found_vendor.vendor_code
        else:
            form = VendorForm(request.POST)
            if form.is_valid():
                vendor = form.save(commit=False)
                vendor.created_by = request.user
                vendor.save()
                messages.success(request, f'Vendor {vendor.vendor_code} was created successfully.')
                return redirect('create_vendor')

    return render(
        request,
        'setup/create_vendor.html',
        {'form': form, 'lookup_code': lookup_code, 'found_vendor': found_vendor},
    )


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
    
# Create Country 
@login_required
def create_country(request):
    form = CountryForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('create_country')

    return render(
        request,
        'setup/create_country.html',
        {'form': form},
        )