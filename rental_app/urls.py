# rental_app/urls.py
from django.urls import path
from . import views

app_name = 'rental_app'

urlpatterns = [
    # path('', views.home, name='home'),  # Widok powitalny
    # path('cars/', views.available_cars, name='available_cars'),  # Lista dostępnych samochodów
    # path('rent/<int:car_id>/', views.rent_car, name='rent_car'),  # Rezerwacja samochodu
    # path('rental_history/', views.rental_history, name='rental_history'),  # Historia wynajmów
    path('', views.CarListView.as_view(), name='all'),
    path('cars/create/', views.CarCreateView.as_view(), name='car_create'),
    path('cars/<int:pk>/update/', views.CarUpdateView.as_view(), name='car_update'),
    path('cars/<int:pk>/delete/', views.CarDeleteView.as_view(), name='car_delete'),

]
