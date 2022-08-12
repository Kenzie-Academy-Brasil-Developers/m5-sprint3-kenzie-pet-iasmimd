from django.test import TestCase

from groups.models import Group


class TraitsTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.name = "cão"
        cls.scientific_name = "canis familiaris"


        cls.group_1_data = {"name": "cão", "scientific_name": "canis familiaris"}
        cls.group_1 = Group.objects.create(**cls.group_1_data)

    
    def test_name_max_length(self):
        max_length = self.group_1._meta.get_field("name").max_length

        self.assertEqual(max_length, 20)


    def test_scientific_name_max_length(self):
        max_length = self.group_1._meta.get_field("scientific_name").max_length

        self.assertEqual(max_length, 50)