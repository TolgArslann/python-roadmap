# 1. Alıştırmalar:
# Kolay Seviyede
# 	
# 	
# 	
# 	4. Hatalı girişler için özelleştirilmiş bir hata mesajı veren bir fonksiyon yazın (örneğin, negatif sayılar kabul edilmesin).
# Orta Seviyede
# 	
# 	
# 	
# Kısmen Zor Seviyede
# 	1. Girilen bir listenin ortalamasını hesaplayan bir fonksiyon oluşturun. Liste boşsa özel bir hata fırlatın.
# 	2. Bir sözlükte anahtar kelime araması yapan bir fonksiyon yazın. Anahtar bulunamazsa özel bir hata döndürün.
# 	3. Kullanıcıdan aldığınız bir girdiyi bir dosyaya yazdıran bir fonksiyon yazın. Hata durumlarında dosya işlem hatalarını yönetin.
# Zor Seviyede
# 	1. Bir log dosyasına hata kayıtlarını yazdıran bir hata yönetimi sistemi tasarlayın.
# 	2. Bir Python modülü oluşturun: İçinde matematiksel fonksiyonlar (toplama, çarpma vb.) ve hata yönetimi olan bir modül yazın.
# 	3. Kullanıcıdan bir sayı alıp, bu sayıyı bir dosyaya yazan ve hataları yöneten bir uygulama geliştirin.


def squadCalculate():#1. Bir sayı alan ve karesini döndüren bir fonksiyon yazın.
    while True:
        num = input("Karesini almak istediğiniz sayıyı giriniz: ")
        try:
            num = float(num)
            print(f"{num} sayısının karesi: {num**2}")
            break  # İşlem başarılıysa döngüden çık
        except ValueError:
            print("Hata: Lütfen geçerli bir sayı giriniz.")


def sumNums():#2. İki sayıyı toplayan bir fonksiyon oluşturun. Eğer parametrelerden biri sayı değilse bir hata mesajı döndürün.
    while True:
        num1 = input("Ilk sayiyi giriniz : ")
        num2 = input("Ikinci sayiyi giriniz : ")
        try:
            num1 = float(num1)
            num2 = float(num2)
            toplam = num1 + num2
            print(f"{num1} + {num2} = {num1+num2}")
            return toplam 
        except ValueError:
            print("Hata: Lütfen geçerli bir sayı giriniz (örneğin, 5 veya 3.14).")

def lengthString():#3. Girilen bir string'in uzunluğunu döndüren bir fonksiyon yazın.
    while True:
        userInput = input("Lutfen string bir deger giriniz : ")
        if userInput.strip():
            print(f"Girdiğiniz metnin uzunluğu: {len(userInput)} karakterdir.")
            return len(userInput)
        else:
            print("Hata: Boş bir metin girdiniz. Lütfen geçerli bir metin giriniz.")
def primeNumCheck():#1. Girilen bir sayının asal olup olmadığını kontrol eden bir fonksiyon yazın. Eğer giriş bir sayı değilse, hata mesajı gösterin.
    control = 0 
    while True:
        userInput = input("Kontrol etmek istediginiz degeri giriniz : ")
        try:
            userInput = int(userInput)
            if userInput > 0:
                for i in range(2,userInput):
                    if userInput % i == 0:
                        control += 1
                if control == 0:
                    print("asal")
                    break
                else:
                    print("asal degil")
                    break
            else:
                print("lutfen pozitif bir deger giriniz")
        except ValueError:
            print("Hata: Lütfen geçerli bir sayı giriniz (örneğin, 5 veya 3.14).")
def checkBigNum():#2. Liste içerisindeki en büyük sayıyı bulan bir fonksiyon yazın. Liste boşsa özel bir hata fırlatın.
    userList = []
    while True:
        try:
            listLen = int(input("Olusturmak istediginiz listenin uzunlugunu belirtiniz : "))
            if listLen < 0:
                raise ValueError("Liste uzunluğu negatif olamaz.")
            break
        except ValueError as e:
            print(f"Hata : {e}")           
    for i in range(listLen):
        while True:
            try:
                userNums = int(input(f"Eklemek istediginiz {i + 1}. sayiyi giriniz : "))
                userList.append(userNums)
                break
            except ValueError:
                print("Hata: Lütfen geçerli bir sayı giriniz (örneğin, 5 veya 3.14).")
    try:
        maxNum = max(userList)
        print(f"Girdiginiz liste: {userList}, En büyük sayı: {maxNum}")
    except ValueError:
        print("Hata: Liste boş. En büyük sayı bulunamadı.")
def faktsFind(): #3. Girilen bir sayının faktöriyelini hesaplayan bir fonksiyon yazın. Eğer sayı negatifse hata mesajı döndürün.
    while True:
        try:
            userInput = int(input("Faktoriyelini hesaplamak istediginiz degeri giriniz : "))
            if userInput < 0:
                raise ValueError("Faktoriyel 0 dan kucuk olamaz")
            break
        except ValueError as e:
            print(f"Hata : {e}")
    fakt = 1
    for i in range(1,userInput+1):
        fakt *=i
    print(fakt)
    return fakt

faktsFind()

    



        
                   
    
         

    




        






