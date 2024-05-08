"""
Prosty system ksiegowy/magazyn:

1.  saldo       - Program pobiera kwote do dodania lub odjecia z konta
2.  sprzedaz    - Sprzedaz produktu. Produkt musi znajdowac sie w magazynie
3.  zakup       - Zakupienie znajdujacego sie na magazynie produktu
4.  konto       - Wyswietla stan konta
5.  lista       - Calkowity stan magazynu z cenami i iloscia
6.  magazyn     - Stan magazynu dla konkretnego produktu
7.  przeglad    - Lista uzytych komend
8.  koniec      - Aplikacja konczy dzialanie
"""

stan_konta = 0
caly_stan_konta = 0

slownik_produktow = {
    "Rower": 10,
    "Zestaw srubokretow": 13,
    "Opony": 22,
    "Detki": 6,
    "Hulajnoga": 8,
    "Hulajnoga elektryczna": 20,
}

LISTA_KOMEND = ['saldo', 'sprzedaz', 'zakup', 'konto', 'lista', 'magazyn', 'przeglad', 'koniec',]

while True:
    print(f"Wybierz komende z listy: {LISTA_KOMEND}")
    akcja = input("Podaj komende: ")
    if akcja == 'koniec':
        print('Koncze dzialanie programu...')
        break
    elif akcja == 'saldo':
        stan_konta = int(input("> Podaj kwote do dodania lub odjecia na swoje saldo"))
        if caly_stan_konta < 0:
            print("> Twoj calkowity stan konta nie moze byc na minusie. Podaj kwote ponownie")
            continue
        if stan_konta == 0:
            print("> Podaj kwote wieksza lub mniejsza od 0")
            continue
        if stan_konta > 0:
            caly_stan_konta += stan_konta
        if stan_konta < 0:
            caly_stan_konta -= stan_konta
    elif akcja == 'zakup':
        nazwa = input("> Podaj nazwe produktu: ")
        liczba_sztuk = int(input("> Podaj liczbe produktow: "))
        if liczba_sztuk <= 0:
            print(">> Liczba zakupionych produktow musi byc wieksza od 0.")
            continue
        if nazwa in slownik_produktow and slownik_produktow[nazwa] >= liczba_sztuk:
            print(f">> Zakupuje {liczba_sztuk} sztuk '{nazwa}'.")
            slownik_produktow[nazwa] -= liczba_sztuk
        else:
            print(f">> Niewystarczajaca liczba sztuk produktu.")
    elif akcja == 'sprzedaz':
        nazwa = input("Podaj nazwe produktu: ")
        liczba_sztuk = int(input("Podaj liczbe produktow: "))
        if liczba_sztuk < 1:
            print(">> Liczba sztuk dodawanych produktow musi byc wieksza od 0.")
            continue
        print(f">> Sprzedaje '{nazwa}' w liczbie {liczba_sztuk} sztuk")
        if nazwa not in slownik_produktow:
            print(">> Produkt nie znajduje sie w magazynie. Podaj produkt ktory znajduje sie na stanie.")
            continue

    elif akcja == 'lista':
        print("Lista dostepnych produktow:")
        for nazwa, liczba_sztuk in slownik_produktow.items():
            print(f"{nazwa:<35.35s} | {liczba_sztuk:>3.0f}")
    elif akcja == 'magazyn':
        nazwa_produktu = input('Podaj nazwe produktu do sprawdzenia: ')
        if nazwa_produktu in slownik_produktow and slownik_produktow[nazwa_produktu] > 0:
            print(f"> Produkt '{nazwa_produktu}' jest dostepny.")
        else:
            print(f"> Niestety, produkt '{nazwa_produktu}' jest niedostepny.")