from django.test import TestCase
from home.models import *
import unittest


class ValidatorsTestCase(unittest.TestCase):
    def test_adv_add(self):
        new_adv = Advert.objects.filter(advert_id='ADV2021010000').get()
        if new_adv is not None:
            self.assertEqual(new_adv.price, 150)
            self.assertEqual(new_adv.advert_name, 'Lise Öğrencilerine Matematik Dersi')
            self.assertEqual(new_adv.summary, 'Sinavlardan yüksek not almanız için uğraşıyoruz')
            self.assertTrue(len(new_adv.advert_name) < 101)
            return True
