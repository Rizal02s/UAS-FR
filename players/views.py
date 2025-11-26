from rest_framework import viewsets
from rest_framework.permissions import AllowAny # UBAH DARI IsAuthenticated ke AllowAny
from rest_framework.filters import SearchFilter, OrderingFilter 
from django_filters.rest_framework import DjangoFilterBackend 
from .models import Pemain
from .serializers import PemainSerializer

class PemainViewSet(viewsets.ModelViewSet):
    queryset = Pemain.objects.all()
    serializer_class = PemainSerializer
    
    # KUNCI PERBAIKAN: Izinkan akses publik untuk POST/GET/PUT/DELETE
    permission_classes = [AllowAny] 
    
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['country', 'position'] 
    search_fields = ['name', 'country'] 
    ordering_fields = ['salary', 'age', 'player_number']