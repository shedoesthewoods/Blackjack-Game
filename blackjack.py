import random

kart_degerleri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
kart_turu_sayisi = 4
kart_tur = ["Karo", "Maça", "Sinek", "Kupa"]

def deste_degerleri_olusturma_fonksiyonu():
    kartlar = kart_degerleri * kart_turu_sayisi
    return kartlar

def kart_turu():
    secilen_tur = random.choice(kart_tur)
    return secilen_tur


deste = deste_degerleri_olusturma_fonksiyonu()


def kart_sil(string):  # desteden secilen kartı siler
    return deste.remove(string)


def dagiticinin_kartlar():
    dgt_acik_kart = random.choice(deste)
    kart_sil(dgt_acik_kart)
    dgt_kapali_kart = random.choice(deste)
    kart_sil(dgt_kapali_kart)
    return dgt_acik_kart, dgt_kapali_kart


def oyuncunun_kartlar():
    oyn_kart_1 = random.choice(deste)
    kart_sil(oyn_kart_1)
    oyn_kart_2 = random.choice(deste)
    kart_sil(oyn_kart_2)
    return oyn_kart_1, oyn_kart_2


def kart_cekme():
    ekstra_kart = random.choice(deste)
    kart_sil(ekstra_kart)
    return ekstra_kart


def dagitici_kart_cekme():
    dgt_extra_kart = random.choice(deste)
    kart_sil(dgt_extra_kart)
    return dgt_extra_kart


# dgt_kart_cekme_degeri = 17


def oyun():
    tekrar = "e"

    while tekrar.lower() == "e":
        dgt_kartlar = list(dagiticinin_kartlar())
        oyn_kartlar = list(oyuncunun_kartlar())
        print("Dağıtıcının açık kartı ", dgt_kartlar[0])
        print("Kartlarınız {} {} ve {} {}, toplamda: {}".format(oyn_kartlar[0], kart_turu(), oyn_kartlar[1], kart_turu(), sum(oyn_kartlar)))
        ek_kart = input("Kart (k) veya Pas (p):")

        while ek_kart.lower() == "k":
            ekstra_kart = kart_cekme()
            oyn_kartlar.append(ekstra_kart)
            print("Çekilen kart: {} {}, yeni toplam: {}".format(ekstra_kart, kart_turu(), sum(oyn_kartlar)))
            if sum(oyn_kartlar) == 21:
                print("Blackjack! Sıra dağıtıcıda.")
                print(
                    "Dağıtıcının kartları {} {} ve {} {}, toplam {}".format(dgt_kartlar[0], kart_turu(), dgt_kartlar[1], kart_turu(), sum(dgt_kartlar)))
                if sum(dgt_kartlar) == 21:
                    print("Berabere!")
                    break
                elif sum(dgt_kartlar) > 21:
                    print("Kazandınız! Dağıtıcı battı.")
                    break
                elif sum(dgt_kartlar) > 17:
                    if sum(oyn_kartlar) > sum(dgt_kartlar):
                        print("Kazandınız! Dağıtıcı battı.")
                        break
                    elif sum(oyn_kartlar) < sum(dgt_kartlar):
                        print("Battınız. Dağıtıcı kazandı!")
                        break
                    else:
                        print("Berabere!")
                        break
                else:
                    while sum(dgt_kartlar) < 17:
                        dgt_ek_kart = dagitici_kart_cekme()
                        dgt_kartlar.append(dgt_ek_kart)
                        print("Dağıtıcının kartları {} {}, toplam {}".format(dgt_kartlar, kart_turu(), sum(dgt_kartlar)))
                    break
            elif sum(oyn_kartlar) > 21:
                print("Battınız. Dağıtıcı kazandı!")
                break
            ek_kart = input("Kart (k) veya Pas (p):")

        while ek_kart.lower() == "p":
            print("Sıra dağıtıcıda.")
            print("Dağıtıcının kartları {} {} ve {} {}, toplam {}".format(dgt_kartlar[0], kart_turu(), dgt_kartlar[1], kart_turu(), sum(dgt_kartlar)))
            if sum(dgt_kartlar) == 21:
                print("Battınız. Dağıtıcı kazandı!")
                break
            elif sum(dgt_kartlar) > 21:
                print("Dağıtıcı battı. Kazandınız!")
                break
            elif sum(dgt_kartlar) > 17:
                if sum(oyn_kartlar) > sum(dgt_kartlar):
                    print("Kazandınız! Dağıtıcı battı.")
                    break
                elif sum(oyn_kartlar) < sum(dgt_kartlar):
                    print("Battınız. Dağıtıcı kazandı!")
                    break
                else:
                    print("Berabere!")
                    break
            else:
                while sum(dgt_kartlar) <= 17:
                    dgt_ek_kart = dagitici_kart_cekme()
                    dgt_kartlar.append(dgt_ek_kart)
                    print("Dağıtıcının kartları {}, toplam {}".format(dgt_kartlar, sum(dgt_kartlar)))
                    if sum(dgt_kartlar) > 21:
                        print("Kazandınız! Dağıtıcı battı.")
                        break
                    elif sum(dgt_kartlar) == 21:
                        print("Berabere!")
                        break
                    else:
                        if sum(oyn_kartlar) > sum(dgt_kartlar):
                            print("Kazandınız! Dağıtıcı battı.")
                            break
                        elif sum(oyn_kartlar) < sum(dgt_kartlar):
                            print("Battınız. Dağıtıcı kazandı!")
                            break
                        else:
                            print("Berabere!")
                            break
                break

        tekrar = input("Tekrar oynamak ister misiniz? (e/h):")

oyun()
