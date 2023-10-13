from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    reg_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Username: {self.name}, email: {self.email},  phone: {self.phone}, address: {self.address}'

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    add_date = models.DateField(auto_now_add=True)
    product_img = models.ImageField(upload_to='image', blank=True, null=True)

    def __str__(self):
        return f'Product name: {self.name}, price: {self.price},  description: {self.description}, quantity: {self.quantity}'


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    date_ordered = models.DateField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'Customer: {self.customer.name}, products: {self.products},  date_ordered: {self.date_ordered}, total_price: {self.total_price}'
