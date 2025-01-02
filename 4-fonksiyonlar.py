# Alıştırma 1: İki Sayının Bölümünü Bulma
# Kullanıcıdan iki sayı alın ve bu sayıları bölen bir fonksiyon yazın.
# Hata Yönetimi:
# Sıfıra bölme hatasını (ZeroDivisionError) kontrol edin.
# Yanlış türde veri girilirse (ValueError) kullanıcıya açıklayıcı mesaj verin.
def divisionNums(num1,num2):
    try:
        sonuc = num1 / num2
    except ValueError:
        print("Lutfen sadece sayi giriniz....")
        return divisionNums()
    except ZeroDivisionError:        
        sonuc=None
        return f"Bolen sayi sifir olamaz..Lutfen tekrar bir deger giriniz..."
    else:                      
        return f"{num1}/{num2} = {sonuc}"
try:
    userNum1 = float(input("Birinci sayıyı giriniz: "))
    userNum2 = float(input("İkinci sayıyı giriniz: "))
    print(divisionNums(userNum1,userNum2))
except ValueError:
    print("Hata: Lütfen geçerli bir sayı giriniz!")


