from rest_framework import serializers
from .models import Corporation

class CorporationSerializer(serializers.Serializer):
    legal_name = serializers.CharField(max_length=255)


class CorporationModelSerializer(serializers.ModelSerializer):
    legal_name = serializers.CharField(max_length=255, allow_null=True, allow_blank=True, required=False)

    class Meta:
        model = Corporation
        fields = '__all__'