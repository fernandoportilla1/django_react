from django.test import TestCase

from apps.countries.models import Country


# Create your tests here.

class BeerTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        Country.objects.create(name="PAC-121", date='2018-10-22', time='7:00:00')
        Country.objects.create(name="PAC-121", date='2018-10-22', time='9:30:00')
        Country.objects.create(name="PAC-121", date='2018-10-22', time='6:59:59')
        Country.objects.create(name="PAC-121", date='2018-10-22', time='9:30:01')
        Country.objects.create(name="PAC-121", date='2018-10-22', time='14:00:00')
        Country.objects.create(name="PAC-121", date='2018-10-22', time='19:30:00')
        Country.objects.create(name="PAC-121", date='2018-10-22', time='13:59:59')
        Country.objects.create(name="PAC-121", date='2018-10-22', time='19:30:01')
        Country.objects.create(name="PAC-123", date='2018-10-22', time='7:00:00')

    def test_can_drive_1(self):
        country = Country.objects.get(pk=1)
        self.assertEqual(country.can_drive, False)

    def test_can_drive_2(self):
        country = Country.objects.get(pk=2)
        self.assertEqual(country.can_drive, False)

    def test_can_drive_3(self):
        country = Country.objects.get(pk=3)
        self.assertEqual(country.can_drive, True)

    def test_can_drive_4(self):
        country = Country.objects.get(pk=4)
        self.assertEqual(country.can_drive, True)

    def test_can_drive_5(self):
        country = Country.objects.get(pk=5)
        self.assertEqual(country.can_drive, False)

    def test_can_drive_6(self):
        country = Country.objects.get(pk=6)
        self.assertEqual(country.can_drive, False)

    def test_can_drive_7(self):
        country = Country.objects.get(pk=7)
        self.assertEqual(country.can_drive, True)

    def test_can_drive_8(self):
        country = Country.objects.get(pk=8)
        self.assertEqual(country.can_drive, True)

    def test_can_drive_9(self):
        country = Country.objects.get(pk=9)
        self.assertEqual(country.can_drive, True)
