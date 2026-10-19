import sqlite3


def connect(path=":memory:"):
    conn = sqlite3.connect(path)
    conn.execute("CREATE TABLE IF NOT EXISTS customers (id INTEGER PRIMARY KEY, email TEXT, name TEXT)")
    conn.execute("CREATE TABLE IF NOT EXISTS invoices (id INTEGER PRIMARY KEY, customer_id INTEGER, amount_pence INTEGER)")
    return conn
