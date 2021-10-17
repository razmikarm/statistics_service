from rest_framework import viewsets, mixins, status
from rest_framework.response import Response

from .filters import StatisticFilter
from .models import Statistics
from .serializers import PostStatisticsSerializer, GetStatisticsSerializer


class StatisticsViewSet(mixins.DestroyModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):

    queryset = Statistics.objects.all()
    serializer_class = GetStatisticsSerializer
    filterset_class = StatisticFilter

    def get_serializer_class(self):
        if self.action == 'create':
            return PostStatisticsSerializer
        return super(StatisticsViewSet, self).get_serializer_class()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        resp = GetStatisticsSerializer(instance)
        return Response(resp.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        self.perform_destroy(self.queryset)
        return Response(status=status.HTTP_204_NO_CONTENT)
