from django.test import TestCase
from user.UserController import ProviderController
from home.models import *
import unittest


class ValidatorsTestCase(unittest.TestCase):
    def test_pro_add(self):
        pro = ProviderController.provider_add('ahmet', 'can', 'abc@gmail.com', 'Balıkesir', 3, 'SVR2021010000')
        self.assertIsNotNone(Provider.objects.filter(experience=pro.experience, speciality=pro.speciality))
        return True


if __name__ == '__main__':
    unittest.main()
