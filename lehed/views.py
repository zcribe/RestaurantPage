from django.views.generic import ListView
from lehed.models import MenuItemCategory


class IndexView(ListView):
    model = MenuItemCategory
    template_name = 'index.html'
