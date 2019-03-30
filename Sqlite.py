# import sqlite3 as sql
# db = sql.connect(r"D:\muratHANCI\iedb.db")
# cursor = db.cursor()
# cursor.execute("SELECT * FROM V_HESAP")

def SozlukGetir(tabloid):
    import sqlite3 as sql
    db = sql.connect(r"D:\muratHANCI\iedb.db")
    cursor = db.cursor()
    cursor.execute("SELECT sozluk_id,sozluk_adi FROM HSP_SOZLUK WHERE tablo_ID = {}".format(tabloid))
    liste = cursor.fetchall()
    return liste

# print(SozlukGetir(2))

for item,ay in SozlukGetir(2):
    print(item,"-",ay)

ayGiris = input("ay verisini  giriniz")

for item,ay in SozlukGetir(1):
    print(item,"-",ay)

KalemGirisi = input("Kalem verisini giriniz")
TutarGirisi = input("tutarı giriniz")

SORGU = """