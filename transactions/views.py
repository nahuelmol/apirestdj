from django.shortcuts import render
from django.views import View

from transactions.models import Transactions, Client

class Monitor(View):

	def get(self,request):
		clients 	= Client.objects.all()
		context 	= {	'example':clients}
		return render(request,'transactions/monitor.html',context)

	def post(self,request,pk=None):
		form = InfoForm(request.POST)
		if form.is_valid():
			amount		= request.POST.get('amount')
			action		= request.POST.get('action')
			sender_id 	= request.POST.get('id_sender')
			destine		= request.POST.get('destine')

			transaction = Transactions(	amount=amount,
										sender_id=sender_id,
										date=date,
										dest_id=destine)

		#making transactions -> get_object