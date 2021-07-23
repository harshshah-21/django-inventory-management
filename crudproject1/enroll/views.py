from django.http import request,HttpResponse
from django.shortcuts import render, HttpResponseRedirect,redirect, get_object_or_404
from django.core.mail import send_mail, BadHeaderError
from .forms import *
from .models import *
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages  # import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordResetForm # add this
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes



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
                    messages.info(request, "You are now logged in as " + username + ".")
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
        p1 = AddProduct(request.POST,request.FILES)
        if p1.is_valid():
            curr_prod=p1.save()
            p1 = AddProduct()

            for img in images:
                ProductImage.objects.create(product=curr_prod,images=img)
    else:
        p1 = AddProduct()
    return render(request, "enroll/add_product.html", {"form": p1})


def view_products(request):
    validate_login(request)
    products = Products.objects.all()
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
        if form.is_valid() and form1.is_valid(): 
            user = form.save()
            profile_data = form1.cleaned_data
            Profile.objects.create(user = user,role = profile_data["role"],bio = profile_data["bio"],aadhaar_id = profile_data["aadhaar_id"],phone = profile_data["phone"],birth_date = profile_data["birth_date"])
            login(request, user)
            messages.success(request, "Registration successful.")
            return HttpResponseRedirect("/")
        else:
            pass
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


def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "enroll/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="enroll/password_reset.html", context={"password_reset_form":password_reset_form})


def add_order_item(request):
    validate_login(request)
    if request.method == "POST":
        p1 = OrderForm(request.POST)
        associated_product = Inventory.objects.get(inventory_products=request.POST.get("order_products"))
        associated_product.no_of_sets = (associated_product.no_of_sets - int(request.POST.get("no_of_sets")))
        if p1.is_valid():
            p1.save()
            associated_product.save()
            p1 = OrderForm()
    else:
        p1 = OrderForm()    
    orders = Order.objects.all()
    return render(request, "enroll/add_order.html", {"form": p1, "prod": orders})


def view_order_items(request):
    validate_login(request)
    orders = Order.objects.all()
    return render(request, "enroll/view_orders.html", {"orders": orders})


def delete_order_item(request, id):
    validate_login(request)
    if request.method == "POST":
        p = Order.objects.get(pk=id)
        associated_product = get_object_or_404(Inventory, inventory_products=p.order_products)
        associated_product.no_of_sets = (associated_product.no_of_sets + p.no_of_sets)
        p.delete()
        associated_product.save()
        return HttpResponseRedirect("/view_order_items")

