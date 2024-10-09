print("Witaj drogi użytkowniku w programie do obsługi ładowarki paczek!")
print(20*"-")
print("Pamiętaj, że limit wagi elementu to 1kg - 10kg ")
print(20*"-")



ilosc_podanych_elementow = int(input("Użytkowniku podaj ilość elementów do przesyłki: "))
print(20*"-")

aktualna_paczka = 0
paczki_wyslane = 0
najlzejsza_paczka = 20
numer_paczki = 0
waga_elementow_wyslanych = 0

for ilosc_paczek in range(ilosc_podanych_elementow):
    waga_podanego_elementu = int(input("Użytkowniku proszę podać wagę elementu: "))
    print(20 * "-")
    if 1 < waga_podanego_elementu > 10:
        print("Podana waga elementu jest niezgodna z ustalonym limitem!")
        print(20 * "-")
        break
    aktualna_paczka += waga_podanego_elementu
    if aktualna_paczka > 20:
        aktualna_paczka -= waga_podanego_elementu
        paczki_wyslane += 1
        print("Maksymalna waga paczki została przekroczona. Pozostałe elementy zostaną dodane do nowej paczki!")
        print(20 * "-")
        print(f"Została wsyłana paczka o wadze {aktualna_paczka}kg!")
        print(20 * "-")
        if aktualna_paczka < najlzejsza_paczka:
            najlzejsza_paczka = aktualna_paczka
            numer_paczki = paczki_wyslane
        waga_elementow_wyslanych += aktualna_paczka
        aktualna_paczka = waga_podanego_elementu
    if aktualna_paczka == 20:
        paczki_wyslane += 1
        print(f"Została wysłana paczka o wadze {aktualna_paczka}kg!")
        print(20 * "-")
        if aktualna_paczka < najlzejsza_paczka:
            najlzejsza_paczka = aktualna_paczka
            numer_paczki = paczki_wyslane
        waga_elementow_wyslanych += aktualna_paczka
        aktualna_paczka = 0
    if aktualna_paczka < 20:
        continue
if aktualna_paczka > 0:
    paczki_wyslane += 1
    print(f"Została wysłana paczka o wadze {aktualna_paczka}kg!")
    print(20 * "-")
    if aktualna_paczka < najlzejsza_paczka:
        najlzejsza_paczka = aktualna_paczka
        numer_paczki = paczki_wyslane
    waga_elementow_wyslanych += aktualna_paczka


suma_pustych_kilogramow = paczki_wyslane * 20 - waga_elementow_wyslanych
suma_pustych_kg_w_naj_paczce = 20 - najlzejsza_paczka

print(f"Zostało wysłanych {paczki_wyslane} paczek!")
print(20*"-")
print(f"Waga paczek wysłanych to {waga_elementow_wyslanych}kg")
print(20*"-")
print(f"Suma pustych kilogramów w paczkach to {suma_pustych_kilogramow}kg")
print(20*"-")
print(f"Najwięcej pustych kilogramów miała paczka {numer_paczki} było to {suma_pustych_kg_w_naj_paczce}kg")
print(20*"-")






