from django.urls import path

from .views import CountryListView, CountryCreateView

urlpatterns = [
    path('country', CountryListView.as_view(), name='country-list'),
    path('country/create', CountryCreateView.as_view(), name='country-create'),
]
