"""
Mini Proje:
“Ürün Yönetim Sistemi” oluştur:

Kullanıcıdan ürün adı, fiyatı ve stok miktarını alarak bir sözlükte sakla.
Kullanıcı yeni bir ürün ekleyebilir, mevcut bir ürünü güncelleyebilir veya silebilir.
"""
def urunSistemi():
    myDict = {}
    urunNo = 0    
    while True:
        #Kullanicidan urun bilgileri istenmeye basliyor
        userProduct = input("Urun adini giriniz : ")
        urunNo +=1
        def productValuefonk(): #Kullanicidan urun fiyati alma
            userProductValue = float(input("Urun Fiyatini giriniz : "))
            lastValue = f"{userProductValue:,.0f}".replace(",", ".") + " TL"
            print(lastValue)                                                                                                                                                                                           
        def get_positive_float(prompt): #fiyatin gecerliligini kontrol etme
            while True:
                try:
                    value = float(input(prompt))
                    if value < 0:
                        raise ValueError("Değer negatif olamaz.")
                    return value
                except ValueError as e:
                    print(e)
        productValue = productValuefonk()
        kontrolledValue = get_positive_float(productValue)    
        def productStockfonk(): #stok fiyati alma
            try:
                productStock = int(input("Stok miktariniz giriniz : "))
                if productStock < 0:
                    raise ValueError("Stok negatif olamaz") 
            except ValueError:
                print("Gecerli bir deger giriniz...")
            return productStock
        #Urunler Dictionary Aktariliyor
        myDict[urunNo] = {"Urun" : userProduct, "toplam stok": productStockfonk(), "urun fiyati":productValuefonk() }
        def productShow(): #urunlerin gosterilmesi
            """
            Tüm ürünleri tablo formatında ekrana yazdırır.
            """
            if not myDict:
                print("Görüntülenecek ürün bulunmamaktadır.")
                return
            # Tablo Başlıkları
            print(f"\n\n{'Ürün No':<10} {'Ürün İsmi':<20} {'Stok':<10} {'Fiyat':<10}")
            print("-" * 50)
            # Ürün Bilgilerini Yazdır
            for i in myDict:
                print(f"{i:<10} {myDict[i].get('Urun', 'Bilinmiyor'):<20} {myDict[i].get('toplam stok', 'Bilinmiyor'):<10} {myDict[i].get('urun fiyati', 'Bilinmiyor'):<10}")       
        def productUpdate(): #urun update
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
        def menu(): #menu sistemi
            found = False
            while True:
                print("\n1. Ürün ekle")
                print("2. Ürünleri görüntüle")
                print("3. Ürün güncelle")
                print("4. Ürün sil")
                print("5. Çıkış")
                try:
                    secim = int(input("Seçiminiz: "))
                    if secim == 1:
                        break
                    elif secim == 2:
                        productShow()
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
urunSistemi()
            
