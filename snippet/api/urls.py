from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers

from .views import UserViewSet, Pet_VS, CustomerViewSet
from .views import FriendsViewSet, LanguagesViewSet, CountriesViewSet  

app_name = 'apirest'

router = routers.DefaultRouter(trailing_slash=False)
#router = routers.SimpleRouter()

router.register(r'user_data', 		UserViewSet)
router.register(r'friends_data', 	FriendsViewSet)
router.register(r'languages', 		LanguagesViewSet)
router.register(r'countries', 		CountriesViewSet)

#router.register(r'thats_pets_data', Pet_VS, basename='pets')
#router.register(r'overview',apiOverview, basename='apiOverview')
#router.register(r'customer_db_prove',CustomerViewSet,basename='costumer')

urlpatterns = router.urls
