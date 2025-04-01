class Product:

    def __init__(self, ProdNum, ProdName, InitQuan, Price):
        self.ProdNum = ProdNum
        self.ProdName = ProdName
        self.InitQuan = InitQuan
        self.Price = Price

    def AppendProduct(self):
        prodAppend = open("Product.txt", "a")
        prodAppend.write(f"{self.ProdNum} {self.ProdName} {self.InitQuan} {self.Price}\n")
        prodAppend.close()