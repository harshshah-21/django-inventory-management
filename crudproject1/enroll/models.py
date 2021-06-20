from django.db import models
from django.core.validators import RegexValidator

from phonenumber_field.modelfields import PhoneNumberField
from gst_field.modelfields import GSTField

class Category(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name


# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=70)
    type = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    # category = models.CharField(max_length=70)

class Supplier(models.Model):
    name = models.CharField(max_length=70)
    phone = PhoneNumberField(null=False, blank=False)
    # phone = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    gst_no = GSTField(null=False, blank=False)
    address = models.CharField(max_length=300)


class SubCategory(models.Model):
    name = models.CharField(max_length=70)

class Brand(models.Model):
    name = models.CharField(max_length=70)

class Fabric(models.Model):
    name = models.CharField(max_length=70)

class TaxClass(models.Model):
    tax_class = models.PositiveSmallIntegerField(null=False, blank=False)

class ReturnPolicy(models.Model):
    name = models.CharField(max_length=70)

