import unittest
from app.db import connect
from app.invoices import list_invoices


class TestInvoices(unittest.TestCase):
    def setUp(self):
        self.conn = connect()
        for i in range(1, 26):
            self.conn.execute("INSERT INTO invoices (id, customer_id, amount_pence) VALUES (?, ?, ?)", (i, 1, i * 100))

    def test_page_sizes(self):
        self.assertEqual(len(list_invoices(self.conn, 3, 10)), 5)
