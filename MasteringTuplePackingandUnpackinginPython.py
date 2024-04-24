orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    # More orders...
]

def simplify(orders):
    for (name, product, quantity) in orders:
        print(f'''Name: {name}
Product: {product}
Quantity: {quantity} \n''')

simplify(orders)
print(simplify)

    