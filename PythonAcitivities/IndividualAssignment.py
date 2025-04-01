from IndiAssClass import Product

def UserInput():
    while True:

        prodNo = open("Product.txt", "r")
        ProdNo = input("Enter Product Number: ")
        if ProdNo not in prodNo.read():
            if not ProdNo:
                print("Empty Number")
                continue
            elif ProdNo.isdigit():
                  ProdNo = int(ProdNo)
            else :
                print("Invalid Input")
                continue
        else:
            print(f"{ProdNo} is already in the list")
            continue
        prodNo.close()

        prodNa = open("Product.txt", "r")
        ProdNa = input("Enter Product Name: ").capitalize()
        if ProdNa not in prodNa.read():
            if not ProdNa:
                print("Empty Number")
                continue
            elif ProdNa:
                Prodna = str(ProdNa)
            else:
                print("Invalid Input")
                continue
        else:
            print(f"{ProdNa} is already in the list")
            continue
        prodNa.close()

        InQuan = input("Enter Initial Quantity: ")

        if not InQuan:
            print("Empty Number")
            continue
        if InQuan.isdigit():
            Inquan = int(InQuan)
        else:
            print("Invalid Input")
            continue

        Prc = input("Enter Price: ")
        if not Prc:
            print("Empty Number")
            continue
        if Prc.isdigit():
            Prc = float(Prc)
        else:
            print("Invalid Input")
            continue

        p1 = Product(ProdNo, ProdNa, InQuan, Prc)
        p1.AppendProduct()

        InputAgain = input("Input again? Yes or No: ").capitalize()
        if InputAgain == "Yes":
            print("\n")
        else:
            print("Input Succesful")
            break

def Transaction():

    prodSearchList = []

    prodSearch1 = open("Product.txt", "r")
    prodSearchLine = prodSearch1.readlines()
    #print(prodSearchLine)
    prodSearch1.close()

    prodSearch2 = open("Product.txt", "r")
    prodSearchLen = len(prodSearch2.readlines())
    #print(prodSearchLen)
    prodSearch2.close()

    for i in range(0, prodSearchLen):
        line = prodSearchLine[i].strip().split(" ")
        prodSearchList.append(line)

    while True:
        ProdNum = int(input("Enter Product Number: "))
        for i in range(0, len(prodSearchList)):

            if prodSearchList[i][0] == str(ProdNum):
                #print("Find Product:", prodSearchList[i][0])

                #print("Quantity Available:", prodSearchList[i][2])

                IntQty = int(prodSearchList[i][2])
                PurSell = input("Purchase or Sell: ").capitalize()
                Qty = int(input("Enter Quantity: "))

                if PurSell == "Purchase":
                    IntQty = IntQty + Qty
                elif PurSell == "Sell":
                    IntQty = IntQty - Qty
                    Price = float(prodSearchList[i][3])
                    SoldPrice = Qty * Price
                    print("Sold Price:", SoldPrice)

                else:
                    print("Invalid Input")
                    continue

                prodSearchList[i][2] = str(IntQty)
                break
        else:
            continue

        inputAgain = input("Input again? Yes or No: ").capitalize()
        if inputAgain == "Yes":
            continue

        prodUpdate = open("Product.txt", "w")
        for product in prodSearchList:
            prodUpdate.write(" ".join(product) + "\n")
        break

# checking if the product is in the txt file
while True:

    User_Input = input("Product / Transaction / Exit (P/T/E): ").upper()
    if User_Input == "P":
        UserInput()
    elif User_Input == "T":
        Transaction()
    elif User_Input == "E":
        TxtFile = open("Product.txt", "r")
        print(TxtFile.read())
        TxtFile.close()
        break
    else:
        print("Invalid Input")
        continue