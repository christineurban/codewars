# https://www.codewars.com/kata/55befc42bfe4d13ab1000007

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
def get_nth(node, index):          
    curr = node
    if index < 0 or node == None:
        raise Exception('I know Python!')
    for i in range(index):
        curr = curr.next
    if curr == None:
        raise Exception('I know Python!')
    return curr
