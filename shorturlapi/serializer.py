from rest_framework.serializers import ModelSerializer
from .models import link

class linkSerializer(ModelSerializer):
    class Meta:
        model=link
        fields='__all__'