"""
Prosty system ksiegowy/magazyn:

1.#  saldo       - Program pobiera kwote do dodania lub odjecia z konta
2.#  sprzedaz    - Sprzedaz produktu. Produkt musi znajdowac sie w magazynie
3.#  zakup       - Zakupienie znajdujacego sie na magazynie produktu
4.#  konto       - Wyswietla stan konta
5.#  lista       - Calkowity stan magazynu z cenami i iloscia
6.#  magazyn     - Stan magazynu dla konkretnego produktu
7.  przeglad    - Lista uzytych komend
8.#  koniec      - Aplikacja konczy dzialanie
"""

stan_konta = 0
caly_stan = 0

cena_produktu_Rower = 980
cena_produktu_Srubokret = 30
cena_produktu_Opony = 60
cena_produktu_Detki = 29
cena_produktu_Hulajnoga = 1400
cena_produktu_Pompka = 55

slownik_produktow = {
    "Rower": 10,
    "Srubokret": 13,
    "Opony": 22,
    "Detki": 6,
    "Hulajnoga": 8,
    "Pompka": 20,
}

slownik_produktow_cala_lista = [
     ["Rower", 10, 980],
     ["Srubokret", 13, 30],
     ["Opony", 22, 60],
     ["Detki", 6, 29],
     ["Hulajnoga", 8, 1400],
     ["Pompka", 20, 55],
]

cena_produktow = {
    "Rower": 980,
    "Srubokret": 30,
    "Opony": 60,
    "Detki": 29,
    "Hulajnoga": 1400,
    "Pompka": 55,
}

LISTA_KOMEND = ['saldo', 'sprzedaz', 'zakup', 'konto', 'lista', 'magazyn', 'przeglad', 'koniec',]

while True:
    print(f"Wybierz komende z listy: {LISTA_KOMEND}")
    akcja = input("Podaj komende: ")
    if akcja == 'koniec':
        print('Koncze dzialanie programu...')
        break
    if akcja == 'konto':
        print(f">>Twoj aktualny stan konta to: {caly_stan}")
    elif akcja == 'saldo':
        stan_konta = int(input("> Podaj kwote do dodania lub odjecia na swoje saldo: "))
        if stan_konta == 0:
            print("> Podaj kwote wieksza lub mniejsza od 0")
            continue
        if stan_konta != 0:
            caly_stan += stan_konta
        if caly_stan < 0:
            caly_stan -= stan_konta
            print("> Twoj calkowity stan konta nie moze byc na minusie. Podaj kwote ponownie")
            continue
    elif akcja == 'sprzedaz':
        nazwa = input("> Podaj nazwe produktu: ")
        liczba_sztuk = int(input("> Podaj liczbe produktow: "))
        if liczba_sztuk <= 0:
            print(">> Liczba sprzedanych produktow musi byc wieksza od 0.")
            continue
        if nazwa in slownik_produktow and slownik_produktow[nazwa] >= liczba_sztuk:
            cena = cena_produktow[nazwa] * liczba_sztuk
            print(f">> Sprzedaje {liczba_sztuk} sztuk '{nazwa}' za '{cena} 'pieniedzy.")
            slownik_produktow[nazwa] -= liczba_sztuk
            caly_stan += cena
        else:
            print(f">> Niewystarczajaca liczba sztuk produktu.")
            continue
    elif akcja == 'zakup':
        nazwa = input("Podaj nazwe produktu: ")
        if nazwa in slownik_produktow:
            cena = cena_produktow[nazwa]
        liczba_sztuk = int(input("Podaj liczbe produktow: "))
        if caly_stan == cena_produktow[nazwa] * liczba_sztuk or caly_stan >= cena_produktow[nazwa] * liczba_sztuk:
            cena = cena_produktow[nazwa] * liczba_sztuk
            print(f">> Zakupiono '{nazwa}' w liczbie {liczba_sztuk} sztuk za '{cena}' pieniedzy")
            slownik_produktow[nazwa] += liczba_sztuk
            caly_stan -= cena
            continue
        else:
            liczba_sztuk = int(input("Podaj liczbe produktow: "))
            cena = int(input("Podaj cene jednego produktu"))
        if liczba_sztuk <= 1:
            print(">> Liczba sztuk dodawanych produktow musi byc wieksza lub rowna 0.")
            continue
        if caly_stan < cena_produktow[nazwa] * liczba_sztuk:
            print("Niewystarczajaca ilosc pieniedzy")
            continue
        if caly_stan == cena_produktow[nazwa] * liczba_sztuk or caly_stan >= cena_produktow[nazwa] * liczba_sztuk:
            print(f">> Zakupiono '{nazwa}' w liczbie {liczba_sztuk} sztuk za '{cena}' pieniedzy")
            slownik_produktow[nazwa] += liczba_sztuk
            caly_stan -= cena
        if nazwa not in slownik_produktow:
            slownik_produktow[nazwa] = 0
        slownik_produktow[nazwa] += liczba_sztuk
        print(">> Produkt zostaje dodany do magazynu.")
    elif akcja == 'lista':
        print("Lista dostepnych produktow:")
        for nazwa, liczba_sztuk in slownik_produktow.items():
            print(f"Produkty oraz ilosc {nazwa:<35.35s} | {liczba_sztuk:>3.0f}")
        for nazwa, liczba_sztuk in cena_produktow.items():
            print(f"Produkty oraz ceny: {nazwa:<35.35s} | {liczba_sztuk:>3.0f}")
    elif akcja == 'magazyn':
        nazwa_produktu = input('Podaj nazwe produktu do sprawdzenia: ')
        if nazwa_produktu in slownik_produktow and slownik_produktow[nazwa_produktu] > 0:
            print(f"> Produkt '{nazwa_produktu}' jest dostepny.")
        else:
            print(f"> Niestety, produkt '{nazwa_produktu}' jest niedostepny.")
