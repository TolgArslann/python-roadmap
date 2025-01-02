# Alıştırma 1: İki Sayının Bölümünü Bulma
# Kullanıcıdan iki sayı alın ve bu sayıları bölen bir fonksiyon yazın.
# Hata Yönetimi:
# Sıfıra bölme hatasını (ZeroDivisionError) kontrol edin.
# Yanlış türde veri girilirse (ValueError) kullanıcıya açıklayıcı mesaj verin.
def divisionNums(num1,num2):
    try:
        sonuc = num1 / num2
    except ZeroDivisionError:
        print(f"Bolen sayi sifir olamaz..Lutfen tekrar bir deger giriniz...")     
        return None
    else:                      
        return f"{num1}/{num2} = {sonuc}"
def getUserInput():
    while True:
        try:
            num1 = float(input("Birinci sayıyı giriniz: "))
            num2 = float(input("İkinci sayıyı giriniz: "))
            return num1,num2
        except ValueError:
            print("Hata: Lütfen geçerli bir sayı giriniz!")
def main():
    num1, num2 = getUserInput()
    result = divisionNums(num1,num2)
    if result is not None:
        print(f"Sonuç: {num1} / {num2} = {result}")
if __name__ == "__main__":
    main()



