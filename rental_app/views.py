# rental_app/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy

from .models import Car, Rental
from .forms import RentalForm  # Używamy formularza, który stworzyliśmy wcześniej
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# # Widok powitalny na stronie głównej
# def home(request):
#     # Pobieramy wszystkie dostępne samochody
#     cars = Car.objects.all()
#
#     # Sprawdzamy, czy użytkownik wysłał jakieś filtry
#     marka = request.GET.get('marka')
#     if marka:
#         cars = cars.filter(brand__icontains=marka)  # Filtrujemy po marce (case-insensitive)
#
#     # Renderujemy stronę z listą samochodów i napisem powitalnym
#     return render(request, 'cars/available_cars.html', {'cars': cars})
#
# # Widok dostępnych samochodów
# def available_cars(request):
#     cars = Car.objects.all()  # Pobieramy wszystkie samochody
#     marka = request.GET.get('marka')  # Sprawdzamy, czy użytkownik podał filtr
#     if marka:
#         cars = cars.filter(brand__icontains=marka)  # Filtrujemy po marce, jeśli jest wpisana
#     return render(request, 'cars/available_cars.html', {'cars': cars})  # Przekazujemy listę samochodów do szablonu
#
# #Widok rezerwacji samochodu
# def rent_car(request, car_id):
#     car = Car.objects.get(id=car_id)  # Pobieramy samochód na podstawie jego ID
#     if request.method == 'POST':
#         form = RentalForm(request.POST)  # Jeśli formularz jest przesyłany
#         if form.is_valid():
#             rental = form.save(commit=False)  # Tworzymy obiekt rezerwacji, ale nie zapisujemy go jeszcze w bazie
#             rental.car = car  # Przypisujemy wybrany samochód do rezerwacji
#             rental.user = request.user  # Przypisujemy aktualnie zalogowanego użytkownika
#             rental.save()  # Zapisujemy rezerwację w bazie danych
#             return redirect('rental_history')  # Przekierowujemy użytkownika do historii wynajmów
#     else:
#         form = RentalForm()  # Jeśli formularz nie jest przesyłany, tworzymy pusty formularz
#     return render(request, 'cars/rent_car.html', {'form': form, 'car': car})  # Wyświetlamy formularz rezerwacji samochodu
#
# # Widok historii wynajmów
# def rental_history(request):
#     rentals = Rental.objects.filter(user=request.user)  # Pobieramy wszystkie wynajmy danego użytkownika
#     return render(request, 'cars/rental_history.html', {'rentals': rentals})  # Wyświetlamy historię wynajmów w szablonie


class CarBaseView(View):
    model = Car
    fields = '__all__'
    success_url = reverse_lazy('cars:all')

class CarListView(CarBaseView, ListView):
    """View to list all cars.
    Use the 'car_list' variable in the template
    to access all Car objects"""

class StudentDetailView(CarBaseView, DetailView):
    """View to list the details from one Car.
    Use the 'Car' variable in the template to access
    the specific Car here and in the Views below"""

class CarCreateView(CarBaseView, CreateView):
    """View to create a new car"""

class CarUpdateView(CarBaseView, UpdateView):
    """View to update a car"""

class CarDeleteView(CarBaseView, DeleteView):
    """View to delete a car"""