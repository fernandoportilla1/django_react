from datetime import datetime, time

from django.db import models


# Create your models here.


class Country(models.Model):
    name = models.CharField('Name', max_length=50)
    date = models.DateField('Date', null=True, blank=True)
    time = models.TimeField('Time', null=True, blank=True)
    is_available = models.BooleanField("Pico y Placa?", db_column="can_drive", default=False)

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.name

    @property
    def can_drive(self):
        _date = datetime.strptime(str(self.date), "%Y-%m-%d").weekday()
        _time = self.time
        checker = self.name[-1]

        if time(7, 00, 00) <= _time <= time(9, 30, 00) or time(14, 00, 00) <= _time <= time(19, 30, 00):
            if _date == 0 and (checker == '1' or checker == '2'):
                return False
            if _date == 1 and (checker == '3' or checker == '4'):
                return False
            if _date == 2 and (checker == '5' or checker == '6'):
                return False
            if _date == 3 and (checker == '7' or checker == '8'):
                return False
            if _date == 4 and (checker == '9' or checker == '0'):
                return False
        return True


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
