from django.http import request
from django.shortcuts import render, HttpResponseRedirect
from .forms import *
from .models import *
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages  # import messages
from django.contrib.auth.forms import AuthenticationForm  # add this
from django.contrib.auth.decorators import login_required


# Create your views here.
def login_request(request):
    if request.user.is_authenticated:
        return logout_request(request)
    else:
        if request.method == "POST":
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password")
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.info(request, "You are now logged in as {username}.")
                    return HttpResponseRedirect("/view_products")
                else:
                    messages.error(request, "Invalid username or password.")
            else:
                messages.error(request, "Invalid username or password.")
        form = AuthenticationForm()
        return render(request, "enroll/authlogin.html", {"login_form": form})


def validate_login(request):
    if not request.user.is_authenticated:
        return login_request(request)


def add_show(request):
    validate_login(request)
    if request.method == "POST":
        images =request.FILES.getlist('images')
        print(request.FILES)
        p1 = AddProduct(request.POST,request.FILES)
        print("recieved p1")
        print(p1.is_valid())
        if p1.is_valid():
            curr_prod=p1.save()
            p1 = AddProduct()

            for img in images:
                print(img)
                ProductImage.objects.create(product=curr_prod,images=img)
    else:
        p1 = AddProduct()
    return render(request, "enroll/add_product.html", {"form": p1})


def view_products(request):
    validate_login(request)
    products = Products.objects.all()
    print(products)
    return render(request, "enroll/view_products.html", {"prod": products})


def delete_product(request, id):
    validate_login(request)
    if request.method == "POST":
        p = Products.objects.get(pk=id)
        p.delete()
        return HttpResponseRedirect("/")


def update_product(request, id):
    validate_login(request)
    if request.method == "POST":
        p = Products.objects.get(pk=id)
        form_obj = AddProduct(request.POST, instance=p)
        if form_obj.is_valid():
            form_obj.save()
    else:
        p = Products.objects.get(pk=id)
        form_obj = AddProduct(instance=p)
    return render(request, "enroll/update_product.html", {"form": form_obj})


def add_supplier(request):
    validate_login(request)
    if request.method == "POST":
        supp = SupplierForm(request.POST)
        if supp.is_valid():
            supp.save()
            supp = SupplierForm()

    else:
        supp = SupplierForm()
    suppliers = Supplier.objects.all()
    return render(
        request, "enroll/add_supplier.html", {"supp_form": supp, "supp": suppliers}
    )


def view_supplier(request):
    validate_login(request)
    suppliers = Supplier.objects.all()
    return render(request, "enroll/view_supplier.html", {"supp": suppliers})


def delete_supplier(request, id):
    validate_login(request)
    if request.method == "POST":
        p = Supplier.objects.get(pk=id)
        p.delete()
        return HttpResponseRedirect("/view_supplier")


def update_supplier(request, id):
    validate_login(request)
    if request.method == "POST":
        p = Supplier.objects.get(pk=id)
        form_obj = SupplierForm(request.POST, instance=p)
        if form_obj.is_valid():
            form_obj.save()
    else:
        p = Supplier.objects.get(pk=id)
        form_obj = SupplierForm(instance=p)
    return render(request, "enroll/update_supplier.html", {"form": form_obj})


def add_category(request):
    validate_login(request)
    if request.method == "POST":
        formobj = CategoryForm(request.POST)
        if formobj.is_valid():

            formobj.save()
            formobj = CategoryForm()

    else:
        formobj = CategoryForm()
    modobj = Category.objects.all()
    return render(
        request, "enroll/view_category.html", {"obj_form": formobj, "obj_mod": modobj}
    )


def delete_category(request, id):
    validate_login(request)
    if request.method == "POST":
        p = Category.objects.get(pk=id)
        p.delete()
        return HttpResponseRedirect("/category")


def update_category(request, id):
    validate_login(request)
    if request.method == "POST":
        p = Category.objects.get(pk=id)
        form_obj = CategoryForm(request.POST, instance=p)
        if form_obj.is_valid():
            form_obj.save()
    else:
        p = Category.objects.get(pk=id)
        form_obj = CategoryForm(instance=p)
    return render(request, "enroll/update_category.html", {"form": form_obj})


def add_subcategory(request):
    validate_login(request)
    if request.method == "POST":
        formobj = SubCategoryForm(request.POST)
        if formobj.is_valid():

            formobj.save()
            formobj = SubCategoryForm()

    else:
        formobj = SubCategoryForm()
    modobj = SubCategory.objects.all()
    return render(
        request,
        "enroll/view_subcategory.html",
        {"obj_form": formobj, "obj_mod": modobj},
    )


def delete_subcategory(request, id):
    validate_login(request)
    if request.method == "POST":
        p = SubCategory.objects.get(pk=id)
        p.delete()
        return HttpResponseRedirect("/subcategory")


def update_subcategory(request, id):
    validate_login(request)
    if request.method == "POST":
        p = SubCategory.objects.get(pk=id)
        form_obj = SubCategoryForm(request.POST, instance=p)
        if form_obj.is_valid():
            form_obj.save()
    else:
        p = SubCategory.objects.get(pk=id)
        form_obj = SubCategoryForm(instance=p)
    return render(request, "enroll/update_subcategory.html", {"form": form_obj})


def add_brand(request):
    validate_login(request)
    if request.method == "POST":
        formobj = BrandForm(request.POST)
        if formobj.is_valid():

            formobj.save()
            formobj = BrandForm()

    else:
        formobj = BrandForm()
    modobj = Brand.objects.all()
    return render(
        request, "enroll/view_brand.html", {"obj_form": formobj, "obj_mod": modobj}
    )


def delete_brand(request, id):
    validate_login(request)
    if request.method == "POST":
        p = Brand.objects.get(pk=id)
        p.delete()
        return HttpResponseRedirect("/brand")


def update_brand(request, id):
    validate_login(request)
    if request.method == "POST":
        p = Brand.objects.get(pk=id)
        form_obj = BrandForm(request.POST, instance=p)
        if form_obj.is_valid():
            form_obj.save()
    else:
        p = Brand.objects.get(pk=id)
        form_obj = BrandForm(instance=p)
    return render(request, "enroll/update_brand.html", {"form": form_obj})


def add_fabric(request):
    validate_login(request)
    if request.method == "POST":
        formobj = FabricForm(request.POST)
        if formobj.is_valid():

            formobj.save()
            formobj = FabricForm()

    else:
        formobj = FabricForm()
    modobj = Fabric.objects.all()
    return render(
        request, "enroll/view_fabric.html", {"obj_form": formobj, "obj_mod": modobj}
    )


def delete_fabric(request, id):
    validate_login(request)
    if request.method == "POST":
        p = Fabric.objects.get(pk=id)
        p.delete()
        return HttpResponseRedirect("/fabric")


def update_fabric(request, id):
    validate_login(request)
    if request.method == "POST":
        p = Fabric.objects.get(pk=id)
        form_obj = FabricForm(request.POST, instance=p)
        if form_obj.is_valid():
            form_obj.save()
    else:
        p = Fabric.objects.get(pk=id)
        form_obj = FabricForm(instance=p)
    return render(request, "enroll/update_fabric.html", {"form": form_obj})


def add_returnpolicy(request):
    validate_login(request)
    if request.method == "POST":
        formobj = ReturnPolicyForm(request.POST)
        if formobj.is_valid():

            formobj.save()
            formobj = ReturnPolicyForm()

    else:
        formobj = ReturnPolicyForm()
    modobj = ReturnPolicy.objects.all()
    return render(
        request,
        "enroll/view_returnpolicy.html",
        {"obj_form": formobj, "obj_mod": modobj},
    )


def delete_returnpolicy(request, id):
    validate_login(request)
    if request.method == "POST":
        p = ReturnPolicy.objects.get(pk=id)
        p.delete()
        return HttpResponseRedirect("/returnpolicy")


def update_returnpolicy(request, id):
    validate_login(request)
    if request.method == "POST":
        p = ReturnPolicy.objects.get(pk=id)
        form_obj = ReturnPolicyForm(request.POST, instance=p)
        if form_obj.is_valid():
            form_obj.save()
    else:
        p = ReturnPolicy.objects.get(pk=id)
        form_obj = ReturnPolicyForm(instance=p)
    return render(request, "enroll/update_returnpolicy.html", {"form": form_obj})


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        form1 = NewProfileForm(request.POST)
        print(form.is_valid())
        print(form1.is_valid())
        if form.is_valid() and form1.is_valid(): 
            print("hello here")
            user = form.save()
            profile_data = form1.cleaned_data
            print(profile_data)
            Profile.objects.create(user = user,role = profile_data["role"],bio = profile_data["bio"],aadhaar_id = profile_data["aadhaar_id"],phone = profile_data["phone"],birth_date = profile_data["birth_date"])
            login(request, user)
            messages.success(request, "Registration successful.")
            return HttpResponseRedirect("/")
        else:
            print("Wait What!")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    form1 = NewProfileForm()
    return render(request, "enroll/register.html", context={"register_form": form,"profile_form": form1})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return HttpResponseRedirect("/")


def add_tax_class(request):
    validate_login(request)
    if request.method == "POST":
        formobj = TaxClassForm(request.POST)
        if formobj.is_valid():

            formobj.save()
            formobj = TaxClassForm()

    else:
        formobj = TaxClassForm()
    modobj = TaxClass.objects.all()
    return render(
        request, "enroll/tax_class.html", {"obj_form": formobj, "obj_mod": modobj}
    )


def delete_tax_class(request, id):
    validate_login(request)
    if request.method == "POST":
        p = TaxClass.objects.get(pk=id)
        p.delete()
        return HttpResponseRedirect("/tax_class")


def update_tax_class(request, id):
    validate_login(request)
    if request.method == "POST":
        p = TaxClass.objects.get(pk=id)
        form_obj = TaxClassForm(request.POST, instance=p)
        if form_obj.is_valid():
            form_obj.save()
    else:
        p = TaxClass.objects.get(pk=id)
        form_obj = TaxClassForm(instance=p)
    return render(request, "enroll/update_tax_class.html", {"form": form_obj})


def add_inventory_item(request):
    validate_login(request)
    if request.method == "POST":
        p1 = InventoryForm(request.POST)
        if p1.is_valid():
            p1.save()
            p1 = InventoryForm()

    else:
        p1 = InventoryForm()
    products = Inventory.objects.all()
    return render(request, "enroll/add_inventory.html", {"form": p1, "prod": products})


def view_inventory_items(request):
    validate_login(request)
    products = Inventory.objects.all()
    return render(request, "enroll/view_inventory.html", {"prod": products})


def delete_inventory_item(request, id):
    validate_login(request)
    if request.method == "POST":
        p = Inventory.objects.get(pk=id)
        p.delete()
        return HttpResponseRedirect("/view_inventory_items")


def update_inventory_item(request, id):
    validate_login(request)
    if request.method == "POST":
        p = Inventory.objects.get(pk=id)
        form_obj = InventoryForm(request.POST, instance=p)
        if form_obj.is_valid():
            form_obj.save()
    else:
        p = Inventory.objects.get(pk=id)
        form_obj = InventoryForm(instance=p)
    return render(request, "enroll/update_inventory.html", {"form": form_obj})
