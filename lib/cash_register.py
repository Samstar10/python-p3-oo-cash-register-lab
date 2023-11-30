#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.items.extend([title] * quantity)

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${self.total:.2f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.items:
            last_item_price = self._get_last_item_price()
            self.total -= last_item_price
            print(f"Subtracted ${last_item_price:.2f} from the total.")
            self.items.pop()
        else:
            print("No items to void.")

    def _get_last_item_price(self):
        last_item_title = self.items[-1]
        return self._get_item_price(last_item_title)

    def _get_item_price(self, title):
        return 1

    def reset_register_totals(self):
        self.total = 0
        self.items = []
