from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from . models import mobiles
from . serializers import mobilesSerializer



class mobileList(APIView):

    def get(self, request):
        mobiles1 = mobiles.objects.all()
        serializer = mobilesSerializer(mobiles1, many=True)
        return Response(serializer.data)

    def post(self, request):
        mobiles_data = JSONParser().parse(request)
        mobile_serializer = mobilesSerializer(data=mobiles_data)
        if mobile_serializer.is_valid():
            mobile_serializer.save()
            return Response(mobile_serializer.data, status=status.HTTP_201_CREATED)
        return Response(mobile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        count = mobiles.objects.all().delete()
        return Response({'message': '{} mobiles deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


