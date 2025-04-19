from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model
from .models import House, HouseInspection, SaveHouse
from . import form as fm 
from .filters import HouseFilters, SavedHouseFilter, HouseInspectionFilter
from core.decorator import tenant_required, landlord_required

User = get_user_model()  # Reference to the custom or default User model

# View for adding a new house listing
@login_required
@landlord_required
def add_house(request):
    if request.method == 'POST':
        form = fm.AddHouseForm(request.POST, request.FILES)  # Handle form submission
        if form.is_valid():
            var = form.save(commit=False)
            var.created_by = request.user  # Attach current user as owner
            var.save()
            messages.success(request, 'House information created and saved to the Database')
            return redirect('add-house')
        else:
            messages.warning(request, 'Something went wrong. Please check form input')
            return redirect('add-house')
    else:
        form = fm.AddHouseForm()  # Render empty form for GET request
        context = {'form': form}
    return render(request, 'house/add_house.html', context)

# View for updating existing house listing
@login_required
@landlord_required
def update_house(request, pk):
    house = get_object_or_404(House, pk=pk)  # Retrieve the house or return 404

    if house.created_by != request.user:
        messages.warning(request, 'You do not have permissions to perform this action')
        return redirect('dashboard')

    if request.method == 'POST':
        form = fm.UpdateHouseForm(request.POST, instance=house)
        if form.is_valid():
            form.save()
            messages.success(request, 'House information changed and updated in database')
            return redirect('house-details', house.pk)
        else:
            messages.warning(request, 'Something went wrong. Please check form inputs')
            return redirect('update-house', house.pk)
    else:
        form = fm.UpdateHouseForm(instance=house)  # Pre-fill form with house data
        context = {'form': form}
    return render(request, 'house/update_house.html', context)

# View for deleting a house (only by owner)
@login_required
@landlord_required
def delete_house(request, pk):
    house = get_object_or_404(House, pk=pk)

    if house.created_by != request.user:
        messages.warning(request, 'You do not have permissions to perform this action')
        return redirect('dashboard')

    if house.created_by != request.user:
        messages.warning(request, 'You do not have permissions to delete this house')
        return redirect('dashboard')

    house.delete()
    messages.success(request, 'House information has been deleted from the database')
    return redirect('my-houses')

# View to list houses created by current user
@login_required
@landlord_required
def my_houses(request):
    houses = House.objects.filter(created_by=request.user)

    # Apply Filter
    houses_filter = HouseFilters(request.GET, queryset=houses)
    filtered_houses = houses_filter.qs

    # Pagination
    paginator = Paginator(filtered_houses, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'houses': page_obj, 'filter':houses_filter}
    return render(request, 'house/my_houses.html', context)

# Public view to show all verified houses
def all_houses(request):
    houses = House.objects.filter(is_verified=True)

    # Apply Filter
    houses_filter = HouseFilters(request.GET, queryset=houses)
    filtered_houses = houses_filter.qs

    # pagination
    paginator = Paginator(filtered_houses, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'houses': page_obj, 'filter':houses_filter}

    return render(request, 'house/all_houses.html', context)

# View to show the details of a single house
def house_details(request, pk):
    house = get_object_or_404(House, pk=pk)
    context = {'house': house}
    return render(request, 'house/house_details.html', context)

# View to allow a user to save a house to their profile
@login_required
@tenant_required
def save_house(request, pk):
    house = get_object_or_404(House, pk=pk)

    if SaveHouse.objects.filter(house=house, user=request.user).exists():
        messages.warning(request, 'You have already saved this house')
        return redirect('house-details', house.pk)

    SaveHouse.objects.create(house=house, user=request.user)
    messages.success(request, 'You just saved this house information to your profile')
    return redirect('house-details', house.pk)

# View to display saved houses of the current user
@login_required
@tenant_required
def my_saved_houses(request):
    saved_houses = SaveHouse.objects.filter(user=request.user)

    # Apply Filter
    houses_filter = SavedHouseFilter(request.GET, queryset=saved_houses)
    filtered_houses = houses_filter.qs

    # Pagination
    paginator = Paginator(filtered_houses, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'saved_houses': page_obj, 'filter': houses_filter}
    return render(request, 'house/saved_houses.html', context)

# View to delete a saved house (only by the user who saved it)
@login_required
@tenant_required
def delete_saved_house(request, pk):
    saved_house = get_object_or_404(SaveHouse, pk=pk)

    if saved_house.user != request.user:
        messages.warning(request, 'You do not have permissions to perform this action')
        return redirect('dashboard')

    if saved_house.user != request.user:
        messages.warning(request, 'You cannot delete this data')
        return redirect('my-saved-houses')
    
    saved_house.delete() 
    messages.success(request, 'Saved house has been removed from your list')
    return redirect('my-saved-houses')

# View to list inspections for a specific house
@login_required
@landlord_required
def inspections_per_house(request, pk):
    house = get_object_or_404(House, pk=pk)
    inspections = house.houseinspection_set.all().order_by('-inspection_date')  # Reverse relation to HouseInspection

    # Apply Filter
    inspections_filter = HouseInspectionFilter(request.GET, queryset=inspections)
    filtered_inspections = inspections_filter.qs

    # Pagination
    paginator = Paginator(filtered_inspections, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {'house': house, 'inspections': page_obj, 'filter':inspections_filter}
    return render(request, 'house/inspections_per_house.html', context)

# View to schedule an inspection for a house
@login_required
@tenant_required
def inspect_house(request, pk):
    house = get_object_or_404(House, pk=pk)
    check_inspection = HouseInspection.objects.filter(house=house, user=request.user)

    if check_inspection.exists():
        messages.warning(request, 'You have already scheduled an inspection for this house')
        return redirect('house-details', house.pk)

    if request.method == 'POST':
        form = fm.HouseInspectionForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.house = house
            var.user = request.user
            var.save()
            messages.success(request, 'House inspection has been scheduled')
            return redirect('dashboard') 
        else:
            messages.warning(request, 'Something went wrong. Please check form inputs')
            return redirect('inspect-house', house.pk)
    else:
        form = fm.HouseInspectionForm()
        context = {'form': form, 'house': house}
    return render(request, 'house/inspect_house.html', context)

# View to list all inspections scheduled by current user
@login_required
@tenant_required
def my_house_inspections(request):
    inspections = HouseInspection.objects.filter(user=request.user).order_by('-inspection_date')

    # Apply Filter
    inspections_filter = HouseInspectionFilter(request.GET, queryset=inspections)
    filtered_inspections = inspections_filter.qs

    # Pagination
    paginator = Paginator(filtered_inspections, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'inspections': page_obj, 'filter':inspections_filter}
    return render(request, 'house/my_house_inspections.html', context)

# View to delete a user's scheduled inspection
@login_required
@login_required
def delete_house_inspection(request, pk):
    inspection = get_object_or_404(HouseInspection, pk=pk)

    if inspection.user != request.user:
        messages.warning(request, 'You do not have permissions to perform this action')
        return redirect('dashboard')
    
    if inspection.user != request.user:
        messages.warning(request, 'You cannot delete this data')
        return redirect('my-house-inspections')
    
    inspection.delete()
    messages.success(request, 'House inspection schedule is deleted')
    return redirect('my-house-inspections')
