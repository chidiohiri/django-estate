import django_filters
from .models import House, HouseInspection, SaveHouse

class HouseFilters(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = House 
        fields = ['title', 'city', 'state', 'rent_cycle']

class SavedHouseFilter(django_filters.FilterSet):
    house__title = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = SaveHouse 
        fields = ['house__title', 'house__city', 'house__state']

class HouseInspectionFilter(django_filters.FilterSet):
    house__title = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = HouseInspection
        fields = ['house__title', 'phone', 'inspection_date']