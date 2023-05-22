from django.urls import path
from api.views import UserProfileRegisterView, UserProfileLoginView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserProfileRegisterView.as_view(), name='user-register'),
    path('login/', UserProfileLoginView.as_view(), name='user-login'),
]