print("""
 
İşlem seçiniz : 
 
 
1 - Para Çekme
 
2 - Para yatırma
 
3 - Bakiye sorgulama

4 - çıkış

""")
 
 
bakiye=1000
 
while True:
    islem = input('İslem yapmak istediğiniz numara')
    if(islem=="4"):
        print('programdan çıkılıyor ')
        break
    elif (islem=='1'):
        miktar=int(input('Miktar giriniz'))
        if(bakiye-miktar<0):
            print('Yetersiz bakiye')
            continue
        else:
            bakiye = bakiye - miktar
 
            print('Hesabınızdan {} Tl para çektiniz'.format(miktar))
 
    elif(islem=='2'):
        yatacak=int(input('yatırmak istediğiniz miktarı girin'))
        bakiye=bakiye+yatacak
        print('Hesabınıza {} Tl yatırdınız'.format(yatacak))
 
    elif(islem=='3'):
        print('Bakiyeniz {} Tl dir'.format(bakiye))
    
    else:
        print('Geçersiz işlem')