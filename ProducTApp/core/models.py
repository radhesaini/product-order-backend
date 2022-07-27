from datetime import datetime
from itertools import product
from django.db import models
from django.conf import settings
from .helper import PrivateApkStorage, apk_directory_path
from .basemodel import Base

# Create your models here.
class Order(Base):
    custumer_name = models.CharField(max_length=255)
    products = models.JSONField(null=False, default=dict)
    total_amount = models.BigIntegerField(null=False)

    class Meta:
        managed = True
        db_table = 'order'


class Product(Base):
    product_name = models.CharField(max_length=255, null=False, unique=True)
    price = models.BigIntegerField(null=False, unique=False, default=0)

    class Meta:
        managed = True
        db_table = 'product'


class CsvFile(Base):
    name = models.CharField(max_length=255)
    source = models.FileField(upload_to='products/')