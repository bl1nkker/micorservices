import time
import random
from sql_queries import create_table, insert_transaction
from transaction import Transaction

create_table()

if __name__ == '__main__':
    while True:
        insert_transaction(
            Transaction(
                description=random.choice(["apple", "banana", "orange"]),
                price=random.randint(1, 100),
                quantity=random.randint(1, 10),
                amount=0,
            )
        )
        print("Inserted")
        time.sleep(10)
