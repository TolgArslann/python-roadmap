# 1. Alıştırmalar:
# Kolay Seviyede
# 	1. Bir sayı alan ve karesini döndüren bir fonksiyon yazın.
# 	2. İki sayıyı toplayan bir fonksiyon oluşturun. Eğer parametrelerden biri sayı değilse bir hata mesajı döndürün.
# 	3. Girilen bir string'in uzunluğunu döndüren bir fonksiyon yazın.
# 	4. Hatalı girişler için özelleştirilmiş bir hata mesajı veren bir fonksiyon yazın (örneğin, negatif sayılar kabul edilmesin).
# Orta Seviyede
# 	1. Girilen bir sayının asal olup olmadığını kontrol eden bir fonksiyon yazın. Eğer giriş bir sayı değilse, hata mesajı gösterin.
# 	2. Liste içerisindeki en büyük sayıyı bulan bir fonksiyon yazın. Liste boşsa özel bir hata fırlatın.
# 	3. Girilen bir sayının faktöriyelini hesaplayan bir fonksiyon yazın. Eğer sayı negatifse hata mesajı döndürün.
# Kısmen Zor Seviyede
# 	1. Girilen bir listenin ortalamasını hesaplayan bir fonksiyon oluşturun. Liste boşsa özel bir hata fırlatın.
# 	2. Bir sözlükte anahtar kelime araması yapan bir fonksiyon yazın. Anahtar bulunamazsa özel bir hata döndürün.
# 	3. Kullanıcıdan aldığınız bir girdiyi bir dosyaya yazdıran bir fonksiyon yazın. Hata durumlarında dosya işlem hatalarını yönetin.
# Zor Seviyede
# 	1. Bir log dosyasına hata kayıtlarını yazdıran bir hata yönetimi sistemi tasarlayın.
# 	2. Bir Python modülü oluşturun: İçinde matematiksel fonksiyonlar (toplama, çarpma vb.) ve hata yönetimi olan bir modül yazın.
# 	3. Kullanıcıdan bir sayı alıp, bu sayıyı bir dosyaya yazan ve hataları yöneten bir uygulama geliştirin.


def squadCalculate():
    num = input("Karesini almak istediginiz sayiyi giriniz")
    try:
        num = float(num)
    except ValueError:
        print("Lutfen bir sayi giriniz...")
        return squadCalculate()
squadCalculate()


