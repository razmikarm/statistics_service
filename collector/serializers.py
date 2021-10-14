from rest_framework import serializers
from .models import Statistics


class StatisticsSerializer(serializers.ModelSerializer):

    cost = serializers.FloatField(min_value=0, required=False)
    cpc = serializers.FloatField(read_only=True)
    cpm = serializers.FloatField(read_only=True)

    class Meta:
        model = Statistics
        fields = (
            "date",
            "views",
            "clicks",
            "cost",
            "cpc",
            "cpm",
        )

    # def validate_cost(self, value):
    #     return int(value * 100)

    def create(self, validated_data):
        instance, created = Statistics.objects.get_or_create(
            date=validated_data['date'],
            defaults={
                **validated_data
            }
        )

        if not created:
            for key, value in validated_data.items():
                if key == 'date':
                    continue
                setattr(instance, key, getattr(instance, key) + value)
        instance.save()
        return instance
