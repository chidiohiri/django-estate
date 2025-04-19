from django import forms 
from .models import House, HouseInspection

class AddHouseForm(forms.ModelForm):
    class Meta:
        model = House 
        exclude = ('created_on', 'created_by', 'is_verified')

class UpdateHouseForm(forms.ModelForm):
    class Meta:
        model = House 
        exclude = ('created_on', 'created_by', 'is_verified', 'coo')

class HouseInspectionForm(forms.ModelForm):
    class Meta:
        model = HouseInspection
        exclude = ('user', 'house', 'created_on')