from customerOrder.api.serializers import CustomerSerializer, OrderSerializer
from rest_framework import generics
from customerOrder.models import Customer, Order


class CustomerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Customer.objects.all().order_by('-id')
    serializer_class = CustomerSerializer


class OrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all().order_by('-id')
    serializer_class = OrderSerializer

