from rest_framework import serializers
from .models import Taxpayer,Business,Receipt
import time


class TaxpayerSerializer(serializers.ModelSerializer):
        class Meta:
            model = Taxpayer
            fields = '__all__'


class BusinessSerializer(serializers.ModelSerializer):
         class Meta:
            model = Business
            fields = ['business_type','tin','taxpayer_id'] 

class ReceiptSerializer(serializers.ModelSerializer):
        class Meta:
              model = Receipt
              fields = '__all__'