"""crudproject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from enroll import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("view_products", views.view_products, name="view_products"),
    path("add_product", views.add_show, name="add_product"),
    path("update_product", views.update_product, name="update_product"),
    path("add_inventory_item", views.add_inventory_item, name="add_inventory_item"),
    path(
        "view_inventory_items", views.view_inventory_items, name="view_inventory_items"
    ),
    path(
        "update_inventory_item/<int:id>/",
        views.update_inventory_item,
        name="update_inventory_item",
    ),
    path(
        "delete_inventory_item/<int:id>/",
        views.delete_inventory_item,
        name="delete_inventory_item",
    ),
    path("delete/<int:id>/", views.delete_product, name="delete_product"),
    path("<int:id>/", views.update_product, name="update_product"),
    path("view_supplier/", views.view_supplier, name="view_supplier"),
    path("add_supplier/", views.add_supplier, name="add_supplier"),
    path("supplier/delete/<int:id>/", views.delete_supplier, name="delete_supplier"),
    path("supplier/update/<int:id>/", views.update_supplier, name="update_supplier"),
    path("category/", views.add_category, name="view_category"),
    path("category/delete/<int:id>/", views.delete_category, name="delete_category"),
    path("category/update/<int:id>/", views.update_category, name="update_category"),
    path("subcategory/", views.add_subcategory, name="view_subcategory"),
    path(
        "subcategory/delete/<int:id>/",
        views.delete_subcategory,
        name="delete_subcategory",
    ),
    path(
        "subcategory/update/<int:id>/",
        views.update_subcategory,
        name="update_subcategory",
    ),
    path("brand/", views.add_brand, name="view_brand"),
    path("brand/delete/<int:id>/", views.delete_brand, name="delete_brand"),
    path("brand/update/<int:id>/", views.update_brand, name="update_brand"),
    path("fabric/", views.add_fabric, name="view_fabric"),
    path("fabric/delete/<int:id>/", views.delete_fabric, name="delete_fabric"),
    path("fabric/update/<int:id>/", views.update_fabric, name="update_fabric"),
    path("returnpolicy/", views.add_returnpolicy, name="view_returnpolicy"),
    path(
        "returnpolicy/delete/<int:id>/",
        views.delete_returnpolicy,
        name="delete_returnpolicy",
    ),
    path(
        "returnpolicy/update/<int:id>/",
        views.update_returnpolicy,
        name="update_returnpolicy",
    ),
    # path('', views.login, name="login"),
    path("", views.login_request, name="login"),
    path("logout/", views.logout_request, name="logout"),
    path("register/", views.register_request, name="register"),
    path("tax_class/", views.add_tax_class, name="tax_class"),
    path("tax_class/delete/<int:id>/", views.delete_tax_class, name="delete_tax_class"),
    path("tax_class/update/<int:id>/", views.update_tax_class, name="update_tax_class"),
    
    path("password_reset/", views.password_reset_request, name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='enroll/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="enroll/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='enroll/password_reset_complete.html'), name='password_reset_complete'),      
    
    path("view_order_items", views.view_order_items, name="view_order_items"),
    path("add_order_item", views.add_order_item, name="add_order_item"),
    path("delete_order_item/<int:id>", views.delete_order_item, name="delete_order_item")
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
