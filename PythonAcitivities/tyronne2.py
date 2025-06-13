def Transaction():
    try:
        with open("Product.txt", "r") as file:
            products = file.readlines()
    except FileNotFoundError:
        print("No product records found.")
        return

    ProdNo = input("Enter Product Number: ")
    found = False
    updated_products = []

    for line in products:
        data = line.strip().split()
        if data and data[0] == ProdNo:
            found = True
            print(f"Product Found: {data[1]} - Current Quantity: {data[2]}")
            transaction_type = input("Enter transaction type (sold/purchase): ").lower()
            if transaction_type not in ["sold", "purchase"]:
                print("Invalid transaction type.")
                return

            try:
                quantity = int(input("Enter quantity: "))
            except ValueError:
                print("Invalid quantity input.")
                return

            current_quantity = int(data[2])
            if transaction_type == "sold":
                if quantity > current_quantity:
                    print("Insufficient stock.")
                    return
                current_quantity -= quantity
            else:  # purchase
                current_quantity += quantity

            updated_products.append(f"{data[0]} {data[1]} {current_quantity}\n")
        else:
            updated_products.append(line)

    if not found:
        print("Record not found.")
        return

    with open("Product.txt", "w") as file:
        file.writelines(updated_products)

    print("Transaction successful! Updated product list:")
    with open("Product.txt", "r") as file:
        print(file.read())
