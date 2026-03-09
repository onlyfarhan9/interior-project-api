from rest_framework import serializers
from api.models import Furniture_Details


class Furniture_DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Furniture_Details
        fields = (
            "src",
            "title",
            "category"
        )

