import django_filters as filters
from .models import Statistics


class StatisticFilter(filters.FilterSet):

    date = filters.DateFromToRangeFilter(field_name='date')

    class Meta:
        model = Statistics
        fields = ('date',)
