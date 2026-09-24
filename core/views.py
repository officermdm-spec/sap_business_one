from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from .models import UserModuleRight

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Assign default module rights
            UserModuleRight.objects.create(user=user)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def home_view(request):
    return render(request, 'core/home.html')

# Dummy Module Views
@login_required
def vendor_entry(request):
    return render(request, 'core/dummy_page.html', {'title': 'Vendor Entry', 'module': 'Setup'})

@login_required
def vendor_report(request):
    return render(request, 'core/dummy_page.html', {'title': 'Vendor Entry Report', 'module': 'Setup'})

@login_required
def mpr_entry(request):
    return render(request, 'core/dummy_page.html', {'title': 'MPR Entry', 'module': 'Purchase'})

@login_required
def mpr_report(request):
    return render(request, 'core/dummy_page.html', {'title': 'MPR Reports', 'module': 'Purchase'})

@login_required
def po_entry(request):
    return render(request, 'core/dummy_page.html', {'title': 'PO Entry', 'module': 'Purchase'})

@login_required
def po_report(request):
    return render(request, 'core/dummy_page.html', {'title': 'PO Reports', 'module': 'Purchase'})