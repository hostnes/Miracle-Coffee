from django.contrib import admin
from django.urls import path, include

from coffee.views import menu, about, contacts, work_place, shops, home, show_contact, show_shop, \
    work_by_place, work, health_check

urlpatterns = [
    path('', home, name='home'),
    path('menu', menu, name='menu'),
    path('about', about, name='about'),
    path('contacts', contacts, name='contacts'),
    path('contact/<slug:slug>', show_contact, name='contact'),
    path('work', work_place, name='work'),
    path('work/<slug:slug>', work_by_place, name='work_by_place'),
    path('work/vacancy/<slug:slug>', work, name='vacancy'),
    path('shops', shops, name='shops'),
    path('shop/<slug:slug>', show_shop, name='shop'),
    path('ping/', health_check),

]
