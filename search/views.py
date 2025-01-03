from django.shortcuts import render
from django.db.models import Q
# Create your views here.

from django.views.generic import ListView

from products.models import Product

class SearchProductView(ListView):

    template_name = "products/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(SearchProductView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', None)
        if query is not None:
            return Product.object.search(query)
        return Product.object.featured()

