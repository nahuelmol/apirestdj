from django.contrib import admin
from transactions.models import Transaction, Client

admin.site.register(Transaction)
admin.site.register(Client)
