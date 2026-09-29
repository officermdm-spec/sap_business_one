from django.shortcuts import render

# Create your views here.

def vendor_entry(request):
    return render(request, 'setup/create_vendor.html')