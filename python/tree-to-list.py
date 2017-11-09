# http://www.codewars.com/kata/tree-to-list

class Node:
    def __init__(self, data, child_nodes=None):
        self.data = data
        self.child_nodes = child_nodes

def tree_to_list(tree_root):
    lst = []
    hold = [tree_root]
    
    while hold:
        curr = hold[0]
        lst.append(curr.data)
        if curr.child_nodes:
            for child in curr.child_nodes:
                hold.append(child)
        hold.pop(0)
    
    return lst