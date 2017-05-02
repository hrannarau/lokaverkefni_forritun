#Lokaverkefni
#Hrannar og Magnús
#Hér importum við random
import random
#Hér opnum við skránna og splittum henni
with open("spillaufhjarta","r",encoding="utf-8") as skra:
    faersla = skra.read().split("\n")
#Hér byrjum við að stokka
stokka = random.sample(range(52),52)
#Hér gerum við listatölurnar
leikmadurtolur = []
talvatolur = []
#Hér klárum við að stokka
for i in stokka:
    if i%2==0:
        talvatolur.append(i)
    else:
        leikmadurtolur.append(i)
#Hér búum við tila spilalistana
leikmadur = []
talva = []
jafntefli = []
#Hér fara tölurnar í færsluna hjá Leikmann og Tölvu
for i in leikmadurtolur:
    leikmadur.append(faersla[i])
for i in talvatolur:
    talva.append(faersla[i])
#Hér er While lykkjan sem heldur leiknum
while len(leikmadur)>0 and len(talva)>0:
#Hér er prentað að Leikmaður á leik og prentað út spilin hans

    print("Leikmaður á leik")
    print(leikmadur)
#Hér er að splitta spilinu í nafn og flokka
    spil1 = leikmadur[0].split(":")
    spil2 = talva[0].split(":")
#Hér er prent út flokkana
    print("Flokkarnir")
    print("1. Þyngd (kg)")
    print("2. Mjólkurlagni (dætra)")
    print("3. Einkunn ullar")
    print("4. Fjöldi afkvæma")
    print("5. Einkunn læris")
    print("6. Frjósemi")
    print("7. Gerð/þykkt bakvöðva")
    print("8. Einkun fyrir malir")
    print("Þetta er spilið þitt")
#Hér er prentað út efsta spilið
    print(spil1)
#Hér fær notandinn að velja hvaða flokk hann vill nota
    val = int(input("Hvaða flokk viltu nota? "))

    flokkarspil1 = spil1[1].split(",")
    print(flokkarspil1[val-1])
    flokkarspil2 = spil2[1].split(",")
#Ef notandi vinnur
    if float(flokkarspil1[val-1]) > float(flokkarspil2[val-1]):
        print("Þú vannst")
        if len(jafntefli)>0:
            for spil in jafntefli:
                leikmadur.append(spil)
            jafntefli.clear()
        leikmadur.append(leikmadur[0])
        leikmadur.remove(leikmadur[0])
        leikmadur.append(talva[0])
        talva.remove(talva[0])
        print(leikmadur)
#Ef talvan vinnur
    elif float(flokkarspil2[val-1]) > float(flokkarspil1[val-1]):
        print("Talvan vann")
        if len(jafntefli)>0:
            for spil in jafntefli:
                talva.append(spil)
            jafntefli.clear()
        talva.append(talva[0])
        talva.remove(talva[0])
        talva.append(leikmadur[0])
        leikmadur.remove(leikmadur[0])
        print(leikmadur)
#Ef það verður jafntefli
    else:
        print("Jafntefli")
        jafntefli.append(leikmadur[0])
        jafntefli.append(talva[0])
        leikmadur.remove(leikmadur[0])
        talva.remove(talva[0])
        print(jafntefli)

#Nú á talvan leik
    print("Talvan á leik")
    val = random.randint(0,7)
    flokkarspil1 = spil1[1].split(",")
    flokkarspil2 = spil2[1].split(",")
    jafntefli = []
#Ef notandi vinnur
    if float(flokkarspil1[val]) > float(flokkarspil2[val]):
        print("Þú vannst")
        if len(jafntefli)>0:
            for spil in jafntefli:
                leikmadur.append(spil)
            jafntefli.clear()
        leikmadur.append(leikmadur[0])
        leikmadur.remove(leikmadur[0])
        leikmadur.append(talva[0])
        talva.remove(talva[0])
        print(leikmadur)
#Ef talvan vinnur
    elif float(flokkarspil2[val]) > float(flokkarspil1[val]):
        print("Talvan vann")
        if len(jafntefli)>0:
            for spil in jafntefli:
                talva.append(spil)
            jafntefli.clear()
        talva.append(jafntefli)
        talva.append(talva[0])
        talva.remove(talva[0])
        talva.append(leikmadur[0])
        leikmadur.remove(leikmadur[0])
        print(leikmadur)
#Ef það verður jafntefli
    else:
        print("Jafntefli")
        jafntefli.append(leikmadur[0])
        jafntefli.append(talva[0])
        print(jafntefli)

#Nú er einhver sigurvegari og skrifað er út hver vann
if len(leikmadur) == 0:
    print("Talvan vann leikinn!")
    print("Takk fyrir leikinn :)")
elif len(talva) == 0:
    print("Þú vannst leikinn!")
    print("Takk fyrir leikinn :)")