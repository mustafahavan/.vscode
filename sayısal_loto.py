from random import randint
print("Sayısal Loto")
kolon = []

for j in range (1,100):
    for i in range(1, 7):
        x=randint(1, 49)
        kolon.insert(i, x)
        kolon.sort()
        myset = set(kolon)
        a = len(kolon)
        b = len(myset)

    if(a==b):
        print(kolon)
        break