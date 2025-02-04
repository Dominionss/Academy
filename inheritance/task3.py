"""
add(product, amount) - adds a specified quantity of a single product with a predefined price premium for your store(30 percent)
set_discount(identifier, percent, identifier_type=’name’) - adds a discount for all products specified by input identifiers (type or name). The discount must be specified in percentage
sell_product(product_name, amount) - removes a particular amount of products from the store if available, in other case raises an error. It also increments income if the sell_product method succeeds.
get_income() - returns amount of many earned by ProductStore instance.
get_all_products() - returns information about all available products in the store.
get_product_info(product_name) - returns a tuple with product name and amount of items in the store.
"""


class Product:
    def __init__(self, type_of_product, name, price):
        self.type = type_of_product
        self.name = name
        self.price = price

    def __str__(self):
        return self.name


class ProductStore:
    def __init__(self):
        self.products = {}
        self.income = 0

    def add(self, product, amount):
        price_with_premium = product.price * 1.3
        if product.name not in self.products:
            self.products[product.name] = {"product": product, "amount": amount, "price": price_with_premium,
                                           "discount": 0}
        else:
            self.products[product.name]["amount"] += amount

    def set_discount(self, identifier, percent, identifier_type='name'):
        if identifier_type == 'name':
            if identifier in self.products:
                self.products[identifier]["discount"] = percent
            else:
                raise ValueError(f"Product '{identifier}' not found in store.")
        elif identifier_type == 'type':
            found = False
            for item in self.products.values():
                if item["product"].type == identifier:
                    item["discount"] = percent
                    found = True
            if not found:
                raise ValueError(f"No products of type '{identifier}' found in store.")
        else:
            raise ValueError("Invalid identifier_type. Use 'name' or 'type'.")

    def sell_product(self, product_name, amount):
        if product_name not in self.products:
            raise ValueError(f"Product '{product_name}' not found in store.")
        if self.products[product_name]["amount"] < amount:
            raise ValueError(f"Not enough '{product_name}' in stock.")

        product_info = self.products[product_name]
        price = product_info["price"] * (1 - product_info["discount"] / 100)

        self.income += price * amount
        self.products[product_name]["amount"] -= amount

        if self.products[product_name]["amount"] == 0:
            del self.products[product_name]

    def get_income(self):
        return self.income

    def get_all_products(self):
        return [(name, details["amount"]) for name, details in self.products.items()]

    def get_product_info(self, product_name):
        if product_name not in self.products:
            raise ValueError(f"Product '{product_name}' not found in store.")
        return product_name, self.products[product_name]["amount"]


p = Product('Sport', 'Football T-Shirt', 100)

p2 = Product('Food', 'Ramen', 1.5)

s = ProductStore()

s.add(p, 10)

s.add(p2, 300)

s.sell_product('Ramen', 10)

print(s.get_product_info('Ramen') == ('Ramen', 290))



