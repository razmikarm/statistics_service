from rest_framework import serializers
from .models import Statistics


class PostStatisticsSerializer(serializers.ModelSerializer):

    date = serializers.DateField(format='%Y-%m-%d')
    cost = serializers.FloatField(min_value=0, required=False, write_only=True)

    class Meta:
        model = Statistics
        fields = (
            "date",
            "views",
            "clicks",
            "cost"
        )

    def validate_cost(self, value):
        if len(str(value).split('.')[1]) > 2:
            raise serializers.ValidationError("Set no more than 2 numbers after the floating point")
        return round(value * 100)

    def create(self, validated_data):
        instance, created = Statistics.objects.get_or_create(
            date=validated_data['date'],
            defaults={**validated_data}
        )

        if not created:
            for key, value in validated_data.items():
                if key == 'date':
                    continue
                value += getattr(instance, key)
                setattr(instance, key, value)
        instance.save()
        return instance

class GetStatisticsSerializer(serializers.ModelSerializer):

    date = serializers.DateField(format='%Y-%m-%d')
    cost = serializers.SerializerMethodField()
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

    def get_cost(self, obj):
        return obj.cost / 100
