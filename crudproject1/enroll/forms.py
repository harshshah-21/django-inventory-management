from django.core import validators
from django import forms
from django.db.models import fields
from django.forms.widgets import Widget
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ["name", "phone", "gst_no", "address"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "gst_no": forms.TextInput(attrs={"class": "form-control"}),
            "address": forms.Textarea(attrs={"class": "form-control"}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
        }

class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
        }

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
        }

class FabricForm(forms.ModelForm):
    class Meta:
        model = Fabric
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
        }

class TaxClassForm(forms.ModelForm):
    class Meta:
        model = TaxClass
        fields = ["tax_class"]
        widgets = {
            "tax_class": forms.TextInput(attrs={"class": "form-control"}),
        }

class ReturnPolicyForm(forms.ModelForm):
    class Meta:
        model = ReturnPolicy
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
        }

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields= ["role","aadhaar_id","bio","phone","birth_date"]

class AddProduct(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={"class": "form-select col-sm-8"}),
    )
    sub_category = forms.ModelChoiceField(
        queryset=SubCategory.objects.all(),
        widget=forms.Select(attrs={"class": "form-select col-sm-8"}),
    )
    fabric_top = forms.ModelChoiceField(
        queryset=Fabric.objects.all(),
        widget=forms.Select(attrs={"class": "form-select col-sm-4"}),
    )
    fabric_bottom = forms.ModelChoiceField(
        queryset=Fabric.objects.all(),
        widget=forms.Select(attrs={"class": "form-select col-sm-4"}),
    )
    fabric_dupatta = forms.ModelChoiceField(
        queryset=Fabric.objects.all(),
        widget=forms.Select(attrs={"class": "form-select col-sm-4"}),
    )
    brand = forms.ModelChoiceField(
        queryset=Brand.objects.all(),
        widget=forms.Select(attrs={"class": "form-select col-sm-4"}),
    )
    gst_type = forms.ModelChoiceField(
        queryset=TaxClass.objects.all(),
        widget=forms.Select(attrs={"class": "form-select col-sm-4"}),
    )
    return_policy = forms.ModelChoiceField(
        queryset=ReturnPolicy.objects.all(),
        widget=forms.Select(attrs={"class": "form-select col-sm-4"}),
    )
    supplier = forms.ModelChoiceField(
        queryset=Supplier.objects.all(),
        widget=forms.Select(attrs={"class": "form-select col-sm-4"}),
    )

    class Meta:
        model = Products
        fields = ["name", "category","sub_category","fabric_top","fabric_bottom","fabric_dupatta","brand","gst_type","price","weight","return_policy","supplier","cover_image"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "price": forms.TextInput(attrs={"class": "form-control"}),
            "weight": forms.TextInput(attrs={"class": "form-control"}),
            # "type": forms.TextInput(attrs={"class": "form-control"}),
            "other_info": forms.Textarea(attrs={"class": "form-control"}),
        }

class InventoryForm(forms.ModelForm):
    inventory_products = forms.ModelChoiceField(
        queryset=Products.objects.all(),
        widget=forms.Select(attrs={"class": "form-select col-sm-8"}),
    )
    class Meta:
        model = Inventory
        fields = ["inventory_products", "no_of_sets","no_of_piece_per_set"]
        widgets = {
            "no_of_sets": forms.TextInput(attrs={"class": "form-control"}),
            "no_of_piece_per_set": forms.TextInput(attrs={"class": "form-control"}),
        }

class OrderForm(forms.ModelForm):
    order_products = forms.ModelChoiceField(
        queryset=Products.objects.all(),
        widget=forms.Select(attrs={"class": "form-select col-sm-8"}),
    )
    class Meta:
        model = Order
        fields = ["order_products", "no_of_sets","price"]
        widgets = {
            "no_of_sets": forms.TextInput(attrs={"class": "form-control"}),
            "price": forms.TextInput(attrs={"class": "form-control"}),
        }