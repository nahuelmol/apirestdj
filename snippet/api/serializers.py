from rest_framework import serializers
from django.contrib.auth.models import User
<<<<<<< HEAD
from snippet.models import whoever, Pets
=======
from snippet.models import mymodel, Customer
>>>>>>> 09c12cbeb971595e7cb09aa40020a3eae11dd084

# Here is where the models are converted with the serializer class

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
    	model = User
    	fields = ('id','username','email')

<<<<<<< HEAD
class whoever_serializer(serializers.ModelSerializer):
	class Meta:
		model = whoever
		fields = '__all__'

class pet_serializer(serializers.ModelSerializer):

	class Meta: 
		model = Pets
		fields = '__all__'
=======
class mymodel_serializer(serializers.ModelSerializer):
    class Meta:
        model = mymodel
	fields = '__all__'

class customer_serializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
>>>>>>> 09c12cbeb971595e7cb09aa40020a3eae11dd084
