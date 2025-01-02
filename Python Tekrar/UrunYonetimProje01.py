myDict = {}
def getPositiveFloat():#Fiyatin alinmasi ve negatif girilip girilmediginin kontrolu
    while True:
        try:
            controlledValue = float(input("Urun Fiyatini giriniz : "))
            if controlledValue < 0:
                raise ValueError("Sayı negatif olamaz.")  
            return controlledValue  # Pozitif bir değer girilirse döner
        except ValueError as e:
            print(e)  
def getProductValue():#Fiyatin formatinin duzenlenmesi
    userProductValue = getPositiveFloat()
    lastValue = f"{userProductValue:,.0f}".replace(",", ".") + " TL"
    return lastValue
def getProductStock():####stok mıktarı alma
    try:
        productStock = int(input("Stok miktariniz giriniz : "))
        if productStock < 0:
            raise ValueError("Stok negatif olamaz") 
    except ValueError:
            print("Gecerli bir deger giriniz...")
    return productStock
def addProduct(): ####Urun Ekleme      
    #Kullanicidan urun bilgileri istenmeye basliyor
    userProduct = input("Urun adini giriniz : ")
    urunNo = 0
    urunNo +=1
    productValue = productValues()
    productStock = getProductStock()                                                                                                                                                                                   
    #Urunler Dictionary Aktariliyor
    myDict[urunNo] = {"Urun" : userProduct, "toplam stok": productStock, "urun fiyati":productValue}
    return myDict
def showProduct(): ####Urun Gosterimi
    if not myDict:
        print("Görüntülenecek ürün bulunmamaktadır.\n")
        return
    print(f"\n\n{'Ürün No':<10} {'Ürün İsmi':<20} {'Stok':<10} {'Fiyat':<10}")# Tablo Başlıkları
    print("-" * 50)
    for i in myDict: ##Ürün Bilgilerini Yazdır-Tablola
        urun = myDict[i].get("Urun", "Bilinmiyor")
        stok = myDict[i].get("toplam stok", "Bilinmiyor")
        fiyat = myDict[i].get("urun fiyati", "Bilinmiyor")

        fiyat = fiyat if fiyat is not None else "Bilinmiyor"

        print(f"{i:<10} {urun:<20} {stok:<10} {fiyat:<10}")
def productUpdate(): ####Urun update
    try:
        urun_no = int(input("Guncellemek istediginiz urun numarasini giriniz : "))
        if urun_no in myDict:
            yeni_ad = input("Yeni Urun ismini giriniz : ")
            try:
                yeni_fiyat = float(input("Yeni ürün fiyatını giriniz: "))
                yeni_fiyat_str = f"{yeni_fiyat} TL"
            except ValueError:
                print("Geçerli bir fiyat giriniz.")
                return
            try:
                yeni_stok = int(input("Yeni stok miktarını giriniz: "))
            except ValueError:
                print("Geçerli bir stok miktarı giriniz.")
                return
            myDict[urun_no] = {"Urun": yeni_ad, "toplam stok": yeni_stok, "urun fiyati": yeni_fiyat_str}
            print("Ürün başarıyla güncellendi.")
        else:
            print("Gecersiz urun numarasi...")
    except ValueError:
        print("Geçerli bir ürün numarası giriniz.")  
def urun_sil(): #urun silimi
    try:
        urun_no = int(input("Silmek istediğiniz ürünün numarasını giriniz: "))
        if urun_no in myDict:
            del myDict[urun_no]
            print("Ürün başarıyla silindi.")
        else:
            print("Geçersiz ürün numarası.")
    except ValueError:
        print("Geçerli bir ürün numarası giriniz.")
def menu(): ####menu sistemi
    found = False
    while True:
        print("\n1. Ürün ekle")
        print("2. Ürünleri görüntüle")
        print("3. Ürün güncelle")
        print("4. Ürün sil")
        print("5. Çıkış")
        try:
            secim = int(input("Seçiminiz: "))
            print()
            if secim == 1:
                addProduct()
            elif secim == 2:
                showProduct()
            elif secim == 3:
                productUpdate()
            elif secim == 4:
                urun_sil()
            elif secim == 5:
                print("Programdan çıkılıyor.")
                found = True
                break
            else:
                print("Geçersiz seçim. Lütfen 1-5 arasında bir sayı giriniz.")
        except ValueError:
            print("Lütfen geçerli bir sayı giriniz.")
        if found:
            break
menu()