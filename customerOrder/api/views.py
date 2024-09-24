from customerOrder.api.serializers import CustomerSerializer, OrderSerializer
from rest_framework import generics
from customerOrder.models import Customer, Order
from rest_framework.permissions import IsAuthenticated


class CustomerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Customer.objects.all().order_by('-id')
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]


class OrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all().order_by('-id')
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

