"""
URL configuration for My_Test project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from Vehicle_App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage_view,  name='home'),
    path('v_list/', views.vehicle_list, name='vehicle_list'),
    path('v_details/<int:vehicle_id>/', views.vehicle_details, name='vehicle_details'),
    path('v_add/', views.add_vehicle, name='add_vehicle'),
    path('v_update/<int:id>/', views.vehicle_update, name='v_update'),
    path('v_delete/<int:id>/', views.vehicle_delete, name='v_delete'),
    path('api/', include('Vehicle_App.api.urls')),

]


