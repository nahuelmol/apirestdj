from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers

<<<<<<< HEAD
from .views import UserViewSet, WhoeverViewSet, Pet_VS

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'user_data', UserViewSet)
router.register(r'whoever_data', WhoeverViewSet)
router.register(r'thats_pets_data', Pet_VS)
=======
from .views import UserViewSet, SomethingViewSet
from .views import CustomerViewSet

router = routers.DefaultRouter()

router.register(r'thats_users_data', UserViewSet)
router.register(r'data_prove', SomethingViewSet)
router.register(r'customer_db_prove',CustomerViewSet)
>>>>>>> 09c12cbeb971595e7cb09aa40020a3eae11dd084

# urlpatterns = [
# 	path('', include(router.urls))
# ]

urlpatterns = router.urls
