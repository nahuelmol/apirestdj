from transactions.models import Client, Transaction
from django.forms import ModelForm


class ClientForm(UserCreationForm):
	
	class Meta:
		model = Client
		fields = ['username','email']



class TransactionForm(UserCreationForm):

	class Meta:
		model = Transaction
		fields = ['username','email']
