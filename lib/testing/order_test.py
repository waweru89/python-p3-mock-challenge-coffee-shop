import pytest

from classes.many_to_many import Coffee
from classes.many_to_many import Customer
from classes.many_to_many import Order


class TestOrders:
    """Tests for the Order class"""

    def test_has_price(self):
        """Order is initialized with a price"""
        coffee = Coffee("Mocha")
        customer = Customer('Steve')
        order_1 = Order(customer, coffee, 2.0)
        assert order_1.price == 2.0

    def test_price_is_immutable(self):
        """Price is immutable"""
        coffee = Coffee("Mocha")
        customer = Customer('Steve')
        order_1 = Order(customer, coffee, 2.0)
        with pytest.raises(AttributeError):
            order_1.price = 3.0