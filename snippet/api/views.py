from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from rest_framework import viewsets
from rest_framework import generics

from rest_framework.decorators import api_view, schema
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema

from django.contrib.auth.models import User
from snippet.models import Friends, Languages, CountriesSpeakers
from snippet.models import Pets, Customers

from .serializers import UserSerializer, pet_serializer, customer_serializer
from .serializers import friends_serializer, LanguagesSerializer, CountriesSerializer

class CustomAutoSchema(AutoSchema):
    def get_link(self, path, method, base_url):
        print(method)
        print(base_url)


@api_view(['GET'])
@schema(CustomAutoSchema())
def example_view(request):
    return Response({"message": "Hello for today! See you tomorrow!"})

@api_view(['GET','POST'])
def Pet_VS(request):

    if request.method == 'GET':
        pets        = Pets.objects.all()
        serializer  = pet_serializer(pets, many=True)
        queryset    = serializer.data
        return Response(queryset)

    if request.method == 'POST':
        content     = {"message": "Got some data!", "data": request.data}
        return Response(content)


@api_view(['GET'])
def apiOverview(request):
    api_urls = {"message": "Hello, world!"}
    return Response(api_urls)

class CustomerViewSet(viewsets.ViewSet):
    
    @staticmethod
    def list(self):
        queryset        = Customers.objects.all()
        serializer      = customer_serializer(queryset, many=True)
        return Response(serializer.data) 

    @staticmethod
    def retrieve(self,pk=None):
        queryset    = Customers.objects.all()
        customer    = get_object_or_404(queryset, pk=pk)
        serializer  = customer_serializer(customer)
        return Response(serializer.data)

class UserViewSet(viewsets.ModelViewSet):
    queryset            = User.objects.all().order_by('-date_joined')
    serializer_class    = UserSerializer

class FriendsViewSet(viewsets.ModelViewSet):
	queryset           = Friends.objects.all()
	serializer_class   = friends_serializer

class LanguagesViewSet(viewsets.ModelViewSet):
    queryset            =Languages.objects.all()
    serializer_class    =LanguagesSerializer

class CountriesViewSet(viewsets.ModelViewSet):
    queryset            =CountriesSpeakers.objects.all()
    serializer_class    =CountriesSerializer
