from django.conf import settings
from django.core.paginator import Paginator
from django.db.models import F
from django.shortcuts import render
from rest_framework import status

from coffee.forms import SendCV
from coffee.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer


def home(requests):
    context = {
        'title': 'Home',
    }
    return render(requests, 'coffee/home.html', context=context)


def menu(requests):
    categories = Categories.objects.all()
    menu = {}
    for cat in categories:
        categ = []
        products = Product.objects.filter(category=cat.id)
        for product in products:
            if product.category == cat:
                categ.append(product)
        menu[cat.title] = categ
    context = {
        'menu': menu,
        'nav': 'menu',
        'title': 'Menu',
        'cat': categories,
    }
    print(requests.session)
    return render(requests, 'coffee/menu.html', context=context)


@api_view(["GET"])
def health_check(request):
    return Response({"status": "Ok"}, status.HTTP_200_OK)


def about(requests):
    context = {
        'nav': 'about',
        'title': 'About',
    }
    return render(requests, 'coffee/about.html', context=context)


def contacts(requests):
    contacts = Contacts.objects.all()
    context = {
        'nav': 'contacts',
        'title': 'Contacts',
        'contacts': contacts,
    }
    return render(requests, 'coffee/contacts.html', context=context)


def show_contact(requests, slug):
    contact = Contacts.objects.get(slug=slug)
    context = {
        'nav': 'contacts',
        'title': 'Contacts',
        'contact': contact
    }
    return render(requests, 'coffee/contact.html', context=context)


def work_place(requests):
    work_places = CoffeeShop.objects.all()
    context = {
        'nav': 'work',
        'title': 'Work',
        'work_places': work_places,
    }
    return render(requests, 'coffee/work-place.html', context=context)





def shops(request):
    # session = request.session
    # cart = session.get(settings.CART_SESSION_ID)
    #
    #
    # email = request.META
    # print(email)
    # # if not cart:
    # #     cart = session[settings.CART_SESSION_ID] = {}
    # # cart['is_publish'] = False
    # #
    # # if session.get(settings.CART_SESSION_ID)['is_publish'] == False:
    # #     print(12312)
    # #
    # # print(cart)
    # cart['is_publish'] = False
    #
    # # del requests.session['cart']
    # # cart['name'] = 'Maks'
    # # cart['data'] = {
    # #     'age': 23,
    # #     'gender': 'Men'
    # # }
    # # print(cart)
    #
    # # requests.session['123'] = 234
    # # requests.session['qwe'] = 'rty'
    # # print(requests.session)
    # # print(requests.session['123'])
    #
    #

    shops = CoffeeShop.objects.all()
    context = {
        'nav': 'shops',
        'title': 'Shops',
        'shops': shops
    }
    return render(request, 'coffee/shops.html', context=context)


def show_shop(requests, slug):
    shop = CoffeeShop.objects.get(slug=slug)
    context = {
        'nav': 'shop',
        'title': 'Shop',
        'shop': shop
    }
    return render(requests, 'coffee/shop.html', context=context)


def work_by_place(requests, slug):
    if slug == 'all':
        work_list = Worker.objects.all()
        paginator = Paginator(work_list, 2)
    else:
        work_list = Worker.objects.filter(coffee_shop__slug=slug)
        paginator = Paginator(work_list, 2)
    page_number = requests.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'nav': 'work',
        'title': 'Work',
        'page_obj': page_obj,
        'page_number': page_number,
    }
    return render(requests, 'coffee/work-by-place.html', context=context)


def work(requests, slug):
    if requests.method == 'POST':
        form = SendCV(requests.POST)
        if form.is_valid():
            Summary.objects.create(**form.cleaned_data)
            print(form.cleaned_data)
    form = SendCV()
    vacancy = Worker.objects.get(slug=slug)
    vacancy.views = F('views')+1
    vacancy.save()
    context = {
        'nav': 'work',
        'title': 'Work',
        'vacancy': vacancy,
        'form': form,
    }
    return render(requests, 'coffee/vacancy.html', context=context)

