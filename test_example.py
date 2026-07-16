import unittest


def process_orders(orders, inventory):
    successful_orders = []
    for order in orders:
        product = order["product"]
        quantity = order["quantity"]

        if product not in inventory:
            raise ValueError(f"Product '{product}' not found in inventory")

        if quantity > inventory[product]:
            raise ValueError(f"Not enough stock for '{product}'")

        inventory[product] -= quantity
        successful_orders.append(order)

    return successful_orders






class TestProcessOrders(unittest.TestCase):

    # ამოწმებს, სწორად აგდებს თუ არა ერორს, როცა პროდუქტი საერთოდ არ არის საწყობში
    def test_product_not_in_inventory(self):
        inventory = {"apple": 10}
        orders = [{"product": "banana", "quantity": 5}]  # ბანანი არ გვაქვს საწყობში

        with self.assertRaises(ValueError) as context:
            process_orders(orders, inventory)
        
        # ასევე შეგვიძლია შევამოწმოთ, რომ ერორის ტექსტი ზუსტია
        self.assertEqual(str(context.exception), "Product 'banana' not found in inventory")

    # ამოწმებს, სწორად აგდებს თუ არა ერორს, როცა პროდუქტი არის, მაგრამ არასაკმარისი რაოდენობით
    def test_insufficient_stock(self):
        inventory = {"apple": 5}
        orders = [{"product": "apple", "quantity": 10}]  # საწყობში 5-ია, ჩვენ 10 გვინდა

        with self.assertRaises(ValueError) as context:
            process_orders(orders, inventory)
            
        self.assertEqual(str(context.exception), "Not enough stock for 'apple'")

    # ამოწმებს, რომ სწორი მონაცემების შემთხვევაში პროდუქტები აკლდება საწყობს და ბრუნდება წარმატებული ორდერები
    def test_successful_order_processing(self):
        # საწყისი საწყობი
        inventory = {
            "apple": 10,
            "banana": 20
        }
        orders = [
            {"product": "apple", "quantity": 3},
            {"product": "banana", "quantity": 5}
        ]

        # ფუნქციის გამოძახება
        result = process_orders(orders, inventory)

        # 1. ვამოწმებთ, რომ ნაშთები სწორად დაკლდა საწყობში (10 - 3 = 7; 20 - 5 = 15)
        self.assertEqual(inventory["apple"], 7)
        self.assertEqual(inventory["banana"], 15)

        # 2. ვამოწმებთ, რომ ფუნქციამ დააბრუნა წარმატებული ორდერების სია
        self.assertEqual(result, orders)


if __name__ == "__main__":
    unittest.main()