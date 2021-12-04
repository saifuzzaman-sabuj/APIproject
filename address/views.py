from django.http import Http404
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Address
from .serializer import AddressSerializer
from django.shortcuts import render

# Create your views here.
class AddressList(APIView):

    def get(self, request):
        address = Address.objects.all()
        serializer = AddressSerializer(address, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

class AddressPost(APIView):

    def post(self, request, format=None):
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddressDetail(APIView):

    def get_object(self, pk):
        # Returns an object instance that should
        # be used for detail views.
        try:
            return Address.objects.get(pk=pk)
        except Address.DoesNotExist:
            raise Http404

    def delete(self, request, pk, format=None):
        address = self.get_object(pk)
        address.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AddressUpdate(APIView):

    def get_object(self, pk):
        # Returns an object instance that should
        # be used for detail views.
        try:
            return Address.objects.get(pk=pk)
        except Address.DoesNotExist:
            raise Http404

    def patch(self, request, pk, format=None):
        Address = self.get_object(pk)
        serializer = AddressSerializer(Address,
                                           data=request.data,
                                           partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddressSearch(generics.ListCreateAPIView):
    queryset = Address.objects.all()

    serializer_class = AddressSerializer

    name = 'address-list'

    filter_fields = (

        "zip",


    )




