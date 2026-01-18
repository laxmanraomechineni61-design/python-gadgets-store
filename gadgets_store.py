products = {
    "101": {"name": "Sony Alpha 4", "price": 250000},
    "102": {"name": "Gimbal", "price": 40000},
    "103": {"name": "Godex", "price": 10000},
    "104": {"name": "Drone DJI Pro", "price": 200000},
    "105": {"name": "Sony Cineline", "price": 250000}
}

cart = []

print("--- Welcome to the Gadgets Studio ---")

print("\nAvailable Products:")
for pid, details in products.items():
    print(f"ID: {pid} | Name: {details['name']} | Price: ₹{details['price']}")
