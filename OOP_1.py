class Kedi:
    familya = "felis"
    def __init__(self,ad="",tuy="",goz="",renk=""):
        self.tuy = tuy
        self.goz = goz
        self.ad = ad
        self.renk = renk
    def beslenme(self):
        self.miyavla()
        print(self.ad,"beslendi")
    def miyavla(self):
         print(self.ad,"miyavladı")        
duman = Kedi(ad="duman",tuy="kısa",goz="yeşil",renk="gri")
print(duman.goz)
duman.beslenme()
Şeytan = Kedi()
Şeytan.ad = "Şeytan"
Şeytan.beslenme()

