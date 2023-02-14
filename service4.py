import time
from sql_queries import create_table, get_transactions

create_table()

if __name__ == '__main__':
    while True:
        transactions = get_transactions()
        print("-------------------- >>")
        for transaction in transactions:
            print(transaction)
        print("-------------------- <<")
        time.sleep(5)
