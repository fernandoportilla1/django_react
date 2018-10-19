from rest_framework import viewsets
from apps.countries.api.serializers import CountrySerializer, CitySerializer
from apps.countries.models import Country, City


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
