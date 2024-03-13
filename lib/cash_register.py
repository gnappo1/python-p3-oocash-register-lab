#!/usr/bin/env python3

class CashRegister:

    def __init__(self, discount = 0):
        self.discount = discount
        self.total = 0
        self.items = []

    def add_item(self, title, price, quantity = 1):
        self.total += price * quantity
        # counter = 0
        # while counter < quantity:
        self.items.append({'title': title, 'price': price, 'quantity': quantity})
        # for _ in range(quantity):
        # self.items.append(title)
        # counter += 1
        return self.total

    def apply_discount(self):
        if self.discount:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if not len(cash_register_with_discount.items):
            return "There are no transactions to void"
        popped_el = cash_register_with_discount.items.pop()
        self.total -= (
          popped_el["quantity"]
          * popped_el["price"]
      )
        return popped_el

cash_register_with_discount = CashRegister(20)
cash_register_with_discount.add_item("book", 5.00, 3)
cash_register_with_discount.add_item("Lucky Charms", 4.5)
print(cash_register_with_discount)
