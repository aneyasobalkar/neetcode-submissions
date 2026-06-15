class MinStack:
    
    def __init__(self):
        self.values = []
        self.stack = LinkedList.empty
    def push(self, val: int) -> None:
        self.values.append(val)
        self.stack = LinkedList(val, self.stack)
    def pop(self) -> None:
        self.values.remove(self.stack.first)
        self.stack = self.stack.rest
    def top(self) -> int:
        return self.stack.first
    def getMin(self) -> int:
        self.values = sorted(self.values)
        return self.values[0]
class LinkedList:
    empty = None
    def __init__(self, first):
        self.first = first
        self.rest = LinkedList.empty
    def __init__(self, first, rest):
        self.first = first
        self.rest = rest
    def first(self):
        return self.first        
