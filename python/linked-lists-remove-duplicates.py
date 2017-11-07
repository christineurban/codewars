# http://www.codewars.com/kata/linked-lists-remove-duplicates

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    if not head:
        return
    curr = head
    next = curr.next
    
    while curr.next:
        if curr.data == next.data:
            if next.next:
                next = next.next
                curr.next = next
            else:
                curr.next = None
        else:
            curr = next
            next = curr.next
    return head
                