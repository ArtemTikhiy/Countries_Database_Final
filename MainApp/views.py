from Countries2_DataBase.wsgi import *
from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound
import json
from MainApp.models import Country
import string

# Create your views here.


alphabet = list(string.ascii_uppercase)


def main(request):
    return render(request, 'main.html')


def all_countries(request):
    items = Country.objects.all()

    country_paginator = Paginator(items, 10)

    page_number = request.GET.get('page','1')
    page = country_paginator.get_page(page_number)

    context = {
        'alphabet': alphabet,
        'page': page,
        'count': country_paginator.count
    }
    return render(request, "country_list.html", context)


def country_page(request, country):
    items = Country.objects.all()
    country_valid = country[0].upper() + country[1::]
    page_title = country_valid
    for item in items:
        if item.country == country or item.country == country_valid:
            context = {
                "item": item,
                "page_title": page_title
            }
            return render(request, 'country_page.html', context)
    return HttpResponseNotFound(f"Страны с названием {country} не существует.")


def countries_by_letter(request, letter):
    items = Country.objects.all()
    letter_valid = letter.upper()
    temporary = []
    # TODO: вы реализовали фильтрацию объектов на уровне питона, нужно реализовать на уровне БД.
    #  Подробнее тут: https://tutorial.djangogirls.org/ru/django_orm/#%D1%84%D0%B8%D0%BB%D1%8C%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D0%BE%D0%B1%D1%8A%D0%B5%D0%BA%D1%82%D0%BE%D0%B2
    for item in items:
        if item.country[0] == letter_valid:
            temporary.append(item.country)
    context = {
        'temporary': temporary,
        'letter_valid': letter_valid,
    }
    return render(request, "countries_by_letter.html", context)


def languages(request):
    items = Country.objects.all()
    temporary = []
    for item in items:
        for language in item.languages:
            temporary.append(language)
    temporary2 = sorted(set(temporary))
    context = {
        'temporary2': temporary2,
    }
    return render(request, "languages.html", context)

def language_one(request, language):
    items = Country.objects.all()
    temporary = []
    language_valid = language[0].upper() + language[1::]
    page_title = language_valid
    # TODO: тут тоже самое, фильтрацию объектов делаем на уровне БД
    for item in items:
        if language_valid in item.languages:
            temporary.append(item.country)
    context = {
        "temporary": temporary,
        "page_title": page_title
    }
    return render(request, 'language.html', context)









