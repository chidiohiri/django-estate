from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_houses, name='all-houses'),
    path('add-house/', views.add_house, name='add-house'), 
    path('update-house/<int:pk>/', views.update_house, name='update-house'),
    path('delete-house/<int:pk>/', views.delete_house, name='delete-house'),
    path('my-houses/', views.my_houses, name='my-houses'),
    path('house-details/<int:pk>/', views.house_details, name='house-details'),
    path('save-house/<int:pk>/', views.save_house, name='save-house'), 
    path('my-saved-houses/', views.my_saved_houses, name='my-saved-houses'), 
    path('delete-saved-house/<int:pk>/', views.delete_saved_house, name='delete-saved-house'), 
    path('inspections-per-house/<int:pk>/', views.inspections_per_house, name='inspections-per-house'), 
    path('inspect-house/<int:pk>/', views.inspect_house, name='inspect-house'), 
    path('my-house-inspections/', views.my_house_inspections, name='my-house-inspections'), 
    path('delete-house-inspections/<int:pk>/', views.delete_house_inspection, name='delete-house-inspections')
]
