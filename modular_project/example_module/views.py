from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Product
from .forms import ProductForm
from engine.models import Module

def is_manager(user):
    return user.groups.filter(name='manager').exists()

def is_normal_user(user):
    return user.groups.filter(name='user').exists()

# Public view (Read only)
def product_list(request):
    module = Module.objects.filter(name="Example Module", installed=True).first()
    if not module:
        return render(request, "example_module/not_installed.html")
    
    products = Product.objects.all()
    return render(request, 'example_module/product_list.html', {'products': products})

# Manager and User views (Create, Read, Update)
@login_required
def product_create(request):
    if not (is_manager(request.user) or is_normal_user(request.user)):
        messages.error(request, "You don't have permission to create products.")
        return redirect('example_module:product_list')

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product created successfully!')
            return redirect('example_module:product_list')
    else:
        form = ProductForm()
    
    return render(request, 'example_module/product_form.html', {'form': form, 'action': 'Create'})

@login_required
def product_update(request, pk):
    if not (is_manager(request.user) or is_normal_user(request.user)):
        messages.error(request, "You don't have permission to update products.")
        return redirect('example_module:product_list')

    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully!')
            return redirect('example_module:product_list')
    else:
        form = ProductForm(instance=product)
    
    return render(request, 'example_module/product_form.html', {'form': form, 'action': 'Update'})

# Manager only view (Delete)
@login_required
@user_passes_test(is_manager)
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted successfully!')
        return redirect('example_module:product_list')
    return render(request, 'example_module/product_confirm_delete.html', {'product': product})
