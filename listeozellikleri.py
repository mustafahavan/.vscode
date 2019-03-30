# liste1 = [12,13,43]
# liste2 = liste1
# liste2[2] = "hello"
# print(liste1)

# liste1 = [12,13,43]
# liste2 = liste1.copy()
# liste2[2] = "hello"
# print(liste2)
# print(liste1)


liste1 = [12,13,43]
liste = [1,2,3,4]

liste1.append(liste)
print(liste1)

liste1.extend(liste)
print(liste)