def easyQues(): # Kolay: 1’den 10’a kadar olan sayıları yazdır.  
    for i in range(10):
        print(f"{i+1}")

def medQues(): # Orta: Bir liste içindeki sayıların toplamını hesapla.
    user_list = []    
    for i in range(100):
            user_nums = input("Liste icin bir eleman giriniz (Bitirmek icin (q)): ")
            if user_nums.isdigit():
                convertedNum = int(user_nums)
                if convertedNum >= 0:
                    user_list.append(convertedNum)
                else:
                     print("Pozitif bir deger giriniz.")
            elif user_nums == "q":
                 break
            else:
                 print("Lutfen bir sayi giriniz...")
    print(f"Girdiginiz Liste = {user_list}")
    total = sum(user_list)
    print(f"Listenizin elemanlarinin toplami = {total}")

def medQues2(): # Orta Zor: Bir while döngüsü kullanarak kullanıcıdan sürekli sayı al ve -1 girildiğinde döngüyü sonlandır.
     numbers = []
     while True:        
            try:              
                user_input = int(input("Bir sayi giriniz : "))
                if user_input == -1:
                    break
                numbers.append(user_input)
            except ValueError:
                print("Lutfen bir sayi giriniz")
            total = sum(numbers)
            print(f"Girilen sayilarin toplami = {total}")

def lastDif(): # Zor: 1’den 100’e kadar olan sayılardan hem 3’e hem 5’e tam bölünebilenleri yazdır.
     sayac=0
     for i in range (1,101):
          if i % 3 == 0 and i % 5 == 0:
               sayac +=1
               print(f"3 ve 5 e bolunen {sayac}. sayi = {i}")
lastDif()
