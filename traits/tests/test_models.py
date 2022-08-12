from django.test import TestCase

from traits.models import Trait


class TraitsTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.name = "peludo"

        cls.trait_1_data = {"name": "peludo"}
        cls.trait_1 = Trait.objects.create(**cls.trait_1_data)

    def test_name_max_length(self):
        max_length = self.trait_1._meta.get_field("name").max_length

        self.assertEqual(max_length, 20)
