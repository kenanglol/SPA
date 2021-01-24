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
        return True


if __name__ == '__main__':
    unittest.main()
