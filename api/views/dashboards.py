
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from api.models.dashboards import Dashboard
from api.serializers.dashboards import DashboardSerializer


class DashboardViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = DashboardSerializer
    queryset = Dashboard.objects.all()
                  

