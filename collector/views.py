from rest_framework import viewsets, mixins

from .filters import StatisticFilter
from .models import Statistics
from .serializers import StatisticsSerializer


class StatisticsViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):

    queryset = Statistics.objects.all()
    serializer_class = StatisticsSerializer

    filterset_class = StatisticFilter

