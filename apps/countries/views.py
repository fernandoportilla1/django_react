from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from apps.countries.forms import CountryForm
from apps.countries.models import Country, City


# Create your views here.


class CountryListView(ListView):
    model = Country

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_country'] = 'active'
        return context


class CountryCreateView(CreateView):
    model = Country
    form_class = CountryForm
    success_url = reverse_lazy('country-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_country'] = 'active'
        return context


class CityListView(ListView):
    model = City
    template_name = 'cities/city_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_city'] = 'active'
        return context
