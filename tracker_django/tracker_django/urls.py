"""
URL configuration for tracker_django project.

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
from django.urls import path
from food_consuming import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name="index"),
    path('delete/<int:id>/', views.DeleteView.as_view(), name="delete"),
    path('delete_consumed_food/<int:pk>/', views.delete_consumed_food, name='delete_consumed_food'),
    path('test/', views.test, name='index'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
]
