from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers

from .views import UserViewSet, Pet_VS, CustomerViewSet
from .views import FriendsViewSet, LanguagesViewSet, CountriesViewSet  

from .user_views import UserRegisterView, UserLoginView, UserLogoutView

app_name = 'apirest'

router = routers.SimpleRouter()

#these are utls related with user authentication, authorization

router.register(r'user_data', 		UserViewSet)
router.register(r'friends_data', 	FriendsViewSet)
router.register(r'languages', 		LanguagesViewSet)
router.register(r'countries', 		CountriesViewSet)
router.register(r'customer',		CustomerViewSet,basename='costumer')

urlpatterns = [
	path('register/', 	UserRegisterView.as_view(), name='user-register'),
	path('login/', 		UserLoginView.as_view(), 	name='user-login'),
	path('logout/',		UserLogoutView.as_view(), 	name='user-logout')
]

urlpatterns += router.urls
