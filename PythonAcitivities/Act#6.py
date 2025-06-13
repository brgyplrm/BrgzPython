from itertools import product


class Product:

    def __init__(self, ProdNum, ProdName, InitQuan):
        self.ProdNum = ProdNum
        self.ProdName = ProdName
        self.InitQuan = InitQuan
        # self.Price = Price

    def AppendProduct(self):
        prodAppend = open("Products.txt", "a")
        prodAppend.write(f"{self.ProdNum} {self.ProdName} {self.InitQuan}a\n")
        prodAppend.close()


def searchData():
    try:
        with open("Products.txt", "r") as file:
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

    with open("Products.txt", "w") as file:
        file.writelines(updated_products)

    print("--------------------------------------------------")
    print("   Transaction successful! Updated product list:")
    print("--------------------------------------------------")
    with open("Products.txt", "r") as file:
        print(file.read())

def ProductInput():
    while True:
        while True:
            with open("Product.txt", "r") as prodNo:
                ProdNo = input("\nEnter Product Number: ").strip()
                if not ProdNo:
                    print("Empty Number")
                    continue
                if not ProdNo.isdigit():
                    print("Invalid Input. Enter a numeric Product Number.")
                    continue
                if ProdNo in prodNo.read():
                    print(f"{ProdNo} is already in the list")
                    continue
                ProdNo = int(ProdNo)  # Convert only after validation
                break

        while True:
            with open("Product.txt", "r") as prodNa:
                ProdNa = input("Enter Product Name: ").strip().capitalize()
                if not ProdNa:
                    print("Empty Name")
                    continue
                if ProdNa in prodNa.read():
                    print(f"{ProdNa} is already in the list")
                    continue
                break

        while True:
            InQuan = input("Enter Initial Quantity: ").strip()
            if not InQuan:
                print("Empty Quantity")
                continue
            if InQuan.isdigit():
                InQuan = int(InQuan)  # Ensure it's stored as an integer
                break
            else:
                print("Invalid Input. Enter a valid number.")

        with open("Product.txt", "a") as prodAppend:
            prodAppend.write(f"{ProdNo} {ProdNa} {InQuan}\n")  # Ensure correct format


        # while True:
        #     Prc = input("Enter Price: ")
        #     if not Prc:
        #         print("Empty Price")
        #         continue
        #     try:
        #         Prc = float(Prc)
        #         break
        #     except ValueError:
        #         print("Invalid Input")
        #         continue

        p1 = Product(ProdNo, ProdNa, InQuan)
        p1.AppendProduct()

        InputAgain = input("Input again? [Y / N]: ").capitalize()
        if InputAgain == "Y":
            print("\n")
        elif InputAgain == "N":
            print("Input Succesful")
            return
        else:
            print("Invalid Input")
            continue

while True:
    # dagdagan nyo nlng per part
    print("--------------------")
    print(" [A] Product Input  ")
    print(" [B] Show Product      ")
    print(" [C] Search Product      ")
    print(" [D] Exit           ")
    print("--------------------")

    User_Input = input("Choose here: ").upper()
    if User_Input == "A":
        ProductInput()
#   elif User_Input == "B":
#        Transaction()
    elif User_Input == "B":
        print("\n")
        print("----------------")
        print("  Product Data  ")
        print("----------------")
        TxtFile = open("Product.txt", "r")

        if not TxtFile:
            print("Empty File")
            continue
        for i in TxtFile:
            print(i, end="")
        TxtFile.close()
        print("\n")
    elif User_Input == "C":
        searchData()
    elif User_Input == "D":
        print("Exiting...")
        break
    else:
        print("Invalid Input")
