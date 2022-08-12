from django.test import TestCase

from animals.models import Animal
from groups.models import Group
from traits.models import Trait


class AnimalTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.name = "Beethoven"
        cls.age = 1
        cls.weight = 30
        cls.sex = "Macho"
        cls.group = {"name": "Cão", "scientific_name": "Canis familiaris"}
        cls.traits = [{"name": "Peludo"}]

        cls.animal_1_data = {
            "name": "Beethoven",
            "age": 1,
            "weight": 30,
            "sex": "Macho",
            "group": {"name": "Cão", "scientific_name": "Canis familiaris"},
            "traits": [{"name": "Peludo"}],
        }

        cls.group_1_data = {"name": "Cão", "scientific_name": "Canis familiaris"}
        cls.group_1 = Group.objects.create(**cls.group_1_data)

        cls.animal_1 = Animal.objects.create(
            name=cls.name,
            age=cls.age,
            weight=cls.weight,
            sex=cls.sex,
            group=cls.group_1,
        )

        cls.traits_1_data = {"name": "Peludo"}
        cls.traits_1_ = Trait.objects.create(**cls.traits_1_data)

    def test_name_max_length(self):
        expected_max_length = 50
        result_max_length = self.animal_1._meta.get_field("name").max_length

        self.assertEqual(result_max_length, expected_max_length)

    def test_animal_fields(self):
        for trait in self.traits:
            animal = Animal.objects.get(id=1)
            trait_item, _ = Trait.objects.get_or_create(**trait)
            animal.traits.add(trait_item)

        self.assertEqual(self.animal_1.name, self.animal_1_data["name"])
        self.assertEqual(self.animal_1.age, self.animal_1_data["age"])
        self.assertEqual(self.animal_1.weight, self.animal_1_data["weight"])
        self.assertEqual(self.animal_1.sex, self.animal_1_data["sex"])
        self.assertEqual(self.animal_1.group.name, self.animal_1_data["group"]["name"])
        self.assertEqual(
            self.animal_1.traits.count(), len(self.animal_1_data["traits"])
        )

    def test_relation_animal_with_group(self):
        self.assertEqual(self.animal_1.group.name, self.animal_1_data["group"]["name"])

    def test_relation_animal_with_traits(self):
        for trait in self.traits:
            animal = Animal.objects.get(id=1)
            trait_item, _ = Trait.objects.get_or_create(**trait)
            animal.traits.add(trait_item)

        self.assertEqual(
            self.animal_1.traits.count(), len(self.animal_1_data["traits"])
        )
