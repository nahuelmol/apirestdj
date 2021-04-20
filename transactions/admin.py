from django.contrib import admin
from transactions.models import Transactions, Client

admin.site.register(Transactions)
admin.site.register(Client)
