from django.contrib import admin
from django.urls import path, include

import snippet.api.urls



urlpatterns = [
	path('api-auth/',include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('api/',include('snippet.api.urls',namespace='apirest')),
]
