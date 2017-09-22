from django.conf.urls import url,include
from django.contrib import admin
from user_mgmt.views import login_api
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user/', include('user_mgmt.urls')),
    url(r'^login_api/',login_api),
    url(r'^api-token-auth/', obtain_jwt_token),
]
