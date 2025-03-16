from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from engine.views import home, logout_view

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('engine/', include('engine.urls')),
    path('example-module/', include('example_module.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),  # Changed to custom logout view
]
