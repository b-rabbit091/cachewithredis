# YourApp/urls.py
from django.contrib import admin
from django.urls import path
from task1.views import calculate_average_age

urlpatterns = [
    path('admin/', admin.site.urls),
    path('calculate_average_age/', calculate_average_age, name='calculate_average_age'),

]
