# https://www.codewars.com/kata/55cacc3039607536c6000081

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
def insert_nth(head, index, data):
    node = Node(data)
    curr = head
    prev = None
    if not curr:
        return node
    elif not index:
        node.next = head
        return node
    for i in range(index):
        prev = curr
        curr = curr.next
    node.next = curr
    if prev:
        prev.next = node
    return head
