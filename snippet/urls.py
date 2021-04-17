from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .api.views import Pet_VS, apiOverview, example_view, CustomerViewSet

urlpatterns = [
    path('snippets/',apiOverview),
    path('pets/',Pet_VS),
    path('example/', example_view),
    path('customer/',CustomerViewSet)
]

