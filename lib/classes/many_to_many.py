class Coffee:
    def __init__(self, name):
        self._name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        raise AttributeError("name is immutable")

    def orders(self):
        return self._orders

    def add_order(self, order):
        """Add an order to the coffee"""
        self._orders.append(order)

    def customers(self):
        """Return a list of unique customers who have ordered this coffee"""
        return list(set([order.customer for order in self._orders]))

    def num_orders(self):
        """Return the number of orders for this coffee"""
        return len(self._orders)

    def average_price(self):
        """Return the average price of the orders for this coffee"""
        if self.num_orders() == 0:
            return 0
        return sum([order.price for order in self._orders]) / self.num_orders()

class Customer:
    def __init__(self, name):
        self.name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0 or len(value) > 15:
            raise Exception("Invalid customer name")
        self._name = value

    def orders(self):
        """Return a list of all orders for this customer"""
        return self._orders

    def create_order(self, coffee, price):
        """Create an order for this customer"""
        order = Order(self, coffee, price)
        self.add_order(order)
        return order

    def add_order(self, order):
        """Add an order to the customer's order list"""
        self._orders.append(order)

    def coffees(self):
        """Return a list of unique coffees this customer has ordered"""
        return list(set([order.coffee for order in self._orders]))

    @staticmethod
    def most_aficionado(coffee):
        """Return the customer who has spent the most on a given coffee"""
        customers = coffee.customers()
        customer_spend = {customer: sum([order.price for order in customer.orders() if order.coffee == coffee]) for customer in customers}
        return max(customer_spend, key=customer_spend.get, default=None)

class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self._price = price  # use _price to store the price as private
        self.__class__.all.append(self)
        coffee.add_order(self)
        customer.add_order(self)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        raise AttributeError("price is immutable")

    def __str__(self):
        return f"{self.customer.name} ordered {self.coffee.name} for ${self.price}"
