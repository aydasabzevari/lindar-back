from rest_framework import generics
from .models import UserProfile
from .serializers import UserProfileSerializer
from djoser.views import UserViewSet


class UserProfileRegisterView(generics.CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserProfileLoginView(generics.RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def get_object(self):
        return self.request.user

class UserProfileViewSet(UserViewSet):
    serializer_class = UserProfileSerializer