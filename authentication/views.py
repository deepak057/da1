from rest_framework import permissions, viewsets
from authentication.models import Account
from authentication.permissions import IsAccountOwner
from authentication.serializers import AccountSerializer

class AccountViewSet(viewsets.ModelViewSet):