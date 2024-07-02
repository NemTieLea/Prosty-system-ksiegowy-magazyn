from manager import Manager

if __name__ == "__main__":
    manager = Manager()

    while True:
        print("\nSelect one of the options:")
        print("1. saldo")
        print("2. sprzedaz")
        print("3. zakup")
        print("4. konto")
        print("5. lista")
        print("6. magazyn")
        print("7. przeglad")
        print("0. koniec")

        akcja = input("\nAction: ")

        if akcja == '0':
            print('Exiting program...')
            break

        manager.execute(akcja)
