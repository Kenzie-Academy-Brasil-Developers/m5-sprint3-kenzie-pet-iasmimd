from numpy import log as ln

from rest_framework import serializers

from .models import Animal, Sex_Options

from groups.models import Group
from groups.serializers import GroupSerializer

from traits.models import Trait
from traits.serializers import TraitSerializer


class AnimalSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    sex = serializers.ChoiceField(
        choices=Sex_Options.choices, default=Sex_Options.DEFAULT
    )

    group = GroupSerializer()
    traits = TraitSerializer(many=True)

    human_age = serializers.SerializerMethodField()

    def get_human_age(self, obj):
        dog_human_age = round(16 * ln(obj.age) + 31)

        return dog_human_age

    def create(self, validated_data: dict) -> Animal:
        group = validated_data.pop("group")
        traits = validated_data.pop("traits")

        group, _ = Group.objects.get_or_create(**group)
        animal = Animal.objects.create(**validated_data, group=group)

        for trait in traits:
            t, _ = Trait.objects.get_or_create(**trait)
            animal.traits.add(t)

        return animal

    def update(self, instance: Animal, validated_data: dict) -> Animal:
        forbidden_keys = (
            "traits",
            "group",
            "sex",
        )

        for key, value in validated_data.items():
            if key in forbidden_keys:
                raise KeyError(key)

            setattr(instance, key, value)

        instance.save()

        return instance
