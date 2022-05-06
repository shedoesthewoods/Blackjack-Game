import random

kart_degerleri = [1, 2, 3, 4, 5, 6, 7, 
        8, 9, 10, "Vale", "Kız", "Papaz"]

kart_turleri = ["Kupa", "Karo", "Maça", "Sinek"]


def deste_olustur():
    deste_listesi = []
    for i in kart_turleri:
        for j in kart_degerleri:
            deste_listesi.append([i, j])
    return deste_listesi

deste = deste_olustur()


def kart_sil(kart):  # desteden seçilen kartı silmek için
    return deste.remove(kart)


def oyuncunun_kartlari():
    kart1 = random.choice(deste)
    kart_sil(kart1)
    kart2 = random.choice(deste)
    kart_sil(kart2)
    return kart1, kart2


def dagiticinin_kartlari():
    acik_kart = random.choice(deste)
    kart_sil(acik_kart)
    kapali_kart = random.choice(deste)
    kart_sil(kapali_kart)
    return acik_kart, kapali_kart


def kart_cekme():  # oyuncu kart çekmek istediğinde kart çeker
    cekilen_kart = random.choice(deste)
    kart_sil(cekilen_kart)
    return cekilen_kart


def dagitici_kart_cekme():  # dağıtıcının kart çekmesi gerektiğinde kart çeker
    dagitici_kart = random.choice(deste)
    kart_sil(dagitici_kart)
    return dagitici_kart


def dagitici_kart_toplamlari(dgt_kartlar):
    toplam = 0
    for i in range(len(dgt_kartlar)):
        if dgt_kartlar[i][1] == "Vale" or dgt_kartlar[i][1] == "Kız" or dgt_kartlar[i][1] == "Papaz":
            dgt_kartlar[i][1] = 10
        if dgt_kartlar[i][1] == "As":
            dgt_kartlar[i][1] = 11
    for j in range(len(dgt_kartlar)):
        if toplam > 21 and dgt_kartlar[j][1] == 11:
            dgt_kartlar[j][1] = 1
        toplam += dgt_kartlar[j][1]
    return toplam


def oyuncu_kart_toplamlari(oyn_kartlar):
    toplam, toplam11 = 0, 0
    for i in range(len(oyn_kartlar)):
        if oyn_kartlar[i][1] == "Vale" or oyn_kartlar[i][1] == "Kız" or oyn_kartlar[i][1] == "Papaz":
            oyn_kartlar[i][1] = 10
        if oyn_kartlar[i][1] == "As":
            oyn_kartlar[i][1] = 1
        toplam += oyn_kartlar[i][1]
        if oyn_kartlar[i][1] == 1:
            toplam11 = toplam + 10
    return [toplam, toplam11]


def blackjack_21():
    tekrar = "e"
    
    dgt_kartlar = list(dagiticinin_kartlari())  # dağıtıcının kartları listesi
    oyn_kartlar = list(oyuncunun_kartlari())  # oyuncunun kartları listesi
    print("Dağıtıcının açık kartı {} {}".format(dgt_kartlar[0][0], dgt_kartlar[0][1]))
    print("Kartlarınız {} {}, {} {} ".format(oyn_kartlar[0][0], oyn_kartlar[0][1], oyn_kartlar[1][0],
                                             oyn_kartlar[1][1]), end="")
    if oyn_kartlar[0][1] == "As" or oyn_kartlar[1][1] == "As":
        print(" (toplam {} ya da {}) ".format(oyuncu_kart_toplamlari(oyn_kartlar)[0],
                                              oyuncu_kart_toplamlari(oyn_kartlar)[1]))
    else:
        print(" (toplam {})".format(oyuncu_kart_toplamlari(oyn_kartlar)[0]))
    if oyuncu_kart_toplamlari(oyn_kartlar)[0] == 21 or oyuncu_kart_toplamlari(oyn_kartlar)[1] == 21:
        print("Blackjack! Sıra dağıtıcıda.")
        print("Dağıtıcının kartları {} {}, {} {}".format(dgt_kartlar[0][0], dgt_kartlar[0][1], dgt_kartlar[1][0],
                                                         dgt_kartlar[1][1]), end="")
        print(" (toplam {})".format(dagitici_kart_toplamlari(dgt_kartlar)))
        while dagitici_kart_toplamlari(dgt_kartlar) < 17:
            yeni_dgt_kart = dagitici_kart_cekme()
            dgt_kartlar.append(yeni_dgt_kart)  # çekilen yeni kart dağıtıcının kartları listesine ekleniyor
            print("Dağıtıcının kartları {}".format(dgt_kartlar), end="")
            print(" (toplam {})".format(dagitici_kart_toplamlari(dgt_kartlar)))
        if dagitici_kart_toplamlari(dgt_kartlar) > 21:
            print("Dağıtıcı battı. Kazandınız!")
        elif dagitici_kart_toplamlari(dgt_kartlar) == 21:
            print("Dağıtıcı blackjack yaptı! Oyun berabere.")
            tekrar = input("Tekrar oynamak istiyor musunuz? (e/h):")
            harfler2 = ["e", "E", "h", "H"]
            while tekrar not in harfler2:
                tekrar = input("Tekrar oynamak istiyor musunuz? (e/h):")
        else:
            print("Kazandınız!")
    else:
        ek_kart = input("Kart ya da Pas (k/p):")
        harfler1 = ["k", "K", "p", "P"]
        while ek_kart not in harfler1:
            ek_kart = input("Kart ya da Pas (k/p):")
        while ek_kart.lower() == "k":
            yeni_oyn_kart = kart_cekme()
            oyn_kartlar.append(yeni_oyn_kart)
            print("Çekilen kart {} {}".format(yeni_oyn_kart[0], yeni_oyn_kart[1]), end="")
            if yeni_oyn_kart[0][1] == "As":
                print(" (toplam {} ya da {}) ".format(oyuncu_kart_toplamlari(oyn_kartlar)[0],
                                                      oyuncu_kart_toplamlari(oyn_kartlar)[1]))
            else:
                print(" (yeni toplam {})".format(oyuncu_kart_toplamlari(oyn_kartlar)[0]))
            if oyuncu_kart_toplamlari(oyn_kartlar)[0] > 21 or oyuncu_kart_toplamlari(oyn_kartlar)[1] > 21:
                # oyuncu_kart_toplamlari fonksiyonu iki toplam döndürdüğü için böyle yapıldı
                print("Battınız. Dağıtıcı kazandı.")
                break
            elif oyuncu_kart_toplamlari(oyn_kartlar)[0] == 21 or oyuncu_kart_toplamlari(oyn_kartlar)[1] == 21:
                print("Blackjack! Sıra dağıtıcıda.")
                print("Dağıtıcının kartları {} {}, {} {}".format(dgt_kartlar[0][0], dgt_kartlar[0][1],
                                                                 dgt_kartlar[1][0], dgt_kartlar[1], [1]), end="")
                print(" (toplam {})".format(dagitici_kart_toplamlari(dgt_kartlar)))
                while dagitici_kart_toplamlari(dgt_kartlar) < 17:
                    yeni_dgt_kart = dagitici_kart_cekme()
                    dgt_kartlar.append(yeni_dgt_kart)
                    print("Dağıtıcının kartları {}".format(dgt_kartlar), end="")
                    print(" (toplam {})".format(dagitici_kart_toplamlari(dgt_kartlar)))
                if dagitici_kart_toplamlari(dgt_kartlar) > 21:
                    print("Dağıtıcı battı. Kazandınız!")
                    break
                elif dagitici_kart_toplamlari(dgt_kartlar) == 21:
                    print("Dağıtıcı blackjack yaptı! Oyun berabere.")
                    break
                else:
                    print("Kazandınız!")
                    break
            else:
                ek_kart = input("Kart ya da Pas (k/p):")
        while ek_kart.lower() == "p":
            print("Sıra dağıtıcıda.")
            print("Dağıtıcının kartları {} {}, {} {}".format(dgt_kartlar[0][0], dgt_kartlar[0][1],
                                                             dgt_kartlar[1][0], dgt_kartlar[1], [1]), end="")
            print(" (toplam {})".format(dagitici_kart_toplamlari(dgt_kartlar)))
            while dagitici_kart_toplamlari(dgt_kartlar) < 17:
                yeni_dgt_kart = dagitici_kart_cekme()
                dgt_kartlar.append(yeni_dgt_kart)
                print("Dağıtıcının kartları {}".format(dgt_kartlar), end="")
                print(" (toplam {})".format(dagitici_kart_toplamlari(dgt_kartlar)))
            if dagitici_kart_toplamlari(dgt_kartlar) > 21:
                print("Dağıtıcı battı. Kazandınız!")
                break
            elif dagitici_kart_toplamlari(dgt_kartlar) == 21:
                if oyuncu_kart_toplamlari(oyn_kartlar)[0] == 21 or oyuncu_kart_toplamlari(oyn_kartlar)[1] == 21:
                    print("Dağıtıcı blackjack yaptı! Oyun berabere.")
                    break
                else:
                    print("Dağıtıcı blackjack yaptı! Kaybettiniz.")
                    break
            elif dagitici_kart_toplamlari(dgt_kartlar) >= 17:
                if oyuncu_kart_toplamlari(oyn_kartlar)[0] > dagitici_kart_toplamlari(dgt_kartlar) or \
                                oyuncu_kart_toplamlari(oyn_kartlar)[1] > dagitici_kart_toplamlari(dgt_kartlar):
                    print("Kazandınız!")
                    break
                elif (oyuncu_kart_toplamlari(oyn_kartlar)[0] or oyuncu_kart_toplamlari(oyn_kartlar)[1]) == \
                        dagitici_kart_toplamlari(dgt_kartlar):
                    print("Oyun berabere.")
                    break
                else:
                    print("Dağıtıcı kazandı.")
                    break


blackjack_21()