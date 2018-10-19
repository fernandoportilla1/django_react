from django.db import models

# Create your models here.


class Country(models.Model):
    name = models.CharField('Name', max_length=50)

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey(
        Country, related_name='cities', null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField('Name', max_length=50)
    prefix = models.CharField('Prefix', max_length=50)

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"

    def __str__(self):
        return '{} {}'.format(self.name, self.prefix)
