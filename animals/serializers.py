from rest_framework import serializers

from .models import Sex_Options

class AnimalSerializer(serializers.Serializer):
    name = serializers.CharField()
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    sex = serializers.ChoiceField(choices=Sex_Options.choices, default=Sex_Options.DEFAULT)
