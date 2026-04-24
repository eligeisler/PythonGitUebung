import unittest
from bank_account import BankAccount

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        # Vorbereitung: Ein Konto mit 100 Euro Startguthaben [cite: 29]
        self.account = BankAccount("Max Mustermann", 100.0)

    def test_initial_balance(self):
        self.assertEqual(self.account.get_balance(), 100.0)

    def test_deposit(self):
        self.account.deposit(50.0)
        self.assertEqual(self.account.get_balance(), 150.0)

    def test_withdraw(self):
        self.account.withdraw(40.0)
        self.assertEqual(self.account.get_balance(), 60.0)

    def test_insufficient_funds(self):
        # Prüft, ob eine Exception bei zu wenig Guthaben ausgelöst wird
        with self.assertRaises(ValueError):
            self.account.withdraw(200.0)

    def test_negative_deposit(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-10.0)

if __name__ == '__main__':
    unittest.main()