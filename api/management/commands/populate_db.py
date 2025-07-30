from decimal import Decimal

from django.core.management.base import BaseCommand
from api.models import User, Comprobante, Item

class Command(BaseCommand):
    help = 'Inicializa la base de datos con algunos comprobantes e items'

    def handle(self, *args, **kwargs):
        # get or create superuser
        user = User.objects.filter(username='admin').first()
        if not user:
            user = User.objects.create_superuser(username='admin', password='test')

        comprobante = Comprobante.objects.create(
            nombre="compra 1",
            user = user
        )
                
                
        items = [
            Item(nombre="YERBA MATE PRIMICIA", precio=Decimal('1500.24'), categoria=Item.CategoryChoices.ALIMENTOS, comprobante=comprobante),
            Item(nombre="FIDEOS FAVORITA", precio=Decimal('780.24'), categoria=Item.CategoryChoices.ALIMENTOS, comprobante=comprobante),
            Item(nombre="POLENTA POLENTINI", precio=Decimal('400.66'), categoria=Item.CategoryChoices.ALIMENTOS, comprobante=comprobante),
            Item(nombre="CEPITA NARANJA 3L", precio=Decimal('2200.24'), categoria=Item.CategoryChoices.BEBIDAS, comprobante=comprobante),
            Item(nombre="COLGATE TOTAL 12", precio=Decimal('2000.00'), categoria=Item.CategoryChoices.CUIDADO_PERSONAL, comprobante=comprobante)
        ]

        Item.objects.bulk_create(items)

