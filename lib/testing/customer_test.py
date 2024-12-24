import pytest

from classes.many_to_many import Coffee
from classes.many_to_many import Customer
from classes.many_to_many import Order


class TestCustomer:
    """Tests for the Customer class"""

    def test_has_name(self):
        """Customer is initialized with name"""
        customer = Customer("Steve")
        assert customer.name == "Steve"

    def test_name_is_mutable_string(self):
        """Name is a mutable string"""
        customer = Customer("Steve")
        customer.name = "Stove"
        assert customer.name == "Stove"

    def test_has_many_orders(self):
        """Customer has many orders"""
        coffee = Coffee("Vanilla Latte")
        customer = Customer("Steve")
        order_1 = Order(customer, coffee, 2.0)
        order_2 = Order(customer, coffee, 5.0)
        assert len(customer.orders()) == 2
        assert order_1 in customer.orders()
        assert order_2 in customer.orders()

    def test_create_order(self):
        """Creates a new order for a customer"""
        coffee_1 = Coffee("Vanilla Latte")
        customer_1 = Customer("Steve")
        order_1 = customer_1.create_order(coffee_1, 2.0)
        assert isinstance(order_1, Order)
        assert order_1.customer == customer_1
        assert order_1.coffee == coffee_1

    def test_most_aficionado(self):
        """The customer who has spent the most on the coffee instance provided."""
        coffee = Coffee("Vanilla Latte")
        steve = Customer("Steve")
        dima = Customer("Dima")
        Order(steve, coffee, 2.0)
        Order(steve, coffee, 4.0)
        Order(dima, coffee, 5.0)
        Order(dima, coffee, 2.0)

        assert Customer.most_aficionado(coffee) == dima

