from django.urls import path
from transactions.views import Monitor 

urlpatterns = [	path('monitor/',Monitor.as_view(),name='monitor')
]