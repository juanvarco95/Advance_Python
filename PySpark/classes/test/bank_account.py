class BankAccount:
    def __init__(self, account_number: str, balance: int) -> None:
        self._account_number = account_number
        self._balance = balance
    
    def deposit(self, amount: int) -> None:
        self._balance += amount
    
    def withdraw(self, amount: int) -> None:
        if amount <= self._balance:
            self._balance -= amount
        else:
            print('Insufficient Funds')
    
    def get_balance(self) -> int:
        return self._balance
    
    def __str__(self) -> str:
        return f'Account {self._account_number}: Balance $ {self._balance: .2f}'
    
class SavingAccount(BankAccount):
    def __init__(self, account_number: str, balance: int, interest_rate: float) -> None:
        super().__init__(account_number, balance)
        self._interest_rate = interest_rate
    
    def apply_interest(self) -> None:
        self._balance += self._balance * self._interest_rate

