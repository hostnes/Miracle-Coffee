from django.contrib import admin

from coffee.models import *

@admin.register(CoffeeShop)
class CoinsAdmin(admin.ModelAdmin):
    list_display = ("street",)


@admin.register(Categories)
class CoinsAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(Product)
class CoinsAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(Worker)
class CoinsAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(Contacts)
class CoinsAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(Summary)
class CoinsAdmin(admin.ModelAdmin):
    list_display = ("name",)