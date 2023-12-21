from rest_framework import serializers
from transactions.models import Client, Transaction

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
    	model = Client
    	fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
    	model = Transaction
    	fields = '__all__' 