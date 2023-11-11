from django.urls import path
from .views import GetAccessToken

urlpatterns = [
    path('get-access-token/', GetAccessToken.as_view(), name='get-access-token'),
]