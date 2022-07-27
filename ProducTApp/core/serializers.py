from rest_framework.serializers import ModelSerializer
from core.models import Product, Order, CsvFile


class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'


class CsvFileSerializer(ModelSerializer):

    class Meta:
        model = CsvFile
        fields = '__all__'
