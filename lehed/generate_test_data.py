from .models import MenuItemCategory, MenuItem
from mimesis import Food, Business
from random import randint


def generate_menu():
    g = Food('et')
    b = Business('et')
    for _ in range(7):
        cat = MenuItemCategory()
        cat.title = g.dish()
        cat.save()
        for _ in range(10):
            m = MenuItem()
            m.title = g.dish()
            m.price = randint(2, 9)
            m.category = cat
            m.save()
