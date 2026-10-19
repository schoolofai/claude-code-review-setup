import unittest
from app.db import connect
from app.invoices import search_customers


class TestSearch(unittest.TestCase):
    def test_finds_customer(self):
        conn = connect()
        conn.execute("INSERT INTO customers (id, email, name) VALUES (1, 'ada@example.com', 'Ada')")
        self.assertEqual(len(search_customers(conn, "ada")), 1)
