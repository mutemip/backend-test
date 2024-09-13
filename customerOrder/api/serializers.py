from rest_framework import serializers
from customerOrder.models import Customer,Order


class OrderSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Order
        fields = '__all__'

    def get_total(self, obj):
        quantity = obj.quantity
        price = obj.price
        return quantity * price
    
class CustomerSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(many=True, read_only=True)
    class Meta:
        model = Customer
        fields = '__all__'