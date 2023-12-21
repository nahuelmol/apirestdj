from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers

from .views import MakeClient, MakeTransaction

app_name = 'transactionapi'


urlpatterns = [
	path('addclient/', 	MakeClient.as_view(), 		name='client-make'),
	path('addtransc/', 	MakeTransaction.as_view(), 	name='transaction-make')
]


