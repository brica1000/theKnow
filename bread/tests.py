from django.test import TestCase
from bread.models import Orders
from django.core.exceptions import ValidationError


class OrdersModelTest(TestCase):

    def test_can_make_order(self):
        order = Orders(
            customer = 'testcustomer',
            order_slot = 'morning',
            order_details = 'hook it up!'
            )
        order.save()
        self.assertIn(order, Orders.objects.all())
