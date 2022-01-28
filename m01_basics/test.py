


class SMS_tarolo():
    def beerkezo_uzenet_hozzaadasa(kuldo_szama, erkezesi_ido, SMS_szovege):
        olvasott_e = True
        uzenet = (olvasott_e, kuldo_szama, erkezesi_ido, SMS_szovege)
        bejovo_uzenetek.append(uzenet)
        return bejovo_uzenetek
        


#   # Készít egy új rendezett 4-est az SMS számára,
#   # és beszúrja őket a tárolóba a többi üzenet után.
#   # Az üzenet készítésénél az olvasott_e állapotát
#   #    hamisra (False) állítja.

# bejovo_uzenetek.uzenetek_szama()
#   # Visszatér a bejovo_uzenetek tárolóban lévő SMS-ek számával

# bejovo_uzenetek.olvasatlan_uzenetek_indexeinek_lekerese()
#   # Visszatér az összes olvasatlan SMS indexét tartalmazó listával.

# bejovo_uzenetek.uzenet_lekerese(i)
#   # Visszatér az uzenet[i]-hez tartozó (kuldo_szama, erkezesi_ido, SMS_szovege) 4-essel.
#   # Az üzenet státuszát olvasottra állítja.
#   # Ha nincs üzenet az i. indexen, akkor a visszatérési érték None.

# bejovo_uzenetek.torol(i)     # Kitörli az i. pozícióban álló üzenetet.
# bejovo_uzenetek.mindent_torol()   # Kitörli az összes üzenetet a bejövő SMS-ek tárolójából.

bejovo_uzenetek = []

olvasott_e = False
kuldo_szama = '06305645575'
erkezesi_ido = '2022.01.28.05:30'
SMS_szovege = 'Hello, szia, szevasz'

print(SMS_tarolo.beerkezo_uzenet_hozzaadasa(
    kuldo_szama, erkezesi_ido, SMS_szovege))