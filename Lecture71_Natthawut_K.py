menuList = []
priceList = []

def showBill():
    totalPrice = 0
    print("---- My Food----")
    for i in range(len(menuList)):
        print(menuList[i], priceList[i])
        totalPrice += int(priceList[i])
    print("ราคารวม :", totalPrice,"THB")

while True:
    menuName = input("กรุณาใส่เมนู :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("กรุณาใส่ราคา (THB):")
        menuList.append(menuName)
        priceList.append(menuPrice)

showBill()