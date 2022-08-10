from django.db import models

from django.db import models


class Sex_Options(models.TextChoices):
    FEMALE = "Femea"
    MALE = "Macho"
    DEFAULT = "Não informado"


class Animal(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    weight = models.FloatField()
    sex = models.CharField(
        max_length=15, choices=Sex_Options.choices, default=Sex_Options.DEFAULT
    )

    group = models.ForeignKey(
        "groups.Group", on_delete=models.CASCADE, related_name="animals"
    )

    traits = models.ManyToManyField("traits.Trait", related_name="animals")

    def __repr__(self) -> str:
        return f"Animal {self.id} - {self.name}"
