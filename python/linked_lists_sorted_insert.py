# https://www.codewars.com/kata/linked-lists-sorted-insert

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
def sorted_insert(head, data):
    node = Node(data)
    if not head:
        return node
    prev = None
    curr = head
    try:
        while data > curr.data and curr is not None:
            prev = curr
            curr = curr.next
    except:
        pass
    if prev:
        prev.next = node
    else:
        head = node
    node.next = curr
    return head