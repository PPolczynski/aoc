from __future__ import annotations

from typing import Any, Optional


class LinkedListNode:
    def __init__(self, value: Any, nxt: Optional[LinkedListNode] = None, prev: Optional[LinkedListNode] = None):
        self.next = nxt
        self.previous = prev
        self.value = value

    def __str__(self):
        return f"{self.value}, NXT: {self.next.value if self.next else 'NONE'}, PRV: {self.previous.value if self.previous else 'NONE'}"

    def __repr__(self):
        return f"{self.value}, NXT: {self.next.value if self.next else 'NONE'}, PREV: {self.previous.value if self.previous else 'NONE'}"

    def detach(self):
        if self.previous:
            self.previous.next = self.next
        if self.next:
            self.next.previous = self.previous
        self.previous, self.next = None, None

    def insert_before(self, node: LinkedListNode) -> None:
        if self.previous:
            self.previous.next = node
        node.previous = self.previous
        node.next = self
        self.previous = node

    def insert_after(self, node: LinkedListNode) -> None:
        if self.next:
            self.next.previous = node
        node.previous = self
        node.next = self.next
        self.next = node

    def swap(self, node: LinkedListNode) ->None:
        if self.next == node:
            self.next = node.next
            if self.next:
                self.next.previous = self
            if self.previous:
                self.previous.next = node
            tmp = self.previous
            self.previous = node
            node.next = self
            node.previous = tmp
        elif self.previous == node:
            node.swap(self)
        else:
            if self.next:
                self.next.previous = node
            if self.previous:
                self.previous.next = node
            if node.next:
                node.next.previous = self
            if node.previous:
                node.previous.next = self
            self.next, node.next = node.next, self.next
            self.previous, node.previous = node.previous, self.previous

    def get_next_values(self) -> list[Any]:
        curr = self
        out = []
        while curr:
            out.append(curr.value)
            curr = curr.next
        return out

    def get_previous_values(self) -> list[Any]:
        curr = self
        out = []
        while curr:
            out.append(curr.value)
            curr = curr.previous
        return out

    @staticmethod
    def get_from_list(values: list[Any]) -> tuple[Optional[LinkedListNode], Optional[LinkedListNode]]:
        if not values:
            return None, None
        dummy = LinkedListNode(0)
        prev = dummy
        for value in values:
            node = LinkedListNode(value, None, prev)
            prev.next = node
            prev = node
        dummy.next.previous = None
        return dummy.next, prev