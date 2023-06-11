import random
import time
import os
os.system("clear")
print("ElxTc açılıyor …⁠ᘛ⁠⁐̤⁠ᕐ⁠ᐷ")
time.sleep(3)
os.system("clear")
while True:
    print("|---------------------|(⁠⊙⁠_⁠◎⁠)")
    print("| 1 => TC oluşturmak. |")
    print("| 2 => TC sorgulamak. |")
    print("|---------------------|")

    abc=int(input("Hangisini:"))
 
    def oluş():

        while True:
            os.system("clear")
            print(" __________________________________________________ ")
            print(" //////////////   //              \\  -⁠ᄒ⁠ᴥ⁠ᄒ⁠-  //    ")
            print(" //               //               \\        //     ")
            print(" //               //                \\      //      ")
            print(" ///////////////  //                 \\    //       ")
            print(" //               //                  \\  //        ")
            print(" //               //                  //  \\        ")
            print(" ///////////////  /////////////      //    \\       ")
            print("__________________________________________________  ")
            try:
                adet=int(input("|Kaç Adet TC kimlik No İstersiniz?|=>"))
            except ValueError:
                print("Lütfen sayı giriniz.")
                print("ฅ⁠^⁠•⁠ﻌ⁠•⁠^⁠ฅ")
                continue
                break 
            
            print("TAMAMDIR")
            print("(⁠^⁠.⁠_⁠.⁠^⁠)⁠ﾉ")
            time.sleep(3)
            i=1

            while i<=adet:
                a1=random.randint(1,9)
                a2=random.randint(0,9)
                a3=random.randint(0,9)
                a4=random.randint(0,9)
                a5=random.randint(0,9)
                a6=random.randint(0,9)
                a7=random.randint(0,9)
                a8=random.randint(0,9)
                a9=random.randint(0,9)
                a10=((((a1+a3+a5+a7+a9)*7)-(a2+a4+a6+a8))%10)
                a11=((a1+a2+a3+a4+a5+a6+a7+a8+a9+a10)%10)
                print("________________________________________")
                print(i,".TC KİMLİK NO:",a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11)
                print("________________________________________")
                i=i+1
                time.sleep(0.5)
            print("NOT:!!!Numaraların aralarında boşluklar vardır!!!")
            print("<⁠(⁠￣⁠︶⁠￣⁠)⁠↗")
                
            break
        
   
            
def sorgu():
    def encodeTc(tc):
        sum = 0
        for i in tc:
            sum += int(i)
        tc+= str(sum)[-1]
        return tc
    def decodeTc(girilen_tc):
        if len(girilen_tc)!=11:
           print("Geçerli bir TC Kimlik Numarası giriniz!")
           return
        encodedtc=encodeTc(girilen_tc[0:10])
        return girilen_tc == encodedtc
    def tclogin():
        a = input("Tc giriniz:")
        result = decodeTc(a)
        if result == None:
            quit()
        elif not result:
            print("Girdiğiniz TC Kimlik numarası gerçek değildir.")
        elif result:
            print("Geçerli Bir TC Kimlik numarası girdiniz.")
    tclogin()
if ( abc == 1 ):
    oluş()
if ( abc == 2 ):
    sorgu()

    if(abc != int(1 and 2)):
        print("Lütfen 1 veya 2 giriniz.")
        print("(⁠#ー⁠_⁠ー)")
        
    break 
