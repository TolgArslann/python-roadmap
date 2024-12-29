def easyQuest(): # Kolay: Bir liste oluştur ve her elemanını ekrana yazdır.
    list = []
    for i in range(100):
        userInput = input("Cikis icin (q)"
                          f"\nListe elemanini giriniz :")
        if userInput == "q":
            break        
        list.append(userInput)


    print(list)
def mediumQuest(): # Orta: Bir liste içindeki tekrar eden elemanları bir küme kullanarak kaldır.
    list = [1, 5, 6, 12, 1, 12, "a", "y", "n", "t", "y"]
    tekrarList = set()
    otherList = set()
    for i in range(len(list)):
        for y in range(len(list)):
            if not i == y:
                if list[i] == list [y]:
                    tekrarList.add(list[i])
                else:
                    otherList.add(list[i])
                    
    print(tekrarList)
    print(otherList)

def medHardQuest(): # Orta Zor: Bir sözlükte bir kişinin adını, yaşını ve mesleğini sakla, ardından bu bilgileri ekrana yazdır.
    mesDict = {"Isim ": "Tolga",
               "Soyisim":"Arslan", 
               "Yas": "32"}
    print(mesDict)

def harderstQuest(): # Zor: Kullanıcıdan aldığı kelimeleri bir demet içinde sakla ve alfabetik sırayla yazdır.
    user_list = []
    while True:
        user_input = input("Cikis icin (q)"
            "Listeye eklemek istediginiz elemani yaziniz : ")        
        if user_input.isdigit():
            print("Sadece kelime giriniz...")
        elif user_input == "q":            
            break
        user_list.append(user_input)
    user_list.sort()
    user_tuple = tuple(user_list)
    print(user_tuple)

harderstQuest()


        
        

