from django.db import models

# Create your models here.
class Product(models.Model):
    description = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    uom = models.CharField(max_length=200)
    price = models.FloatField()

    def __str__(self):
        return self.description
    
class Customer(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class GrossSales(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField()
    gross_sales = models.FloatField()
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.description + ' ' + self.customer.name + ' ' + str(self.date) + ' ' + str(self.gross_sales)