import time
from sql_queries import create_table, complete_transactions

create_table()

if __name__ == '__main__':
    while True:
        complete_transactions()
        print("completed")
        time.sleep(20)
