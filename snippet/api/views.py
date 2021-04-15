from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib.auth.models import User

<<<<<<< HEAD
from snippet.models import whoever, Pets
from .serializers import UserSerializer, whoever_serializer, pet_serializer

=======
from snippet.models import mymodel, Customer
from .serializers import UserSerializer, mymodel_serializer
from .serializers import CustomerSerializer
>>>>>>> 09c12cbeb971595e7cb09aa40020a3eae11dd084

# Here, the objects from the models and the functions serializers are puted together on views

class CustomerViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Customer.objects.all()
        serializer = CustomerSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Customer.objects.all()
        customer = get_object_or_404(queryset, pk=pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

class UserViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    # we can use the next method instead of queryset
    # def get_queryset(self):
        # return self.request.user.accounts.all()


<<<<<<< HEAD
class WhoeverViewSet(viewsets.ModelViewSet):
	queryset = whoever.objects.all()
	serializer_class = whoever_serializer

class Pet_VS(viewsets.ModelViewSet):
	queryset = Pets.objects.all()
	serializer_class = pet_serializer
=======
class SomethingViewSet(viewsets.ModelViewSet):
	queryset = mymodel.objects.all()
	serializer_class = mymodel_serializer
>>>>>>> 09c12cbeb971595e7cb09aa40020a3eae11dd084

