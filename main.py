import json
import os

FILE_NAME = "shop_warehouse_data.txt"


def load_state():
    if not os.path.isfile(FILE_NAME):
        return {
            "caly_stan": 0,
            "historia": [],
            "slownik_produktow": {
                "Rower": 10,
                "Srubokret": 13,
                "Opony": 22,
                "Detki": 6,
                "Hulajnoga": 8,
                "Pompka": 20,
            },
            "cena_produktow": {
                "Rower": 980,
                "Srubokret": 30,
                "Opony": 60,
                "Detki": 29,
                "Hulajnoga": 1400,
                "Pompka": 55,
            }
        }

    with open(FILE_NAME, 'r') as file:
        data = json.load(file)
        return data


def save_state(state):
    with open(FILE_NAME, 'w') as file:
        json.dump(state, file)


state = load_state()

LISTA_KOMEND = ['saldo', 'sprzedaz', 'zakup', 'konto', 'lista', 'magazyn', 'przeglad', 'koniec']

while True:
    print(f"Wybierz komende z listy: {LISTA_KOMEND}")
    akcja = input("Podaj komende: ")
    if akcja == 'koniec':
        print('Koncze dzialanie programu...')
        save_state(state)
        break
    elif akcja == 'konto':
        print(f">>Twoj aktualny stan konta to: {state['caly_stan']}")
    elif akcja == 'saldo':
        stan_konta = int(input("> Podaj kwote do dodania lub odjecia na swoje saldo: "))
        if stan_konta == 0:
            print("> Podaj kwote wieksza lub mniejsza od 0")
            continue
        state['caly_stan'] += stan_konta
        state['historia'].append([akcja, stan_konta, state['caly_stan']])
        if state['caly_stan'] < 0:
            state['caly_stan'] -= stan_konta
            print("> Twoj calkowity stan konta nie moze byc na minusie. Podaj kwote ponownie")
            continue
    elif akcja == 'sprzedaz':
        nazwa = input("> Podaj nazwe produktu: ")
        liczba_sztuk = int(input("> Podaj liczbe produktow: "))
        if liczba_sztuk <= 0:
            print(">> Liczba sprzedanych produktow musi byc wieksza od 0.")
            continue
        if nazwa in state['slownik_produktow'] and state['slownik_produktow'][nazwa] >= liczba_sztuk:
            cena = state['cena_produktow'][nazwa] * liczba_sztuk
            print(f">> Sprzedaje {liczba_sztuk} sztuk '{nazwa}' za '{cena} 'pieniedzy.")
            state['slownik_produktow'][nazwa] -= liczba_sztuk
            state['caly_stan'] += cena
        else:
            print(f">> Niewystarczajaca liczba sztuk produktu.")
            continue
        state['historia'].append([akcja, nazwa, liczba_sztuk])
    elif akcja == 'zakup':
        nazwa = input("Podaj nazwe produktu: ")
        if nazwa in state['slownik_produktow']:
            cena = state['cena_produktow'][nazwa]
            liczba_sztuk = int(input("Podaj liczbe produktow: "))
            if liczba_sztuk <= 0:
                print(">> Liczba zakupionych produktow musi byc wieksza od 0.")
                continue
            if state['caly_stan'] >= cena * liczba_sztuk:
                koszt = cena * liczba_sztuk
                print(f">> Zakupiono '{nazwa}' w liczbie {liczba_sztuk} sztuk za '{koszt}' pieniedzy")
                state['slownik_produktow'][nazwa] += liczba_sztuk
                state['caly_stan'] -= koszt
                state['historia'].append([akcja, nazwa, liczba_sztuk])
            else:
                print("Niewystarczajaca ilosc pieniedzy")
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
            koszt = cena * liczba_sztuk
            if state['caly_stan'] < koszt:
                print("Niewystarczajaca ilosc pieniedzy")
                continue
            if nazwa not in state['slownik_produktow']:
                state['slownik_produktow'][nazwa] = 0
                state['cena_produktow'][nazwa] = cena
            state['slownik_produktow'][nazwa] += liczba_sztuk
            state['caly_stan'] -= koszt
            print(f">> Zakupiono '{nazwa}' w liczbie {liczba_sztuk} sztuk za '{koszt}' pieniedzy")
            state['historia'].append([akcja, nazwa, liczba_sztuk])
    elif akcja == 'lista':
        print("Lista dostepnych produktow:")
        for nazwa, liczba_sztuk in state['slownik_produktow'].items():
            print(f"Produkty oraz ilosc {nazwa:<35.35s} | {liczba_sztuk:>3.0f}")
        for nazwa, cena in state['cena_produktow'].items():
            print(f"Produkty oraz ceny: {nazwa:<35.35s} | {cena:>3.0f}")
    elif akcja == 'magazyn':
        nazwa_produktu = input('Podaj nazwe produktu do sprawdzenia: ')
        if nazwa_produktu in state['slownik_produktow'] and state['slownik_produktow'][nazwa_produktu] > 0:
            print(f"""> Produkt '{nazwa_produktu}' jest dostepny. 
            ilosc: {state['slownik_produktow'][nazwa_produktu]}
            Cena za sztuke: {state['cena_produktow'][nazwa_produktu]}""")
        else:
            print(f"> Niestety, produkt '{nazwa_produktu}' jest niedostepny.")
    elif akcja == 'przeglad':
        print(f"> Calkowita ilosc wprowadzonych komend: {len(state['historia'])}")
        try:
            wartosc_od = input("Wprowadz wartosc od (wcisnij enter dla calej listy): ")
            wartosc_do = input("Wprowadz wartosc do (wcisnij enter dla calej listy): ")
            if not wartosc_od.strip():
                wartosc_od = 0
            else:
                wartosc_od = int(wartosc_od)
            if not wartosc_do.strip():
                wartosc_do = len(state['historia'])
            else:
                wartosc_do = int(wartosc_do)
            if wartosc_od < 0 or wartosc_od > len(state['historia']):
                print(f"Nieprawidlowa wartosc. Musi byc pomiedzy 0 a {len(state['historia'])}")
                wartosc_od = 0
            if wartosc_do > len(state['historia']) or wartosc_od > wartosc_do:
                print(f"Nieprawidlowa wartosc. Musi byc pomiedzy {wartosc_od} a {len(state['historia'])}")
                wartosc_do = len(state['historia'])
            for entry in state['historia'][wartosc_od:wartosc_do]:
                print(entry)
        except ValueError:
            print("Nieprawidlowa wartosc. Prosze wpisac prawidlowa wartosc.")
        except Exception as e:
            print(f"Blad: {str(e)}")
