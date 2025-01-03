def menu():

    while True:
        print("1.Toplama")
        print("2.Cikarma")
        print("3.Carpma")
        print("4.Bolme")
        print("5.Cikis")
        try:
            userInput = int(input("Yapmak istediginiz islemi seciniz = "))
            if userInput == 1:
                toplamaMak()
            elif userInput ==2:
                cikartmaMak()
            elif userInput ==3:
                carpmaMak()
            elif userInput ==4:
                bolmeMak()
            elif userInput ==5:
                print("Hesap Makinesinden cikiliyor")
                break
            else:
                print("Geçersiz seçim. Lütfen 1-5 arasında bir sayı giriniz.")
        except ValueError:
            print("Lutfen gecerli bir deger giriniz...")

def inputChecks():
    while True:
        try:
            nums1 = float(input("1. sayiyi giriniz : "))
            nums2 = float(input("2. sayiyi giriniz : "))
            return nums1,nums2
        except ValueError:
            print("Lutfen bir sayi degeri giriniz...")
def toplamaMak():
    nums1,nums2 = inputChecks()
    totalNums = sum(nums1,nums2)
    print(f"{nums1}+{nums2} = {totalNums}")
    return totalNums
def cikartmaMak():
    nums1,nums2 = inputChecks()
    value = nums1-nums2
    print(f"{nums1}-{nums2} = {value}")
    return value
def carpmaMak():
    nums1,nums2 = inputChecks()
    value = nums1*nums2
    print(f"{nums1}*{nums2} = {value}")
    return value
def bolmeMak():
    nums1,nums2 = inputChecks()
    try:
        value = nums1/nums2
        print(f"{nums1}/{nums2} = {value}")
        return value
    except ZeroDivisionError:
        print("Bir sayi 0 a bolunemez, tekrar deneyiniz...")   

menu()