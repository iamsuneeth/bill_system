from django.db import models

# Create your models here.

class Address(models.Model):
    name = models.CharField(max_length=40)
    line1 = models.CharField(max_length=40)
    line2 = models.CharField(max_length=40)
    line3 = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=40)
    pin = models.PositiveIntegerField()

class Product(models.Model):
    product_id = models.CharField(max_length=40)
    name = models.CharField(max_length=80)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    CATEGORY =(
        ('ST','STATIONARY'),
        ('EL','ELECTRONIC'),
        ('F','FOOD')
    )
    category = models.CharField(
            max_length=2,
            choices=CATEGORY
    )
    
class Bill(models.Model):
    invoice_no = models.CharField(max_length=20,unique=True)
    bill_date = models.DateField()
    order_date = models.DateField()
    bill_to = models.OneToOneField(Address,on_delete=models.CASCADE)
    items = models.ManyToManyField(Product, through = 'BillItem')
    total = models.DecimalField(max_digits=7,decimal_places=2)

class BillItem(models.Model):
    bill = models.ForeignKey(Bill,on_delete=models.CASCADE)
    items = models.ForeignKey(Product,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField()
    total = models.DecimalField(max_digits=7, decimal_places=2)

