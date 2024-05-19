"""
Prosty system ksiegowy/magazyn:

1.#  saldo       - Program pobiera kwote do dodania lub odjecia z konta
2.#  sprzedaz    - Sprzedaz produktu. Produkt musi znajdowac sie w magazynie
3.#  zakup       - Zakupienie znajdujacego sie na magazynie produktu
4.#  konto       - Wyswietla stan konta
5.#  lista       - Calkowity stan magazynu z cenami i iloscia
6.#  magazyn     - Stan magazynu dla konkretnego produktu
7.#  przeglad    - Lista uzytych komend
8.#  koniec      - Aplikacja konczy dzialanie
"""

stan_konta = 0
caly_stan = 0

historia = []

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
            historia.append([akcja, stan_konta, caly_stan])
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
        historia.append([akcja, nazwa, liczba_sztuk])
    elif akcja == 'zakup':
        nazwa = input("Podaj nazwe produktu: ")
        if nazwa in slownik_produktow:
            cena = cena_produktow[nazwa]
            liczba_sztuk = int(input("Podaj liczbe produktow: "))
            if liczba_sztuk <= 0:
                print(">> Liczba zakupionych produktow musi byc wieksza od 0.")
                continue
            if caly_stan == cena_produktow[nazwa] * liczba_sztuk or caly_stan >= cena_produktow[nazwa] * liczba_sztuk:
                cena = cena_produktow[nazwa] * liczba_sztuk
                print(f">> Zakupiono '{nazwa}' w liczbie {liczba_sztuk} sztuk za '{cena}' pieniedzy")
                slownik_produktow[nazwa] += liczba_sztuk
                caly_stan -= cena
                historia.append([akcja, nazwa, liczba_sztuk])
                continue
        else:
            liczba_sztuk = int(input("Podaj liczbe produktow: "))
            if liczba_sztuk <= 0:
                print(">> Liczba zakupionych produktow musi byc wieksza od 0.")
                continue
            cena = int(input("Podaj cene jednego produktu: "))
            if cena <= 0:
                print(">> Cena musi byc wyzsza od 0")
                continue
        if liczba_sztuk <= 0:
            print(">> Liczba sztuk dodawanych produktow musi byc wieksza lub rowna 0.")
            continue
        if caly_stan < cena * liczba_sztuk:
            print("Niewystarczajaca ilosc pieniedzy")
            continue
        if nazwa not in slownik_produktow:
            slownik_produktow[nazwa] = 0
            cena_produktow[nazwa] = 0
        cena = cena * liczba_sztuk
        slownik_produktow[nazwa] += liczba_sztuk
        cena_produktow[nazwa] += cena
        print(">> Produkt zostaje dodany do magazynu.")
        if caly_stan == cena_produktow[nazwa] * liczba_sztuk or caly_stan >= cena_produktow[nazwa] * liczba_sztuk:
            print(f">> Zakupiono '{nazwa}' w liczbie {liczba_sztuk} sztuk za '{cena}' pieniedzy")
            caly_stan -= cena
        historia.append([akcja, nazwa, liczba_sztuk])
    elif akcja == 'lista':
        print("Lista dostepnych produktow:")
        for nazwa, liczba_sztuk in slownik_produktow.items():
            print(f"Produkty oraz ilosc {nazwa:<35.35s} | {liczba_sztuk:>3.0f}")
        for nazwa, liczba_sztuk in cena_produktow.items():
            print(f"Produkty oraz ceny: {nazwa:<35.35s} | {liczba_sztuk:>3.0f}")
    elif akcja == 'magazyn':
        nazwa_produktu = input('Podaj nazwe produktu do sprawdzenia: ')
        if nazwa_produktu in slownik_produktow and slownik_produktow[nazwa_produktu] > 0:
            print(f"""> Produkt '{nazwa_produktu}' jest dostepny. 
            ilosc: {slownik_produktow[nazwa_produktu]}
            Cena za sztuke: {cena_produktow[nazwa_produktu]}""")
        else:
            print(f"> Niestety, produkt '{nazwa_produktu}' jest niedostepny.")
    elif akcja == 'przeglad':
        print(f"> Calkowita ilosc wprowadzonych komend: {len(historia)}")
        try:
            wartosc_od = input("Wprowadz wartosc od (wcisnij enter dla calej listy): ")
            wartosc_do = input("Wprowadz wartosc do (wcisnij enter dla calej listy): ")
            if not wartosc_od.strip():
                wartosc_od = 0
            else:
                wartosc_od = int(wartosc_od)
            if not wartosc_do.strip():
                wartosc_do = len(historia)
            else:
                wartosc_do = int(wartosc_do)
            if wartosc_od < 0 or wartosc_od > len(historia):
                print(f"Nieprawidlowa wartosc. Musi byc pomiedzy 0 a {len(historia)}")
                wartosc_od = 0
            if wartosc_do > len(historia) or wartosc_od > wartosc_do:
                print(f"Nieprawidlowa wartosc. Musi byc pomiedzy {wartosc_od} a {len(historia)}")
                wartosc_do = len(historia)
            for entry in historia[wartosc_od:wartosc_do]:
                print(entry)
        except ValueError:
            print("Nieprawidlowa wartosc. Prosze wpisac prawidlowa wartosc.")
        except Exception as e:
            print(f"Blad: {str(e)}")
