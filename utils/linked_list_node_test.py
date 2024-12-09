import unittest

from utils.linked_list_node import LinkedListNode


class LinkedListNodeTestCase(unittest.TestCase):
    def test_linked_list_creation(self):
        values = [1,2,3,4,5]
        head, tail = LinkedListNode.get_from_list(values)
        self.assertListEqual(values, head.get_next_values())
        self.assertListEqual(list(reversed(values)), tail.get_previous_values())
        values = [1]
        head, tail = LinkedListNode.get_from_list(values)
        self.assertListEqual(values, head.get_next_values())
        self.assertListEqual(list(reversed(values)), tail.get_previous_values())
        self.assertEqual(head, tail)
        values = []
        head, _ = LinkedListNode.get_from_list(values)
        self.assertEqual(None, head)

    def test_insert_after(self):
        values = [1, 2, 3, 4, 5]
        head, tail = LinkedListNode.get_from_list(values)
        n15 = LinkedListNode(1.5)
        head_nxt = head.next
        head.insert_after(n15)
        self.assertListEqual([1, 1.5, 2, 3, 4, 5], head.get_next_values())
        self.assertEqual(head, n15.previous)
        self.assertEqual(n15, head.next)
        self.assertEqual(head_nxt, n15.next)
        self.assertEqual(n15, head_nxt.previous)
        tail.insert_after(LinkedListNode(6))
        self.assertListEqual([1, 1.5, 2, 3, 4, 5, 6], head.get_next_values())
        values = [1]
        head, tail = LinkedListNode.get_from_list(values)
        n2 = LinkedListNode(2)
        head.insert_after(n2)
        self.assertEqual(head, n2.previous)
        self.assertEqual(None, head.previous)
        self.assertEqual(n2, head.next)
        self.assertEqual(None, n2.next)
        self.assertListEqual([1, 2], head.get_next_values())

    def test_insert_before(self):
        mem = dict()
        values = [1, 2, 3, 4, 5]
        dummy = LinkedListNode(0)
        prev = dummy
        for value in values:
            node = LinkedListNode(value, None, prev)
            mem[value] = node
            prev.next = node
            prev = node
        dummy.next.previous = None
        head = dummy.next
        n15 = LinkedListNode(1.5)
        head_nxt = head.next
        mem[2].insert_before(n15)
        self.assertListEqual([1, 1.5, 2, 3, 4, 5], head.get_next_values())
        self.assertEqual(head, n15.previous)
        self.assertEqual(n15, head.next)
        self.assertEqual(head_nxt, n15.next)
        self.assertEqual(n15, head_nxt.previous)
        node0 = LinkedListNode(0)
        head.insert_before(node0)
        self.assertListEqual([0, 1, 1.5, 2, 3, 4, 5], node0.get_next_values())
        self.assertEqual(node0, head.previous)
        self.assertEqual(head, node0.next)
        values = [1]
        head, tail = LinkedListNode.get_from_list(values)
        n0 = LinkedListNode(0)
        head.insert_before(n0)
        self.assertEqual(n0, head.previous)
        self.assertEqual(None, head.next)
        self.assertEqual(n0, head.previous)
        self.assertEqual(None, n0.previous)
        self.assertListEqual([0,1], n0.get_next_values())

    def test_swap_middle(self):
        mem = dict()
        values = [1, 2, 3, 4, 5]
        dummy = LinkedListNode(0)
        prev = dummy
        for value in values:
            node = LinkedListNode(value, None, prev)
            mem[value] = node
            prev.next = node
            prev = node
        dummy.next.previous = None
        head = dummy.next
        self.assertListEqual(values, head.get_next_values())
        mem[2].swap(mem[4])
        self.assertListEqual([1, 4, 3, 2, 5], head.get_next_values())
        self.assertEqual(mem[1], mem[4].previous)
        self.assertEqual(mem[3], mem[4].next)
        self.assertEqual(mem[4], mem[3].previous)
        self.assertEqual(mem[4], mem[1].next)

        self.assertEqual(mem[3], mem[2].previous)
        self.assertEqual(mem[5], mem[2].next)
        self.assertEqual(mem[2], mem[5].previous)
        self.assertEqual(mem[2], mem[3].next)

    def test_swap_edge(self):
        mem = dict()
        values = [1, 2, 3, 4, 5]
        dummy = LinkedListNode(0)
        prev = dummy
        for value in values:
            node = LinkedListNode(value, None, prev)
            mem[value] = node
            prev.next = node
            prev = node
        dummy.next.previous = None
        head = dummy.next
        self.assertListEqual(values, head.get_next_values())
        mem[1].swap(mem[5])
        self.assertListEqual([5, 2, 3, 4, 1], prev.get_next_values())
        self.assertEqual(None, mem[5].previous)
        self.assertEqual(mem[2], mem[5].next)
        self.assertEqual(mem[5], mem[2].previous)

        self.assertEqual(mem[4], mem[1].previous)
        self.assertEqual(None, mem[1].next)
        self.assertEqual(mem[1], mem[4].next)

    def test_swap_neighbours(self):
        mem = dict()
        values = [1, 2, 3, 4, 5]
        dummy = LinkedListNode(0)
        prev = dummy
        for value in values:
            node = LinkedListNode(value, None, prev)
            mem[value] = node
            prev.next = node
            prev = node
        dummy.next.previous = None
        head = dummy.next
        self.assertListEqual(values, head.get_next_values())
        mem[2].swap(mem[3])
        self.assertListEqual([1, 3, 2, 4, 5], head.get_next_values())
        self.assertEqual(mem[1], mem[3].previous)
        self.assertEqual(mem[2], mem[3].next)
        self.assertEqual(mem[3], mem[2].previous)
        self.assertEqual(mem[3], mem[1].next)

        self.assertEqual(mem[3], mem[2].previous)
        self.assertEqual(mem[4], mem[2].next)
        self.assertEqual(mem[2], mem[4].previous)
        self.assertEqual(mem[2], mem[3].next)

    def test_swap_neighbours_edge(self):
        mem = dict()
        values = [1, 2]
        dummy = LinkedListNode(0)
        prev = dummy
        for value in values:
            node = LinkedListNode(value, None, prev)
            mem[value] = node
            prev.next = node
            prev = node
        dummy.next.previous = None
        head = dummy.next
        self.assertListEqual(values, head.get_next_values())
        mem[2].swap(mem[1])
        self.assertListEqual([2, 1], prev.get_next_values())
        self.assertEqual(mem[2], mem[1].previous)
        self.assertEqual(None, mem[1].next)
        self.assertEqual(None, mem[2].previous)
        self.assertEqual(mem[1], mem[2].next)

    def test_swap_neighbours_self(self):
        mem = dict()
        values = [1]
        dummy = LinkedListNode(0)
        prev = dummy
        for value in values:
            node = LinkedListNode(value, None, prev)
            mem[value] = node
            prev.next = node
            prev = node
        dummy.next.previous = None
        head = dummy.next
        self.assertListEqual(values, head.get_next_values())
        mem[1].swap(mem[1])
        self.assertListEqual([1], prev.get_next_values())
        self.assertEqual(None, mem[1].previous)
        self.assertEqual(None, mem[1].next)

    def test_detach(self):
        mem = dict()
        values = [1, 2, 3, 4, 5]
        dummy = LinkedListNode(0)
        prev = dummy
        for value in values:
            node = LinkedListNode(value, None, prev)
            mem[value] = node
            prev.next = node
            prev = node
        dummy.next.previous = None
        head = dummy.next
        self.assertListEqual(values, head.get_next_values())
        mem[2].detach()
        self.assertListEqual([1, 3, 4, 5], head.get_next_values())
        self.assertListEqual([2], mem[2].get_next_values())
        self.assertEqual(None, mem[2].previous)
        self.assertEqual(None, mem[2].next)
        self.assertEqual(mem[3], mem[1].next)
        self.assertEqual(mem[1], mem[3].previous)

        mem[1].detach()
        self.assertListEqual([3, 4, 5], mem[3].get_next_values())
        self.assertListEqual([5, 4, 3], mem[5].get_previous_values())
        self.assertListEqual([1], mem[1].get_next_values())
        self.assertListEqual([1], mem[1].get_previous_values())
        self.assertEqual(None, mem[3].previous)
        self.assertEqual(mem[3], mem[4].previous)

        mem[5].detach()
        self.assertListEqual([3, 4], mem[3].get_next_values())
        self.assertEqual(None, mem[4].next)

        mem[3].detach()
        self.assertListEqual([3], mem[3].get_next_values())
        self.assertListEqual([3], mem[3].get_previous_values())
        self.assertListEqual([4], mem[4].get_next_values())
        self.assertListEqual([4], mem[4].get_previous_values())

if __name__ == '__main__':
    unittest.main()
