from rest_framework import serializers
from django.contrib.auth.models import User
from snippet.models import Friends, Languages, CountriesSpeakers
from snippet.models import Pets, Customers


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
    	model  = User
    	fields = ('id','username','email')

class friends_serializer(serializers.ModelSerializer):
    class Meta:
        model   = Friends
        fields  = '__all__'

class pet_serializer(serializers.ModelSerializer):

	class Meta: 
		model     = Pets
		fields    = '__all__'

class customer_serializer(serializers.ModelSerializer):
    class Meta:
        model   = Customers
        fields  = '__all__'


class LanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Languages
        fields  ='__all__'

class CountriesSerializer(serializers.ModelSerializer):
    class Meta:
        model   = CountriesSpeakers
        fields  ='__all__'