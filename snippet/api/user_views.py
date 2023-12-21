from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.utils import timezone

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from rest_framework.views import APIView
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, schema
from rest_framework.response import Response
from rest_framework import permissions, generics, authentication
from rest_framework import serializers

from snippet.forms import UserCreator

from snippet.utils import generate_access_token
from snippet.api.serializers import UserSerializer



#login, logout and register views

class UserRegisterView(APIView):

	serializer_class = UserSerializer
	authentication_classes = [authentication.TokenAuthentication]
	permission_classes = [permissions.AllowAny]

	def get(self, request):
		pass

	
	def post(self, request):
		form = UserCreator(request.data)
		print(request.data) 

		if form.is_valid():
			new_user = form.save()

			if new_user:
				access_token = generate_access_token(new_user)
				data = {'access_token':access_token}
				response = Response(data, status=status.HTTP_201_CREATED)
				response.set_cookie(key='access_token', value=access_token)
				return response

		return Response(form.errors, status=status.HTTP_400_BAD_REQUEST, content_type='application/json')


class UserLoginView(APIView):

	def post(self, request):
		username = request.data.get('username', '')
		password = request.data.get('password', '')

		user = authenticate(request, username=username, password=password)

		if user:

			login(request, user)
			session_token = generate_access_token(user)

			session, created = Session.objects.get_or_create(session_key=session_token,
				defaults={'expire_date': timezone.now() + timezone.timedelta(days=1)})

			data = {'session_token': session_token}
			response = Response(data, status=status.HTTP_201_CREATED)
			response.set_cookie(key='session_token', value=session_token, httponly=True)

			return response
		else:
			return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class UserLogoutView(APIView):

	def post(self, request):

		data = {'message':'logout succesful'}
		response = Response(data, status=status.HTTP_201_CREATED)
		response.delete_cookie('access_token')

		return response
