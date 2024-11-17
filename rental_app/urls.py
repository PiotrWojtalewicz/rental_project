# rental_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Widok powitalny
    path('cars/', views.available_cars, name='available_cars'),  # Lista dostępnych samochodów
    path('rent/<int:car_id>/', views.rent_car, name='rent_car'),  # Rezerwacja samochodu
    path('rental_history/', views.rental_history, name='rental_history'),  # Historia wynajmów
]
