def productValuefonk(): #Kullanicidan urun fiyati alma
    userProductValue = float(input("Urun Fiyatini giriniz : "))
    lastValue = f"{userProductValue:,.0f}".replace(",", ".") + " TL"
    return lastValue
deneme = productValuefonk()   
print(deneme)