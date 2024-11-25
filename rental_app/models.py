from django.db import models
# Create your models here.

class Car(models.Model):
    brand = models.CharField(max_length=100) #marka pojazdu
    model = models.CharField(max_length=100) #model pojazdu
    fuel_type = models.CharField(max_length=50) #rodzaj paliwa
    available = models.BooleanField(default=True)  # Dostępność auta
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.brand} {self.model}"

class Rental(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Rental {self.id} by {self.user.username}"

class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return f"Profile of {self.user.username}"

# class Payment(models.Model):
#     rental = models.OneToOneField(Rental, on_delete=models.CASCADE)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     payment_date = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(
#         max_length=20,
#         choices=[('paid', 'Paid'), ('pending', 'Pending'), ('failed', 'Failed')],
#         default='pending'
#     )
#
#     def __str__(self):
#         return f"Payment for Rental {self.rental.id}: {self.amount} - {self.status}"