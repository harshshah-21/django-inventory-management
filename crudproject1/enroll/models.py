from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

from phonenumber_field.modelfields import PhoneNumberField
from gst_field.modelfields import GSTField


class Category(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=70)
    phone = PhoneNumberField(null=False, blank=False)
    # phone = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    gst_no = GSTField(null=False, blank=False)
    address = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name


class Fabric(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name


class TaxClass(models.Model):
    tax_class = models.PositiveSmallIntegerField(null=False, blank=False)

    def __str__(self):
        return str(self.tax_class)


class ReturnPolicy(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name



# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=70)
    cover_image = models.ImageField(upload_to='images/')
    
    price = models.PositiveIntegerField(default=0)
    weight = models.PositiveIntegerField(default=0)

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="category", default="0"
    )
    sub_category = models.ForeignKey(
        SubCategory, on_delete=models.CASCADE, related_name="sub_category", default="0"
    )
    fabric_top = models.ForeignKey(
        Fabric, on_delete=models.CASCADE, related_name="fabric_top", default="0"
    )
    fabric_bottom = models.ForeignKey(
        Fabric, on_delete=models.CASCADE, related_name="fabric_bottom", default="0"
    )
    fabric_dupatta = models.ForeignKey(
        Fabric, on_delete=models.CASCADE, related_name="fabric_dupatta", default="0"
    )
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE, related_name="brand", default="0"
    )
    gst_type = models.ForeignKey(
        TaxClass, on_delete=models.CASCADE, related_name="gst_type", default="0"
    )
    return_policy = models.ForeignKey(
        ReturnPolicy, on_delete=models.CASCADE, related_name="return_policy", default="0"
    )
    supplier = models.ForeignKey(
        Supplier, on_delete=models.CASCADE, related_name="supplier", default="0"
    )
    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Products,default=None,on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'product/images/')
    
    def __str__(self):
        return self.post.title
    

class Inventory(models.Model):
    inventory_products = models.ForeignKey(
        Products, on_delete=models.CASCADE, related_name="inventory_products", default="0"
    )
    no_of_sets = models.PositiveIntegerField()
    no_of_piece_per_set = models.PositiveIntegerField()

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    role = models.CharField(max_length=70)
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    phone = PhoneNumberField(null=False, blank=False)
    aadhaar_id = models.CharField(max_length=12) 

class Order(models.Model):
    order_products = models.ForeignKey(
        Products, on_delete=models.CASCADE, related_name="order_products", default="0"
    )
    no_of_sets = models.PositiveIntegerField()
    price = models.PositiveIntegerField()