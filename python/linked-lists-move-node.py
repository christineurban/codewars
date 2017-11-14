# http://www.codewars.com/kata/linked-lists-move-node

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
    
def move_node(source, dest):
    if not source:
        raise Exception('No source')
        
    move = source.data
    source = source.next
    
    if not dest:
        dest = Node(move)
    else:   
        dest = push(dest, move)
    
    return Context(source, dest)