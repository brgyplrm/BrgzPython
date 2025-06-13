import time


class Product:
    def __init__(self, product_number, product_name, quantity, price):
        self.product_number = product_number
        self.product_name = product_name
        self.quantity = quantity
        self.price = price


def is_valid_name(name):
    return all(char.isalpha() or char.isspace() for char in name)


def input_products():
    products = read_from_file()
    existing_numbers = {p.product_number for p in products}
    existing_names = {p.product_name for p in products}

    print("Enter product details:")

    while True:
        try:
            # Input product details
            product_name = input("\nProduct Name: ").strip()

            if not is_valid_name(product_name):
                print("Invalid input! Product Name must contain only letters and spaces.")
                continue

            if product_name in existing_names:
                print("Error: A product with this name already exists!")
                continue

            product_number = input("Product Number: ")
            if not product_number.isdigit():
                print("Invalid input!")
                continue
            product_number = int(product_number)

            if product_number in existing_numbers:
                print("Error: A product with this number already exists!")
                continue

            quantity = input("Quantity: ")
            if not quantity.isdigit():
                print("Invalid input! Quantity must be a number.")
                continue
            quantity = int(quantity)

            price = input("Price: ")
            if not price.replace('.', '', 1).isdigit():  # Allow decimal points
                print("Invalid input! Price must be a number.")
                continue
            price = float(price)

            existing_names.add(product_name)
            existing_numbers.add(product_number)

            products.append(Product(product_number, product_name, quantity, price))

            stop = input("\nDo you want to stop adding products? (yes/no): ").strip().lower()
            if stop == 'yes':
                break

        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")

    write_to_file(products)

    # Display all records after adding products
    print("\nAll Product Records:")
    display_products(products)
    return products


def write_to_file(products, filename="product.txt"):
    with open(filename, 'w') as file:
        for product in products:
            file.write(f"{product.product_number},{product.product_name},{product.quantity},{product.price}\n")


def read_from_file(filename="product.txt"):
    products = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 4:
                    product_number = int(parts[0])
                    product_name = parts[1]
                    quantity = int(parts[2])
                    price = float(parts[3])
                    products.append(Product(product_number, product_name, quantity, price))
    except FileNotFoundError:
        pass
    except Exception as e:
        print(f"Error reading file: {e}")
    return products


def display_products(products):
    if not products:
        print("No products to display.")
        return

    print("\nProduct Records:")
    print("-" * 50)
    print(f"{'No.':<10}{'Product Name':<20}{'Quantity':<10}{'Price':<10}")
    print("-" * 50)
    time.sleep(0.5)

    for product in products:
        print(f"{product.product_number:<10}{product.product_name:<20}{product.quantity:<10}{product.price:<10}")
        time.sleep(0.3)


def search_and_update_product():
    products = read_from_file()
    if not products:
        print("No products available to search.")
        return

    product_number = input("Search Product Number: ")
    if not product_number.isdigit():
        print("Invalid Product Number.")
        return

    product_number = int(product_number)
    found_index = None

    for i, product in enumerate(products):
        if product.product_number == product_number:
            found_index = i
            break

    if found_index is None:
        print("\nRecord Not Found!")
        return

    found_product = products[found_index]
    print("\nProduct Found:")
    print("-" * 50)
    print(f"{'No.':<10}{'Product Name':<20}{'Quantity':<10}{'Price':<10}")
    print("-" * 50)
    print(
        f"{found_product.product_number:<10}{found_product.product_name:<20}{found_product.quantity:<10}{found_product.price:<10}")

    # Input transaction type
    while True:
        transaction = input("\nEnter transaction type (Sold/Purchased): ").strip().lower()
        if transaction in ['sold', 'purchased']:
            break
        print("Invalid transaction type! Please enter 'Sold' or 'Purchased'.")

    # Input quantity
    while True:
        quantity = input("Enter quantity: ").strip()
        if quantity.isdigit():
            quantity = int(quantity)
            if quantity > 0:
                break
        print("Invalid quantity! Please enter a positive number.")

    # Update quantity based on transaction
    if transaction == 'sold':
        if found_product.quantity >= quantity:
            found_product.quantity -= quantity
        else:
            print("Error: Not enough stock to sell this quantity!")
            return
    elif transaction == 'purchased':
        found_product.quantity += quantity

    # Save updated products to file
    write_to_file(products)
    print("\nTransaction completed successfully!")

    # Display updated product records
    print("\nUpdated Product Records:")
    display_products(products)


def search_and_delete_product():
    products = read_from_file()
    if not products:
        print("No products available to search.")
        return

    product_number = input("Search Product Number: ")
    if not product_number.isdigit():
        print("Invalid Product Number.")
        return

    product_number = int(product_number)
    found_index = None

    for i, product in enumerate(products):
        if product.product_number == product_number:
            found_index = i
            break

    if found_index is None:
        print("\nRecord Not Found!")
        return

    found_product = products[found_index]
    print("\nProduct Found:")
    print("-" * 50)
    print(f"{'No.':<10}{'Product Name':<20}{'Quantity':<10}{'Price':<10}")
    print("-" * 50)
    print(
        f"{found_product.product_number:<10}{found_product.product_name:<20}{found_product.quantity:<10}{found_product.price:<10}")

    # Confirm deletion
    confirm = input("\nAre you sure you want to delete this product? (yes/no): ").strip().lower()
    if confirm == 'yes':
        del products[found_index]
        write_to_file(products)
        print("\nProduct deleted successfully!")
    else:
        print("\nDeletion canceled. The product remains in the file.")

    # Display updated product records
    print("\nUpdated Product Records:")
    display_products(products)


def main():
    while True:
        print("\n==========Main Menu==========:\n")
        print("1] Input Products (With Price): ")
        print("2] Search and Update Product: ")
        print("3] Search and Delete Product: ")
        print("4] Exit")

        choice = input("\nChoose From [1-4]: ")

        if choice == '1':
            products = input_products()
            if products:
                print(f"\n{len(products)} product(s) in file.")
        elif choice == '2':
            search_and_update_product()
        elif choice == '3':
            search_and_delete_product()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()