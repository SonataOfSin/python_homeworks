

products = [
    {"cola": {"price": 1.5, "quantity": 10}},
    {"fanta": {"price": 2.5, "quantity": 5}},
    {"snickers": {"price": 3.5, "quantity": 12}},
    {"water": {"price": 4.5, "quantity": 8}},
    {"beer": {"price": 6.5, "quantity": 5}}
]

print("--- products list ---")
for item in products:
    product_name = list(item.keys())[0]
    print(f"- {product_name}")
print("\n-----------------------")
total_sum = 0
for item in products:
    for name, info in item.items():
        total_sum += info["price"] * info["quantity"]

print(f"sum of every product: {total_sum} lari")