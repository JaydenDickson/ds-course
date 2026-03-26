# ======== Class Definition ========


class Shoe:
    """
    Represents a shoe item in inventory.

    Attributes:
        country (str): Country of origin.
        code (str): Unique product code.
        product (str): Name of the product.
        cost (float): Cost per item.
        quantity (int): Number of items in stock.
    """

    def __init__(self, country, code, product, cost, quantity):
        """Initialize a Shoe object."""
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        """Return the cost of the shoe."""
        return self.cost

    def get_quantity(self):
        """Return the quantity in stock."""
        return self.quantity

    def __str__(self):
        """Return a representation of the shoe."""
        return (
            f"{self.country},{self.code},{self.product},"
            f"{self.cost},{self.quantity}"
        )


# ======== Global Shoe List ========

shoe_list = []


# ======== Functions ========


def read_shoes_data():
    """
    Read shoe data from 'inventory.txt' and populate shoe_list.

    Skips the header row and converts each line into a Shoe object.
    """
    with open("inventory.txt", "r") as file:
        next(file)

        for line in file:
            try:
                # Split line into components and create a Shoe object
                country, code, product, cost, quantity = (
                    line.strip().split(",")
                )
                shoe = Shoe(
                    country,
                    code,
                    product,
                    float(cost),
                    int(quantity)
                )
                shoe_list.append(shoe)

            except ValueError:
                print(f"Skipping invalid line: {line.strip()}")


def capture_shoes(country, code, product, cost, quantity):
    """
    Create a Shoe object and add it to shoe_list after validation.
    """
    try:
        country = str(country)
        code = str(code)
        product = str(product)
        cost = float(cost)
        quantity = int(quantity)

    except ValueError:
        print("Invalid input. Please enter the correct data types.")
        return

    shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe)


def view_all():
    """Display all shoes in the inventory."""
    for shoe in shoe_list:
        print(shoe)


def re_stock():
    """Find the lowest stock item and update its quantity."""
    # Check if shoe_list is empty
    if not shoe_list:
        print("No shoes available. Please use option 1 to load shoe data first.")
        return
    
    # Find shoe with lowest quantity by using min() with a key function
    min_shoe = min(shoe_list, key=lambda shoe: shoe.quantity)

    # Display the shoe with the lowest quantity and prompt user to add stock
    print(
        f"Lowest stock item: {min_shoe} "
        f"(Quantity: {min_shoe.quantity})"
    )

    try:
        added_qty = int(input("Enter quantity to add: "))

    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    min_shoe.quantity += added_qty
    print(f"Updated quantity: {min_shoe.quantity}")


def search_shoe():
    """Search for a shoe by its code."""
    shoe_code = input("Enter shoe code: ")
    # Search for shoe with matching code using a linear search
    for shoe in shoe_list:
        if shoe.code == shoe_code:
            print(shoe)
            return shoe

    print("Shoe not found.")
    return None


def value_per_item():
    """Calculate and display total value for each shoe."""
    for shoe in shoe_list:
        value = shoe.get_cost() * shoe.get_quantity()
        print(f"{shoe.product}: Value = {value}")


def highest_qty():
    """Display the shoe with the highest quantity."""
    # Check if shoe_list is empty
    if not shoe_list:
        print("No shoes available. Please use option 1 to load shoe data first.")
        return
    # Find shoe with highest quantity by using max() with a key function
    max_shoe = max(shoe_list, key=lambda shoe: shoe.quantity)

    print(
        f"Highest stock item: {max_shoe} "
        f"(Quantity: {max_shoe.quantity})"
    )
    print(f"{max_shoe.product} is for sale!")


# ======== Main Program ========

"""
Main menu loop for the inventory system.

Writes updated data back to 'inventory.txt' on exit.
"""

while True:
    input_menu = input(
        """Select an option:
1. Read shoe data
2. Capture shoes
3. View all shoes
4. Re-stock shoe
5. Search shoe
6. Calculate value per item
7. Show shoe with highest quantity
8. Exit and save changes
"""
    )

    if input_menu == "1":
        read_shoes_data()

    elif input_menu == "2":
        country = input("Enter country: ")
        code = input("Enter code: ")
        product = input("Enter product: ")
        cost = input("Enter cost: ")
        quantity = input("Enter quantity: ")

        capture_shoes(country, code, product, cost, quantity)

    elif input_menu == "3":
        view_all()

    elif input_menu == "4":
        re_stock()

    elif input_menu == "5":
        search_shoe()

    elif input_menu == "6":
        value_per_item()

    elif input_menu == "7":
        highest_qty()

    elif input_menu == "8":
        # Write updated shoe data back to 'inventory.txt'
        with open("inventory.txt", "w") as file:
            file.write("Country,Code,Product,Cost,Quantity\n")

            for shoe in shoe_list:
                file.write(f"{shoe}\n")
        break

    else:
        print("Invalid option. Enter a number from 1 to 8.")