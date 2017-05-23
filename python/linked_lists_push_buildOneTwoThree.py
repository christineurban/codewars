# https://www.codewars.com/kata/55be95786abade3c71000079

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
def push(head, data):    
    node = Node(data)    
    node.next = head
    return node
    
    
def build_one_two_three():
    one = Node(1)
    two = Node(2)
    three = Node(3)
    
    one.next = two
    two.next = three
    
    return one