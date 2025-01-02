# Alıştırma 1: İki Sayının Bölümünü Bulma
# Kullanıcıdan iki sayı alın ve bu sayıları bölen bir fonksiyon yazın.
# Hata Yönetimi:
# Sıfıra bölme hatasını (ZeroDivisionError) kontrol edin.
# Yanlış türde veri girilirse (ValueError) kullanıcıya açıklayıcı mesaj verin.
def divisionNums():
    num1 = float(input("Bolunecek sayiyi giriniz :"))
    num2 = float(input("Bolecek sayiyi giriniz :"))    
    try:
        value1= num1
        value2= num2
    except ValueError:
        print("Lutfen sadece sayi giriniz....")
        return
    except ZeroDivisionError:
        print("Bolen sayi sifir olamaz..Lutfen tekrar bir deger giriniz...")
        return
    else:
        sonuc = num1 / num2                       
        print(f"{num1}/{num2} = {sonuc}")
divisionNums()

