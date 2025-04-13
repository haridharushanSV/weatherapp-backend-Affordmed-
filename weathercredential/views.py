from rest_framework import viewsets
from .models import data
from  .serializers import dataSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

class dataViewSet(viewsets.ModelViewSet):
    queryset=data.objects.all()
    serializer_class=dataSerializer

@api_view(['GET'])
def get_users(request):
    users = data.objects.all()
    serializer = DataSerializer(users, many=True)
    return Response(serializer.data)