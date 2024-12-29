

def pozNeg():
    """
    1. Koşullu İfadeler (if-elif-else)
    Kolay:
    Kullanıcıdan bir sayı al ve bu sayının pozitif mi, negatif mi yoksa sıfır mı olduğunu kontrol et.
    """

    user_num = int(input("Bir sayi giriniz : "))
    if user_num > 0:
        print("Pozitif")
    elif user_num < 0:
        print("Negatif")
    else:
        print("Notr")

def ageCont():
    """
    Orta:
    Kullanıcıdan yaşını al ve yaşına göre kategori belirle:

    0-12: Çocuk
    13-19: Genç
    20-64: Yetişkin
    65 ve üzeri: Yaşlı
    """
    user_age = int(input("Lutfen yasinizi giriniz : "))

    if user_age > 64:
        print("Yasli")
    elif user_age > 19:
        print("Yetiskin")
    elif user_age > 12:
        print("Genc")
    elif user_age >= 0:
        print("Cocuk")
    else:
        print("Gecerli bir deger giriniz...")

def pswCont():
    """
    Orta Zor:
    Kullanıcıdan bir şifre al ve şu kurallara uyup uymadığını kontrol et:

    Şifre en az 8 karakter uzunluğunda olmalı.
    En az bir büyük harf ve bir küçük harf içermeli.
    En az bir sayı içermeli.
    """
    user_password = input("Lütfen bir şifre giriniz: ")

    # Uzunluk kontrolü
    if len(user_password) < 8:
        print("Şifre en az 8 karakter uzunluğunda olmalıdır.")
        return

    # Karakter türü kontrolleri
    has_upper = False
    has_lower = False
    has_digit = False

    for char in user_password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True

    # Sonuç kontrolü
    if has_upper and has_lower and has_digit:
        print("Şifre geçerli.")
    else:
        print("Şifre, en az bir büyük harf, bir küçük harf ve bir sayı içermelidir.")


def twoNum():
    """
    Zor:
    Kullanıcıdan aldığı iki sayıyı karşılaştıran bir program yaz:

    Eğer iki sayı eşitse, ekrana "Eşit" yaz.
    Eğer birinci sayı büyükse, farkını yaz.
    Eğer ikinci sayı büyükse, oranlarını yaz
    """
    user_num1 = int(input("Lutfen ilk sayiyi giriniz :"))
    user_num2 = int(input("Lutfen ikinci sayiyi giriniz :"))

    if user_num1 == user_num2:
        print("Girdiginiz iki deger birbirine esitler")
    elif user_num1 > user_num2:
        new_num = user_num1 - user_num2
        print(f"\nGirilen sayilar:\n"
            f"Sayi 1 = {user_num1}\n"
            f"Sayi 2 = {user_num2}\n"
            f"Sayilarin farki = {new_num}")
    elif user_num1 < user_num2:
        new_or = user_num2/user_num1
        print(f"\nGirilen sayilar:\n"
            f"Sayi 1 = {user_num1}\n"
            f"Sayi 2 = {user_num2}\n"
            f"Sayilarin Orani = {new_or}")

