from rest_framework import serializers
from . models import mobiles

class mobilesSerializer(serializers.ModelSerializer):

    class Meta:
        model=mobiles

        fields='__all__'