from django.urls import path

from .views import CountryListView, CountryCreateView, CityListView

urlpatterns = [
    path('country', CountryListView.as_view(), name='country-list-view'),
    path('country/create', CountryCreateView.as_view(), name='country-create-view'),
    path('city', CityListView.as_view(), name='city-list-view'),
]
