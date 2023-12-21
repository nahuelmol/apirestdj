from .serializer import ClientSerializer, TransactionSerializer

from rest_framework.views import APIView
from rest_framework import permissions, generics, authentication
from rest_framework.response import Response
from rest_framework import status

class MakeClient(APIView):

	serializer_class = ClientSerializer
	authentication_classes = [authentication.TokenAuthentication]
	permission_classes = [permissions.AllowAny]

	def get(self, request):
		pass

	def post(self, request):
		# Include the owner (logged-in user) in the data before serializing
		request.data['owner'] = request.user.id
		serializer 	= ClientSerializer(data=request.data)

		if serializer.is_valid():
			new_client = serializer.save()

			if new_client:
				access_token = generate_access_token(new_client)
				data = {'access_token':access_token}
				response = Response(data, status=status.HTTP_201_CREATED)
				response.set_cookie(key='access_token', value=access_token)
				return response

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST, content_type='application/json')

class MakeTransaction(APIView):

	serializer_class = TransactionSerializer
	authentication_classes = [authentication.TokenAuthentication]
	permission_classes = [permissions.AllowAny]

	def get(self, request):
		pass

	def post(self, request):
		serializer = TransactionSerializer(request.data)

		if serializer.is_valid():

			new_transaction = serializer.save()

			if new_transaction:
				access_token = generate_access_token(new_client)
				data = {'access_token':access_token}
				response = Response(data, status=status.HTTP_201_CREATED)
				response.set_cookie(key='access_token', value=access_token)
				return response

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST, content_type='application/json')