import psycopg2

from transaction import Transaction

conn = psycopg2.connect(
    host="test.dsacademy.kz",
    database="fortesting",
    user="testing",
    password="testing123"
)


def create_table():
    query = """
    CREATE TABLE IF NOT EXISTS transactions (
        id SERIAL PRIMARY KEY,
        description VARCHAR(255) NOT NULL,
        price INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        amount INTEGER,
        created DATE DEFAULT NOW(),
        status VARCHAR(255) DEFAULT 'new'
        )
    """

    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()


def insert_transaction(transaction: Transaction):
    query = """
    INSERT INTO transactions (description, price, quantity, amount)
    VALUES (%s, %s, %s, %s)
    """

    cursor = conn.cursor()
    cursor.execute(query, (transaction.description, transaction.price, transaction.quantity, transaction.amount))
    conn.commit()


def update_transactions():
    query = "UPDATE transactions SET amount=price*quantity, status='calculated' WHERE status='new';"
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()


def complete_transactions():
    query = "UPDATE transactions SET status='completed' WHERE status='calculated';"
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()


def get_transactions() -> list[Transaction]:
    query = "SELECT * FROM transactions;"
    cursor = conn.cursor()
    cursor.execute(query)
    return [Transaction(
        id=transaction[0],
        description=transaction[1],
        price=transaction[2],
        quantity=transaction[3],
        amount=transaction[4],
        created=transaction[5],
        status=transaction[6],
    ) for transaction in cursor.fetchall()]
