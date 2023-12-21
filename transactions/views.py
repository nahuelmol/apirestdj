from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from rest_framework import authentication

from transactions.models import Transaction, Client

#@login_required(login_url='/admin/')
class Monitor(View):

	def get(self,request):
		#this shows the transanctions between clients that were created by the current client

		#if request.user.is_authenticated:
		try:
			clients 	= Client.objects.all()

			context 	= {	'example':clients}
			return render(request,'transactions/monitor.html',context)
		except:

			context 	= {	'example':[]}
			return render(request,'transactions/monitor.html',context)
		

	def post(self,request,pk=None):
		form = InfoForm(request.POST)

		user = request.user.username

		if request.user.is_authenticated:

			if form.is_valid():
				amount		= request.POST.get('amount')
				action		= request.POST.get('action')
				sender_id 	= request.POST.get('id_sender')
				destine		= request.POST.get('destine')

				transaction = Transactions(
										amount=amount,
										sender_id=sender_id,
										date=date,
										dest_id=destine)

