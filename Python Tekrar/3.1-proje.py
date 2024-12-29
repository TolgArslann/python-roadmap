"""
Mini Proje:
“Ürün Yönetim Sistemi” oluştur:

Kullanıcıdan ürün adı, fiyatı ve stok miktarını alarak bir sözlükte sakla.
Kullanıcı yeni bir ürün ekleyebilir, mevcut bir ürünü güncelleyebilir veya silebilir.
"""
myDict = {}
urunNo = 0
found = False
while True:
    userProduct = input("Urun adini giriniz : ")
    urunNo +=1
    try:
        userProductValue = float(input("Urun Fiyatini giriniz : "))
        lastValue = f"{userProductValue} TL"
    except ValueError:
        print("Lutfen gecerli bir deger giriniz...")
    try:
        productStock = int(input("Stok miktariniz giriniz : "))
    except ValueError:
        print("Gecerli bir deger giriniz...")
    myDict[urunNo] = {"Urun" : userProduct, "toplam stok": productStock, "urun fiyati ": lastValue}
    #myDict[urunNo].update({"Urun" : userProduct, "toplam stok": productStock, "urun fiyati ": lastValue})
    while True:
        user_input = int(input("\n\nUrun eklemeye devam etmek icin '1'\n" 
                               "Urunleri goruntulemek icin '2'\n"
                                "Mevcut Urunu guncellemek icin '3'\n"
                                "Sonlandirmak icin '4'\n"
                                "\nIsleminiz : "))
        if user_input == 1:
            break
        elif user_input == 2:
            print(myDict)
        elif user_input == 3:# bu kisimda tikandim. devamini getiremiyorum.
            print(myDict)
            update_num = input("Urunleriniz listelenmistir.Guncellemek istediginiz urunun numarasini giriniz : ")
            # myDict[update_num].update
        elif user_input == 4:
            found = True
            break
        else:
            print("Gecerli bir deger giriniz")
    if found:
        break
    
