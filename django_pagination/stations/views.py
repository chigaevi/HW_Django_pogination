import os
import csv
from pathlib import Path

from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
# from django_pagination.django_pagination.settings import BUS_STATION_CSV

# при попытке имортировать путь BUS_STATION_CSV возникает ошибка
# No module named 'django_pagination.django_pagination'
# поэтому пришлось напрямую определить в этом модуле BUS_STATION_CSV

BASE_DIR = Path(__file__).resolve().parent.parent
BUS_STATION_CSV = os.path.join(BASE_DIR, 'data-398-2018-08-30.csv')


def index(request):
    return redirect(reverse('bus_stations'))


def _get_stations_list():
    stations_list = []
    with open(BUS_STATION_CSV, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for stations in reader:
            stations_list.append(stations)
    return stations_list


def bus_stations(request):
    page_number = request.GET.get('page', 1)
    stations_list = _get_stations_list()
    paginator = Paginator(stations_list, 10)
    page = paginator.get_page(page_number)
    context = {
        'page': page,
    }
    return render(request, 'stations/index.html', context)
