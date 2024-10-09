class BankAccount:
    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, deposit):
        if deposit > 0:
            self.balance += deposit
            print(f"{deposit} a été déposé sur le compte de {self.account_holder}.")
        else:
            print("Le montant du dépôt doit être positif.")

    def withdraw(self, withdraw):
        if withdraw > 0:
            if self.balance >= withdraw:
                self.balance -= withdraw
                print(f"{withdraw} a été retiré du compte de {self.account_holder}.")
            else:
                print("Fonds insuffisants pour ce retrait.")
        else:
            print("Le montant du retrait doit être positif.")

    def display_balance(self):
        print(f"Le solde du compte de {self.account_holder} est de {self.balance}.")


if __name__ == '__main__':
    compte = BankAccount("Gunther", 1000.0)
    compte.deposit(500.0)
    compte.withdraw(200.0)
    compte.display_balance()
