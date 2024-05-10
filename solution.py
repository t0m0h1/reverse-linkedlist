class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#  this class represents the linked list, a linked list is a data structure that consists of a sequence of elements where each element points to the next element in the sequence.

def reverseList(head):
    prev = None
    while head:
        temp = head
        head = head.next
        temp.next = prev
        prev = temp
    return prev


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)
    head.next.next.next.next.next.next = ListNode(7)
    head.next.next.next.next.next.next.next = ListNode(8)
    head.next.next.next.next.next.next.next.next = ListNode(9)
    head.next.next.next.next.next.next.next.next.next = ListNode(10)
    reversed_head = reverseList(head)
    print(reversed_head.val)