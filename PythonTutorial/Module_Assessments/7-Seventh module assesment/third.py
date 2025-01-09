class Product:
    def __init__(self, name, price, quantity):
        """Initialize the product with name, price, and quantity."""
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        """Displays the product's name, price, and quantity."""
        print(f"Product Name: {self.name}")
        print(f"Price: ${self.price}")
        print(f"Quantity Available: {self.quantity}")

    def update_quantity(self, quantity_sold_or_restocked):
        """Updates the quantity of the product (either selling or restocking)."""
        self.quantity += quantity_sold_or_restocked
        if quantity_sold_or_restocked > 0:
            print(f"{quantity_sold_or_restocked} units of {self.name} restocked.")
        elif quantity_sold_or_restocked < 0:
            print(f"{abs(quantity_sold_or_restocked)} units of {self.name} sold.")

    def calculate_value(self):
        """Calculates and returns the total value of the product (price * quantity)."""
        return self.price * self.quantity


class InventorySystem:
    def __init__(self):
        """Initialize an empty list of products."""
        self.products = []

    def add_product(self, name, price, quantity):
        """Add a new product to the inventory."""
        new_product = Product(name, price, quantity)
        self.products.append(new_product)
        print(f"{name} has been added to the inventory.")

    def view_inventory(self):
        """Displays all products in the inventory."""
        if not self.products:
            print("No products in inventory.")
        else:
            for product in self.products:
                product.display_info()
                print("-----------------------------")

    def total_inventory_value(self):
        """Calculates the total value of all products in the inventory."""
        total_value = sum(product.calculate_value() for product in self.products)
        print(f"Total Inventory Value: ${total_value:.2f}")

    def search_product(self, name):
        """Search for a product by its name."""
        for product in self.products:
            if product.name.lower() == name.lower():
                return product
        return None


def main():
    # Create an instance of the Inventory System
    inventory = InventorySystem()

    # Add some products to the inventory
    inventory.add_product("Laptop", 1200, 10)
    inventory.add_product("Smartphone", 800, 20)
    inventory.add_product("Headphones", 150, 50)

    # View all products in the inventory
    print("\n--- Current Inventory ---")
    inventory.view_inventory()

    # Restock some products
    product_to_restock = inventory.search_product("Laptop")
    if product_to_restock:
        product_to_restock.update_quantity(5)  # Restocking 5 more laptops

    # Sell some products
    product_to_sell = inventory.search_product("Smartphone")
    if product_to_sell:
        product_to_sell.update_quantity(-3)  # Selling 3 smartphones

    # View updated inventory
    print("\n--- Updated Inventory ---")
    inventory.view_inventory()

    # Calculate and display the total inventory value
    inventory.total_inventory_value()

    # Search for a product that doesn't exist
    print("\n--- Searching for a non-existent product ---")
    product_not_found = inventory.search_product("Tablet")
    if product_not_found:
        product_not_found.display_info()
    else:
        print("Product not found in inventory.")


# Run the program
if __name__ == "__main__":
    main()
