# https://www.codewars.com/kata/linked-lists-length-and-count

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
def length(node):
    if node == None:
        return 0
        
    counter = 1
    curr = node
    
    while curr.next != None:
        counter += 1
        curr = curr.next
    return counter
  
def count(node, data):
    if node == None:
        return 0

    counter = 0
    curr = node
    
    while curr:
        if curr.data == data:
            counter += 1
        curr = curr.next

    return counter