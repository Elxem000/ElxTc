import random
import time
import os
os.system("clear")
print("ElxOluşturu açılıyor …⁠ᘛ⁠⁐̤⁠ᕐ⁠ᐷ")
time.sleep(3)
os.system("clear")
print(" _______________________________________________________________________________________ ")
print(" //////////////   //               \\ -⁠ᄒ⁠ᴥ⁠ᄒ⁠- //     //////////////      //            \\ ")
print(" //               //                \\      //      //                  // //      \\ \\ ")
print(" //               //                 \\    //       //                  //   //  \\   \\ ")
print(" ///////////////  //                  \\  //        //////////////      //     /\     \\ ")
print(" //               //                   \\//         //                  //            \\ ")
print(" //               //                  //  \\        //                  //            \\ ")
print(" ///////////////  /////////////      //    \\       //////////////      //            \\ ")
print("________________________________________________________________________________________ ")
while true:
    try:
        adet=int(input("Kaç Adet TC kimlik No İstersiniz?"))
    except ValueError:
        print("Lütfen sayı giriniz.")
        print("ฅ⁠^⁠•⁠ﻌ⁠•⁠^⁠ฅ")
return
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
