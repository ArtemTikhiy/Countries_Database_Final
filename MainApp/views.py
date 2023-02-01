from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound
import json
# from MainApp.models import Country
import string

# Create your views here.


with open('/home/student/Projects/First_DZ/country-by-languages.json') as json_file:
    data = json.load(json_file)

country_list = data

alphabet = list(string.ascii_uppercase)


def main(request):
    return render(request, 'main.html')


def all_countries(request, page_number):
    country_paginator = []
    for item in country_list:
        country_paginator.append(item['country'])

    valid_page = 1

    if isinstance(page_number, int) == True:
        valid_page = page_number

    paginator = Paginator(country_paginator, 10)

    page = paginator.get_page(valid_page)

    context = {
        'country_list': country_list,
        'alphabet': alphabet,
        'page': page,
        'count': paginator.count
    }
    return render(request, "country_list.html", context)


def country_page(request, country):
    country_valid = country[0].upper() + country[1::]
    page_title = country_valid
    for item in country_list:
        if item['country'] == country or item['country'] == country_valid:
            context = {
                "item": item,
                "page_title": page_title
            }
            return render(request, 'country_page.html', context)
    return HttpResponseNotFound(f"Страны с названием {country} не существует.")


def countries_by_letter(request, letter):
    letter_valid = letter.upper()
    temporary = []
    for item in country_list:
        if item['country'][0] == letter_valid:
            temporary.append(item['country'])
    context = {
        'temporary': temporary,
        'letter_valid': letter_valid,
    }
    return render(request, "countries_by_letter.html", context)


def languages(request):
    temporary = []
    for item in country_list:
        for language in item['languages']:
            temporary.append(language)
    temporary2 = sorted(set(temporary))
    context = {
        'temporary2': temporary2,
    }
    return render(request, "languages.html", context)

def language_one(request, language):
    temporary = []
    language_valid = language[0].upper() + language[1::]
    page_title = language_valid
    for item in country_list:
        if language_valid in item['languages']:
            temporary.append(item['country'])
    context = {
        "temporary": temporary,
        "page_title": page_title
    }
    return render(request, 'language.html', context)




