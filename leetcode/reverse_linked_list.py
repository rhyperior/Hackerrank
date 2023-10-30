from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create the linkedList
        start = None
        current = None
        for node in head:
            if current:
                current.next = ListNode(val=node)
                current = current.next
            else:
                current = ListNode(val=node)
            if start is None:
                start = current

        # Reverse The LinkedList.
        current = start
        prev = None

        swap = None
        while current:
            swap = current
            current = current.next
            swap.next = prev
            prev = swap
        return prev

    def print_nodes(self, start=None):
        current = start
        while current:
            print(current.val)
            current = current.next


if __name__ == "__main__":
    head = [1, 2, 3, 4, 5]
    sol = Solution()
    start = sol.reverseList(head=head)
    sol.print_nodes(start=start)
