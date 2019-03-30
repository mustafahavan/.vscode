# def fonksiyon():
#     print("merhaba")
# fonksiyon()

# def carp(sayi=1):
#     print(sayi*sayi)

# def topla(a=0,b=0):
#     print("{} + {} = {}".format(a,b,a+b))
# topla()




liste = [20,10,40,30,0]
# print(*liste,sep="\n")
def ortalama(*args,katsayı=0):
    toplam = 0
    for item in args:
        toplam += item
    return (toplam/len(args)*katsayı)

print(ortalama(20,85,625,45,85,katsayı=4)*5)    