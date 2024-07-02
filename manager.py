from library_storage import load_state, save_state
from actions import Actions

class Manager:
    def __init__(self):
        self.state = load_state()
        self.actions = Actions(self)

    def execute(self, action):
        if action == '1' or action.lower() == 'saldo':
            self.actions.saldo()
            self.save_state()  # Save state after modifying
        elif action == '2' or action.lower() == 'sprzedaz':
            self.actions.sprzedaz()
            self.save_state()  # Save state after modifying
        elif action == '3' or action.lower() == 'zakup':
            self.actions.zakup()
            self.save_state()  # Save state after modifying
        elif action == '4' or action.lower() == 'konto':
            self.actions.konto()
        elif action == '5' or action.lower() == 'lista':
            self.actions.lista()
        elif action == '6' or action.lower() == 'magazyn':
            self.actions.magazyn()
        elif action == '7' or action.lower() == 'przeglad':
            self.actions.przeglad()
        elif action == '0' or action.lower() == 'koniec':
            self.save_state()  # Save state before exiting
        else:
            print(f"Nieznana komenda: {action}")

    def save_state(self):
        save_state(self.state)


if __name__ == "__main__":
    manager = Manager()

    options = [
        'koniec',
        'saldo',
        'sprzedaz',
        'zakup',
        'konto',
        'lista',
        'magazyn',
        'przeglad'
    ]

    while True:
        print("\nSelect one of the options:")
        for i, option in enumerate(options):
            print(f"{i}. {option}")
        akcja = input("\nAction: ")
        manager.execute(akcja)
