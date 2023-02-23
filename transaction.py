from dataclasses import dataclass
from typing import Optional


@dataclass
class Transaction:
    description: str
    price: int
    quantity: int
    amount: int
    created: str = ""
    status: str = "new"
    id: Optional[int] = None

    def __str__(self) -> str:
        return f"Transaction: {self.description}, {self.price}, {self.quantity}, {self.amount}, {self.created}, {self.status}, {self.id}"
