from django.urls import path
from . import views

urlpatterns = [
    path('comprobantes/', views.ComprobanteListCreateAPIView.as_view()),
    path('comprobantes/<int:pk>/', views.ComprobanteDetailAPIView.as_view()),
    path('items/', views.ItemListCreateAPIView.as_view()),
    path('items/<int:pk>/', views.ItemDetailAPIView.as_view())
]