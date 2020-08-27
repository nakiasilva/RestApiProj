from django.db import models

# Create your models here.
class Products(models.Model):
    id = models.CharField(unique=True, primary_key=True, max_length=36, blank=False)
    name = models.CharField(max_length=17, null=False, blank=False)
    description = models.CharField(max_length=35, null=False, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, null= False,blank=False)
    deliveryPrice = models.DecimalField(max_digits=4, decimal_places=2, null= False, blank=False)

    class Meta:
        managed = True
        db_table = 'Products'


class ProductOptions(models.Model):
    id = models.CharField(unique=True, primary_key=True, max_length=36, blank=False)
    productId = models.CharField(max_length=36, blank=False)
    name = models.CharField(max_length=9, null=False, blank=True)
    description = models.CharField(max_length=23, null=False, blank=True)

    class Meta:
        managed = True
        db_table = 'ProductOptions'