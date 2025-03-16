from django.shortcuts import render, redirect
from django.urls import clear_url_caches
from django.contrib.auth.decorators import login_required
from .models import Module
from django.contrib.auth import logout
from django.shortcuts import redirect

def home(request):
    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def module_list(request):
    modules = Module.objects.all()
    example_module_installed = Module.objects.filter(name="Example Module", installed=True).exists()
    return render(request, 'engine/module_list.html', {
        'modules': modules,
        'example_module_installed': example_module_installed
    })


def install_module(request, module_name):
    module, created = Module.objects.get_or_create(name=module_name)
    module.installed = True
    module.save()
    reload_urls()
    return redirect('module_list')

def uninstall_module(request, module_name):
    module = Module.objects.get(name=module_name)
    module.installed = False
    module.save()
    reload_urls()
    return redirect('module_list')

def upgrade_module(request, module_name):
    module = Module.objects.get(name=module_name)
    if module.installed:
        # Upgrade logic here
        pass
    return redirect('module_list')

def reload_urls():
    clear_url_caches()
