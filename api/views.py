from django.shortcuts import render
from api.serializers import ItemSerializer, ComprobanteSerializer
from api.models import Comprobante, Item
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class ComprobanteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comprobante.objects.prefetch_related('Items')
    serializer_class = ComprobanteSerializer

    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)


class ComprobanteDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ComprobanteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Comprobante.objects.filter(user=self.request.user).prefetch_related('Items')


class ItemListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Item.objects.filter(comprobante__user=self.request.user)
    

class ItemDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Item.objects.filter(comprobante__user=self.request.user)