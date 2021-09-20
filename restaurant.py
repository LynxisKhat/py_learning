class RestaurantTable:

    menus={
        'pizza':5000,
        'cola':600,
        'apple juice':2000,
        'hamburger':1000,
        'fried potato':1500
    }

    def __init__(self):
        self.total = 0
        self.orders = []

    def addOrder(self,order):
        self.orders.append(order)
        self.total+=self.menus[order]

    def printBill(self):
        for order in self.orders:
            print(f'{order} : {self.menus[order]}' )

        print(f'Total Price is {self.total}')



def startProgram():

    table = RestaurantTable()

    while True:
        order = input("Order : ")
        table.addOrder(order)

        another = input("Another ? Y / N : ")
        if another == 'y' :
            continue
        else:
            table.printBill()
            break


def printMenu():
    print("Today Menu")
    print("------------")
    for (key,value) in RestaurantTable.menus.items():
        print(f"{key} : {value}")

        
printMenu()
startProgram()

