from functools import wraps
from django.shortcuts import redirect
from django.contrib import messages

# Check if session user is tenant, if not redirect to dashboard with error message
def tenant_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        user = request.user
        if user.is_authenticated and user.is_tenant:
            return view_func(request, *args, **kwargs)
        else:
            messages.warning(request, "You must be a Tenant to access this page.")
            return redirect('dashboard') 
    return _wrapped_view

# Check if session user is landlord, if not redirect to dashboard with error message
def landlord_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        user = request.user
        if user.is_authenticated and user.is_landlord:
            return view_func(request, *args, **kwargs)
        else:
            messages.warning(request, "You must be a Landlord to access this page.")
            return redirect('dashboard') 
    return _wrapped_view