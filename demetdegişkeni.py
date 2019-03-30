# demet = (2,2)
# demet[1] = 56
# print(demet)

# sozluk = {"book":"kitap","apple":"elma"}

# print(sozluk["book"])

alfabe = "abcdefghiıjklmnoöprsiqtuvwyz"

cevrim = {i : alfabe.index(i) for i in alfabe}
print(cevrim.keys())
print(cevrim.value())
print(cevrim.items())
# print(cevrim)
# isimlistesi = ["ahmet","ışıl","berkecan","ışınsu","çisem","orçun","ömer"]
# sozluk = {}
# sozluk = sozluk.fromkeys(isimlistesi)

# print(sozluk)
# cevrim.update({"â":29})
# print(cevrim)


# print(cevrim.get("o"))

# isimlistesi = ["ahmet","ışıl","berkecan","ışınsu","çisem","orçun","ömer"]
# isimlistesi.sort()
# print(isimlistesi)

# print(sorted(isimlistesi,key = lambda x : cevrim.get(x[0])))