from rest_framework import serializers
from .models import Comprobante, Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = (
            'id',
            'nombre',
            'precio',
            'categoria',
            'comprobante'
        )

class ComprobanteSerializer(serializers.ModelSerializer):
    Items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Comprobante
        fields = (
            'id',
            'nombre',
            'created_at',
            'user',
            'Items'
        )

    

