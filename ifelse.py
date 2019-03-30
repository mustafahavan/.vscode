# a = int(input("sayıyı giriniz"))

# if a%2==0 :
#     print("sayı çifttir")
# else:
#     print("sayı tektir")



# a = int(input("sayıyı giriniz"))

# if not a%2==0 :
#     print("sayı tektir")
# else:
#     print("sayı çiftir")

 # not 1 and 2 or3  sıralaması


# notu = int(input("notunuzu giriniz"))
# sonuc = ""

if notu < 25 and notu >=0:
    sonuc="FF"
elif notu < 45 and notu >=25:
    sonuc="FD"
elif notu < 55 and notu >= 45:
    sonuc="DD"
elif notu < 60 and notu >=55:
    sonuc="DC"
elif notu < 69 and notu >=60:
    sonuc="CC"
elif notu < 80 and notu >=70:
    sonuc="CB"
elif notu < 85 and notu >=80:
    sonuc="BB"
elif notu < 90 and notu >=85:
    sonuc="BA"
elif notu < 100 and notu >=90:
    sonuc="AA"
else:
    sonuç = "not hesaplama"
print("notunuz {} iyi günler dileriz".format(sonuc))
    


vize1 = int(input("I.vize notunuzu giriniz"))
vize2 = int(input("II.vize notunuzu giriniz"))
vize1 = int(input("final notunuzu giriniz"))
notu = raund(vize1*0.3)+(vize2*0.3)+(final*0.4)
sonuc = ""
print()