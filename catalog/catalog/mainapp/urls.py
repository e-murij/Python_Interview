from django.urls import path

from mainapp.views import CatalogListView, SectionListView

urlpatterns = [
    path('', CatalogListView.as_view(), name='index'),
    path('<int:pk>/', SectionListView.as_view(), name='section'),
]
