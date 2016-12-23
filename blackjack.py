import random

deste = {"As": 1, "İkili": 2, "Üçlü": 3, "Dört": 4, "Beşli": 5, "Altılı": 6, "Yedili": 7, "Sekizli": 8, "Dokuzlu": 9,
         "Onlu": 10, "Vale": 10, "Kız": 10, "Papaz": 10}
kart_turu = {"Kupa", "Maça", "Sinek", "Karo"}


def kart_sec():
    kart = random.choice(kart_turu) + random.choice(deste)
    return kart


secilmis_kart = kart_sec()


def dagitici():
    acik_kart = random.choice(secilmis_kart)
    kapali_kart = random.choice(secilmis_kart)
    dagitici_top = acik_kart + kapali_kart
    return acik_kart, kapali_kart, dagitici_top


def oyuncu():
    kart1 = random.choice(secilmis_kart)
    kart2 = random.choice(secilmis_kart)
    oyuncu_toplam = kart1 + kart2
    return kart1, kart2, oyuncu_toplam


def kart_cekme():
    ek_kart = random.choice(secilmis_kart)
    return ek_kart
