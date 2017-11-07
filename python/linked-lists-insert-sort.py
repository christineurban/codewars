# http://www.codewars.com/kata/linked-lists-insert-sort

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
def insert_sort(head):
    if not head or not head.next:
        return head
    
    curr = head
    next = curr.next
    
    while next:
        if curr.data > next.data:
            head = sorted_insert(head, next.data)
            curr.next = next.next
            next = curr.next
        else:
            curr = next
            next = next.next
    return head