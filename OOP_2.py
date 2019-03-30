# Mars = """Korkma, sönmez bu şafaklarda yüzen al sancak;
# Sönmeden yurdumun üstünde tüten en son ocak.
# O benim milletimin yıldızıdır, parlayacak;
# O benimdir, o benim milletimindir ancak.

# Çatma, kurban olayım, çehreni ey nazlı hilal!
# Kahraman ırkıma bir gül! Ne bu şiddet, bu celal?
# Sana olmaz dökülen kanlarımız sonra helal…
# Hakkıdır, hakk'a tapan, milletimin istiklal!

# Ben ezelden beridir hür yaşadım, hür yaşarım.
# Hangi çılgın bana zincir vuracakmış? Şaşarım!
# Kükremiş sel gibiyim, bendimi çiğner, aşarım.
# Yırtarım dağları, enginlere sığmam, taşarım.

# Garbın afakını sarmışsa çelik zırhlı duvar,
# Benim iman dolu göğsüm gibi serhaddim var.
# Ulusun, korkma! Nasıl böyle bir imanı boğar,
# ‘Medeniyet!' dediğin tek dişi kalmış canavar?

# Arkadaş! Yurduma alçakları uğratma, sakın.
# Siper et gövdeni, dursun bu hayasızca akın.
# Doğacaktır sana va'dettigi günler hakk'ın…
# Kim bilir, belki yarın, belki yarından da yakın.

# Bastığın yerleri ‘toprak!' diyerek geçme, tanı:
# Düşün altında binlerce kefensiz yatanı.
# Sen şehit oğlusun, incitme, yazıktır, atanı:
# Verme, dünyaları alsan da, bu cennet vatanı.

# Kim bu cennet vatanın uğruna olmaz ki feda?
# Şuheda fışkıracak toprağı sıksan, şuheda!
# Canı, cananı, bütün varımı alsın da hüda,
# Etmesin tek vatanımdan beni dünyada cüda.

# Ruhumun senden, ilahi, şudur ancak emeli:
# Değmesin mabedimin göğsüne namahrem eli.
# Bu ezanlar-ki şahadetleri dinin temeli,
# Ebedi yurdumun üstünde benim inlemeli.

# O zaman vecd ile bin secde eder -varsa- taşım,
# Her cerihamdan, ilahi, boşanıp kanlı yaşım,
# Fışkırır ruh-i mücerred gibi yerden na'şım;
# O zaman yükselerek arsa değer belki başım.

# Dalgalan sen de şafaklar gibi ey şanlı hilal!
# Olsun artık dökülen kanlarımın hepsi helal.
# Ebediyen sana yok, ırkıma yok izmihlal:
# Hakkıdır, hür yaşamış, bayrağımın hürriyet;
# Hakkıdır, hakk'a tapan, milletimin istiklal!

# Mehmet Âkif Ersoy"""

# liste = ["hilal","helal","yıldız","millet","istiklal","kan"]
class HarfSayaci:

    def __init__(self):
        self.sesli_harf = "aeiıoüuö"
        self.sessiz_harf = "qwrtypğsdfghjklşzxcvbnmç"
        self.turkce = ""
        self.sesli_sayac = 0
        self.sessiz_sayac = 0

    def kelime_sor(self):
        return input("Bir kelime Girin")

    def seslidir(self,harf):
        return harf in self.sesli_harf

    def sessizdir(self,harf):
        return harf in self.sessiz_harf

    def arttır(self):
        for harf in self.kelime:
            if self.seslidir(harf):
                self.sesli_sayac += 1
            if self.sessizdir(harf):
                self.sessiz_sayac += 1
        return (self.sessiz_sayac,self.sesli_sayac)

    def ekrana_bas(self):
        sayim = self.arttır()
        mesaj = "{} kelimesinde {} sesli harf ve {} sessiz harf vardır."
        print(mesaj.format(self.kelime,sayim[1],sayim[0]))

    def çalıştır(self):
        self.kelime = self.kelime_sor()
        self.ekrana_bas()

if __name__ == '__main__':
    sayac = HarfSayaci()
    sayac.çalıştır()