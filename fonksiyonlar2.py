# def tumsayi(sayi):
#     sayi = sayi.replace(",","").replace(".","")
#     if len(sayi)%3 > 0:
#         sayi = sayi.zfill(3-len(sayi)%3+len(sayi))
#     liste = [sayi[i*3:(i*3)+3] for i in range(int(len(sayi)/3))]
#     liste.reverse()
#     return okuma(liste)
# def okuma(liste):
#     birler = {"0":"","1":"Bir","2":"İki","3":"Üç","4":"Dört","5":"Beş","6":"Altı"}
#     onlar = {"0":"","1":"On","2":"Yirmi","3":"Otuz","4":"Kırk","5":"Elli","6":"Altmış"}
#     basamak = {0:"",1:"Bin",2:"Milyon",3:"Milyar"}
#     sonuc = ""
#     okuma = ""
#     for i in range(len(liste)):      
#         if liste[i][0] != "1" and liste[i][0] != "0":
#             okuma += birler[liste[i][0]] + "Yüz"
#         elif liste[i][0] == "1":
#             okuma += " Yüz"
#         okuma += onlar[liste[i][1]] 
#         if i !=  1 and liste[i][2] != "1":
#             okuma += birler[liste[i][2]]
#         sonuc = okuma + " " + basamak[i] +  sonuc
#         okuma = ""
#     return sonuc

# # print(tumsayi(input("Sayıyı Giriniz")))


# hesap = lambda a,b:a+b
# print(hesap(2,4))



def disari(b):
    a = 10
    def iceri(c):
        global a
        a=20
        return a
    return a
a = 5
print(disari(a))
print(a)