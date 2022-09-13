from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Corporation
from .serializers import CorporationSerializer, CorporationModelSerializer

def index(request):
    result = ""
    for corporation in Corporation.objects.all():
        result += f"{corporation.legal_name} -"
    return HttpResponse(result)


class ListCorporation(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        corporations = Corporation.objects.all()
        serializer = CorporationModelSerializer(corporations, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = CorporationModelSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            Corporation.objects.create(**serializer.validated_data)
            return Response(status=status.HTTP_201_CREATED)


class CorporationViewSet(viewsets.ModelViewSet):
    serializer_class = CorporationModelSerializer
    queryset = Corporation.objects.all()
    permission_classes = [AllowAny]
