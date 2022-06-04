from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from mainapp.models import Catalog, Section


class SectionListView(ListView):
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({
            'sections': Section.on_site.all(),
            'site': get_current_site(request=self.request)
        })
        return context


class CatalogListView(SectionListView):
    model = Catalog
    template_name = 'catalog_list.html'
    queryset = Catalog.on_site.select_related('provider').select_related('measure').prefetch_related('sections').all()


class SectionListView(SectionListView):
    template_name = 'catalog_list.html'
    model = Catalog

    def get_queryset(self):
        queryset = Catalog.on_site.select_related('provider').select_related('measure').prefetch_related(
            'sections').all()
        return queryset.filter(sections=self.kwargs['pk'])
