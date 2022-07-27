from calendar import month
from itertools import product
from requests import request
from rest_framework.viewsets import ModelViewSet
from core.serializers import ProductSerializer, OrderSerializer, CsvFileSerializer
from core.models import Product, Order, CsvFile
from rest_framework.parsers import FileUploadParser
from rest_framework.decorators import action
from rest_framework.response import Response 
from rest_framework import status
from datetime import datetime
from dateutil import relativedelta
from csv import reader



class ProductViewSet(ModelViewSet):
    queryset = Product.objects.order_by('pk')
    serializer_class = ProductSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.order_by('pk')
    serializer_class = OrderSerializer

    @action(methods=["GET"], detail=False)
    def gethistory(self, request, *args, **kwargs):
        months = int(request.query_params["months"])
        serializer =ProductSerializer(Order.objects.filter(
            created_date__gte=datetime.today() - relativedelta.relativedelta(
                months=months)), many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        data = request.data
        amount = 0
        for item in data['products']:
            print(item)
            current_product = Product.objects.get(product_name=item)
            quantity = data['products'][item] 
            amount += current_product.price * quantity
        data["total_amount"] = amount
        serializer = OrderSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data="Your Order has been Successfully completed", status=status.HTTP_201_CREATED)

class CsvFileViewSet(ModelViewSet):
    # parser_classes = (FileUploadParser,)
    queryset = CsvFile.objects.order_by('pk')
    serializer_class = CsvFileSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        with open(serializer.data['source'].replace("http://127.0.0.1:8000", '.'), mode ='r')as file:
            # reading the CSV file
            csvFile = reader(file)
            # displaying the contents of the CSV file
            for line in csvFile:
                if line[0] == "name":
                    continue
                print("--------------------",line)
                product, created = Product.objects.get_or_create(
                    product_name=line[0])
                print(created)
                product.price = line[1]
                product.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
