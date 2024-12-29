"""Mini Proje: Kullanıcı Giriş Sistemi
Kullanıcıdan giriş bilgileri alın:
Kullanıcı adı ve şifre.
Doğru kullanıcı adı: admin, şifre: 12345.
Kullanıcı en fazla 3 kez şifre girebilir.
Şifre yanlışsa kalan hakkı göster.
Şifre doğru girilirse "Giriş Başarılı" yazdır.
"""
import getpass

def userPanel():        
    """
    Kullanıcıdan kullanıcı adı ve şifre alır.
    Doğru bilgiler girildiğinde giriş yapılır.
    Yanlış bilgiler girildiğinde 3 deneme hakkı tanınır.
    """
    for i in range(3):
        # Kullanıcı adı girişi                      
        usId = input ("Kullanici adinizi giriniz : ")
        # Sifre Girisi-Karakterler gizleniyor
        psw = getpass.getpass("Sifrenizi giriniz : ")
        #Kullanici adi ve sifre kontrolu
        if usId == "admin" and psw == "12345":            
            print("Kullanici adi ve sifre dogru... Sisteme yonlendiriliyorsunuz.")
            break                
        else:
            kalan_hak = 2-i
            print(f"Hatali giris yaptiniz, lutfen tekrar deneyiniz\n"
                f"Kalan giris hakkiniz {kalan_hak}")
    else:
        print("Giris hakkiniz tukendi.Daha sonra tekrar deneyiniz.")
            
userPanel()
    