from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from mainapp.models import Catalog


class CatalogListView(ListView):
    model = Catalog
    template_name = 'catalog_list.html'

