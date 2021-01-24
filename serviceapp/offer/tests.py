from django.test import TestCase
from offer.OfferController import OfferController
from home.models import *
import unittest


class ValidatorsTestCase(unittest.TestCase):
    def test_offer_add(self):
        new_off = ServiceOffer.objects.filter(service_offer_id='SVO2021010000').get()
        if new_off is not None:
            self.assertEqual(new_off.status, 'Accepted')
            self.assertEqual(new_off.customer_performance, 3.0)
            self.assertEqual(new_off.provider_performance, 3.0)


        return True