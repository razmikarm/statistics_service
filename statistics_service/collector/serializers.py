from rest_framework import serializers
from models import Statistics


class StatisticsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Statistics
        fields = "__all__"
