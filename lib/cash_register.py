#!/usr/bin/env python3
import ipdb
class CashRegister:

    def __init__(self, discount=0) -> None:
        self.discount = discount
        self.total = 0
        self.items_with_deets = []
        self.items = []

    def add_item(self, item_name, item_price, quantity=1):
        self.items_with_deets.append(
            {"name": item_name, "price": item_price, "quantity": quantity}
        )
        for _ in range(quantity):
            self.items.append(item_name)
        self.total += item_price * quantity

    def apply_discount(self):
        if self.discount:
            self.total *= (100 - self.discount) / 100
            print(f"After the discount, the total comes to ${round(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        # extract/remove the LAST el from the items_with_deets using index -1
        last_item_to_void = self.items_with_deets.pop()
        # and then update the total (-=)
        self.total -= last_item_to_void["price"] * last_item_to_void["quantity"]
        for _ in range(last_item_to_void.get('quantity')):
          self.items.pop()

if __name__ == "__main__":
    cr = CashRegister()
    crwd = CashRegister(20)
    cr.add_item("eggs", 0.98)
    cr.add_item("book", 5.00, 3)
    crwd.add_item("book", 5.00, 3)
    cr.apply_discount()
    crwd.apply_discount()
    cr.void_last_transaction()
    crwd.void_last_transaction()
    import ipdb; ipdb.set_trace()
