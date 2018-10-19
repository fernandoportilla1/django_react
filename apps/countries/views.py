from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.countries.models import Country, City
from apps.countries.forms import CountryForm

# Create your views here.


class CountryListView(ListView):
    model = Country


class CountryCreateView(CreateView):
    model = Country
    form_class = CountryForm
    success_url = reverse_lazy('country-list')
