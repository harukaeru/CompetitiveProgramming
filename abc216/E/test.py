from typing import Any
from dataclasses import dataclass, field

@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any = field(compare=True)

from queue import PriorityQueue

q = PriorityQueue()
q.put((1, 3))
q.put((2, 2))
q.put((3, 1))
q.put((1, 4))
print(q.get())
