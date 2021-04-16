from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import viewsets

from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.contrib.auth.models import User
from snippet.models import Friends, Languages, CountriesSpeakers
from snippet.models import Pets, Customer

from .serializers import UserSerializer, pet_serializer, customer_serializer
from .serializers import friends_serializer, LanguagesSerializer, CountriesSerializer

@api_view(['GET'])
def Pet_VS(request):
    pets        = Pets.objects.all()
    serializer  = pet_serializer(pets, many=True)
    return Response(serializer)

@api_view(['GET'])
def apiOverview(req):
    api_urls = {
        'List':'/task-list/',
        'Detail View':'/task-detail/<str:pk>'
    }
    return Response(api_urls)

class CustomerViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset    = Customer.objects.all()
        serializer  = CustomerSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset    = Customer.objects.all()
        customer    = get_object_or_404(queryset, pk=pk)
        serializer  = CustomerSerializer(customer)
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
