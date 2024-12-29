"""Mini Proje: Kullanıcı Giriş Sistemi
Kullanıcıdan giriş bilgileri alın:
Kullanıcı adı ve şifre.
Doğru kullanıcı adı: admin, şifre: 12345.
Kullanıcı en fazla 3 kez şifre girebilir.
Şifre yanlışsa kalan hakkı göster.
Şifre doğru girilirse "Giriş Başarılı" yazdır.
"""

def userPanel():
    

    for i in range(3):                        
            usId = input ("Kullanici adinizi giriniz : ")
            psw = input("Sifrenizi giriniz : ")
            if usId == "admin" and psw == "12345":
                True
                print("Kullanici adi ve sifre dogru... Sisteme yonlendiriliyorsunuz.")
                
            else:
                print("Hatali giris yaptiniz, lutfen tekrar deneyiniz\n"
                    f"Kalan giris hakkiniz {3-(i+1)}")
            
userPanel()
    