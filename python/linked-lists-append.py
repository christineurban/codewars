# http://www.codewars.com/kata/linked-lists-append

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def append(listA, listB):
    print listA
    print listB
    if not listA and not listB:
        return
    if not listA and listB:
        return listB
    if not listB and listA:
        return listA
    if listA and listB:
        curr = listA
        while curr.next:
            curr = curr.next
        curr.next = listB
        return listA