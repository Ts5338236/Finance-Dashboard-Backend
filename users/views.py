from rest_framework import viewsets, permissions
from .models import User
from .serializers import UserSerializer, UserCreateSerializer
from .permissions import IsAdmin

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    Only accessible by Admin role.
    """
    queryset = User.objects.all().order_by('-date_joined')
    permission_classes = [IsAdmin]

    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        return UserSerializer
