"""moisture_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from rest_framework.urlpatterns import format_suffix_patterns
from webapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.welcome),
    path('api/v1/sensors/', views.sensorList.as_view()),
    path('api/v1/sensors/<slug:rm_No>/', views.uniqueSensorList.as_view(), name='get_sensor'),
    path('api/v1/sensors/<slug:rm_No>/update/', views.MultiOperation.as_view(), name='update_sensor'),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework')),
  #  path('api/v1/sensors/', views.MultiOperation.as_view(),name='sensor_details'),
]
