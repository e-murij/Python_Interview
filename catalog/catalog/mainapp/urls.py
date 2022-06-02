from django.urls import path

from mainapp.views import CatalogListView

urlpatterns = [
    path('', CatalogListView.as_view(), name='index'),
]