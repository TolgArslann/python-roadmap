# Alıştırma 1: İki Sayının Bölümünü Bulma
# Kullanıcıdan iki sayı alın ve bu sayıları bölen bir fonksiyon yazın.
# Hata Yönetimi:
# Sıfıra bölme hatasını (ZeroDivisionError) kontrol edin.
# Yanlış türde veri girilirse (ValueError) kullanıcıya açıklayıcı mesaj verin.
def divisionNums():
    num1 = input("Bolunecek sayiyi giriniz :")
    num2 = input("Bolecek sayiyi giriniz :")  
    try:
        value1= float(num1)
        value2= float(num2)
        sonuc = value1 / value2
    except ValueError:
        print("Lutfen sadece sayi giriniz....")
        return divisionNums()
    except ZeroDivisionError:
        print("Bolen sayi sifir olamaz..Lutfen tekrar bir deger giriniz...")
        sonuc=None
        return divisionNums()
    else:                      
        print(f"{num1}/{num2} = {sonuc}")
divisionNums()

