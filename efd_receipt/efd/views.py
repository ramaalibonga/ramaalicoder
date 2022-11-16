from rest_framework import viewsets
from .models import Taxpayer,Business,Receipt
from .serializer import TaxpayerSerializer,BusinessSerializer,ReceiptSerializer


class TaxpayerViewSet(viewsets.ModelViewSet):
    queryset = Taxpayer.objects.all()
    serializer_class = TaxpayerSerializer



class BusinessViewSet(viewsets.ModelViewSet):
    queryset = Business.objects.select_related('taxpayer_id')
    serializer_class = BusinessSerializer

class ReceiptViewSet(viewsets.ModelViewSet):
    queryset = Receipt.objects.select_related('taxpayer_id')
    serializer_class = ReceiptSerializer


