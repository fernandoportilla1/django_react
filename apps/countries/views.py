from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from apps.countries.forms import CountryForm
from apps.countries.models import Country


# Create your views here.


class CountryListView(ListView):
    model = Country


class CountryCreateView(CreateView):
    model = Country
    form_class = CountryForm
    success_url = reverse_lazy('country-list')
