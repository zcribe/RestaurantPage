from django.db import models


class MenuItemCategory(models.Model):
    title = models.CharField(max_length=200)
    image_side = models.ImageField(default='#')

    def __str__(self):
        return self.title


class MenuItem(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(MenuItemCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Address(models.Model):
    street = models.CharField(max_length=128)
    state = models.CharField(max_length=128)
    country = models.CharField(max_length=128)
    index = models.PositiveIntegerField()
    latitude = models.DecimalField(max_digits=20, decimal_places=10)
    longitude = models.DecimalField(max_digits=20, decimal_places=10)

    def __str__(self):
        return f"{self.street}, {self.state}, {self.country}, {self.index}"


class Location(models.Model):
    title = models.CharField(max_length=200)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
