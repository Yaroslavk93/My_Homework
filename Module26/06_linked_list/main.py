from typing import Any, Optional


class Node:
    def __init__(self, elem: Optional[Any] = None, next: Optional['Node'] = None) -> None:
        self.elem = elem
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        self.head: Optional['Node'] = None
        self.length = 0

    def __str__(self) -> str:
        if self.head is not None:
            elem_tail = self.head
            elem_list = [elem_tail.elem]
            while elem_tail.next is not None:
                elem_tail = elem_tail.next
                elem_list.append(elem_tail.elem)
            return str(elem_list)

    def append(self, item: Any) -> None:
        first_head = Node(item)
        if self.head is None:
            self.head = first_head
            return

        last_head = self.head
        while last_head.next:
            last_head = last_head.next
        last_head.next = first_head

    def get(self, num: Any) -> None:
        tail = self.head
        while tail.next is not None:
            self.length += 1
            tail = tail.next
            if num == self.length:
                return tail.elem

    def remove(self, item: Any) -> None:
        current = self.head
        index = 0
        last_cur = None
        while current:
            if index == item:
                if last_cur is None:
                    self.head = current.next
                else:
                    last_cur.next = current.next
            index += 1
            last_cur = current
            current = current.next


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)
