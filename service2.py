import time
from sql_queries import create_table, update_transactions

create_table()

if __name__ == '__main__':
    while True:
        update_transactions()
        print("updated")
        time.sleep(20)
