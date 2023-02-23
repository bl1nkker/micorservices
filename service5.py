import time
from sql_queries import get_transactions
from service6 import send_message
from credentials import conn


cached = []

if __name__ == '__main__':
    while True:
        transactions = get_transactions(conn)
        for transaction in transactions:
            if transaction not in cached:
                cached.append(transaction)
        send_message(f'New transaction!, {transaction}')
        time.sleep(1)
