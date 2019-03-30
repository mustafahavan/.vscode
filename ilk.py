# print("hello")
# print("merhaba")

# var1 = 123456789
# deneme = type(var1)
# var2 = 5.5
# var3 = 5.9j
# var4 = "str"
# var5 = []
# var6 = ()
# var7 ={}
# print(bin(2))
# print(oct(2))
# print(2)
# print(hex(2))

# print(type(var1))
# print(type(var2))
# print(type(var3))
# print(type(var4))
# print(type(var5))
# print(type(var6))
# print(type(var7))
# print(type(deneme))

# a = 1
# b = 1
# for i in range(0, 100):
#     c = a+b
#     print(c)
#     a=b
#     b=c
# print()
# a = int(input("1. Sayıyı Giriniz"))
# b = int(input("2. Sayıyı Giriniz"))
# a = int(a)
# b = int(b)
# c= a+b
# print(c)
# print(c,a,b,sep="-",end=".")

sesli_harfler = 'aeıioöuü'
sayaç = 0

kelime = input('Bir kelime girin: ')

for harf in kelime:
    if harf in sesli_harfler:
        sayaç += 1

mesaj = '{} kelimesinde {} sesli harf var.'
print(mesaj.format(kelime, sayaç))