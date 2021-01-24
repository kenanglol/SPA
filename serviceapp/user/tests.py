from django.test import TestCase
from user.UserController import ProviderController
from home.models import *
import unittest


class ValidatorsTestCase(unittest.TestCase):
    def test_pro_add(self):
        new_pro = User.objects.filter(user_id='USR2021010004').get()
        if new_pro is not None:
            self.assertEqual(new_pro.mail, 'abc@gmail.com')
            self.assertTrue(len(new_pro.name) < 31)
            self.assertTrue(len(new_pro.surname) < 31)
            self.assertEqual(new_pro.location, 'Balıkesir')
            self.assertEqual(new_pro.score, 3.0)
        return True

    def test_cus_add(self):
        new_cus = User.objects.filter(user_id='USR2021010000').get()
        if new_cus is not None:
            self.assertEqual(new_cus.mail, 'kemalkaya@gmail.com')
            self.assertTrue(len(new_cus.name) < 31)
            self.assertTrue(len(new_cus.surname) < 31)
            self.assertEqual(new_cus.location, 'İstanbul')
            self.assertEqual(new_cus.score, 3.0)
        return True



