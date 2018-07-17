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
from webapp import views,forms
from django.views.generic import ListView,DetailView
from webapp.models import Machines
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.post_create),
    path('Update', views.post_create),
    path('api/v1/Retrive/', views.StackViewList.as_view(), name='update_sensor'),
    path('api/v1/update/', views.UpdateOperation.as_view(), name='update_sensor'),
    path('index', views.show),
    path('done', views.done),
    path('getUnique/', views.showUnqiueStack),
    path('api/v1/Stack/', views.StackList.as_view()),
    path('api/v1/Stack/<slug:MC_No>', views.uniqueStackList.as_view(), name='get_sensor'),
    path('api/v1/StackView/<slug:MC_No>', views.uniqueStackViewList.as_view(), name='get_sensor'),
    path('api/v1/Stack/<slug:MC_No>/update/', views.MultiOperation.as_view(), name='update_sensor'),
    # path('api/v1/Stack/update/', views.MultiOperation.as_view(), name='update_sensor'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
