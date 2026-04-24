import unittest
from unittest.mock import MagicMock
from flight import Flight, BookingSystem


class TestFlightSystem(unittest.TestCase):
    def setUp(self):
        self.flight = Flight("LH123", 2)
        # Mocking der externen Datenquelle [cite: 38]
        self.mock_payment = MagicMock()
        self.booking_system = BookingSystem(self.mock_payment)
        self.booking_system.add_flight(self.flight)

    def test_successful_booking(self):
        # Wir simulieren: Zahlung ist immer erfolgreich (True)
        self.mock_payment.process_payment.return_value = True

        seat = self.booking_system.book_ticket("LH123", "Alice", "4111", 500)
        self.assertEqual(seat, 1)
        self.assertEqual(self.flight.get_available_seats(), 1)

    def test_failed_payment(self):
        # Wir simulieren: Zahlung schlägt fehl (False)
        self.mock_payment.process_payment.return_value = False

        with self.assertRaises(ValueError):
            self.booking_system.book_ticket("LH123", "Bob", "4111", 500)


if __name__ == '__main__':
    unittest.main()