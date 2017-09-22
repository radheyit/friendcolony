from django.conf.urls import url
from user_mgmt.views import login_api
from rest_framework_jwt.views import obtain_jwt_token
from user_mgmt.views import registration_api

urlpatterns = [
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^login_api', login_api, name='Login'),
    url(r'^registration_api/(?P<pk>[0-9]+)$', registration_api, name='registration'),
	
]
