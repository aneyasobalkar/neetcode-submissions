class ListNode:
    def __init__(self, key, val, prev, nxt):
        self.key = key
        self.val = val
        self.prev = prev
        self.nxt = nxt

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = ListNode(None, None, None, None)
        self.tail = ListNode(None,None, None, None)
        self.head.nxt = self.tail
        self.tail.prev = self.head
        self.key_val_map = {} #map key to Node
    def remove(self, node):
        prev, nxt = node.prev, node.nxt
        prev.nxt = nxt
        nxt.prev = prev
    def insert(self, node):
        prev, nxt = self.tail.prev, self.tail
        prev.nxt = node
        nxt.prev = node
        node.prev = prev
        node.nxt = nxt
    def get(self, key: int) -> int:
        if key in self.key_val_map:
            get_node = self.key_val_map[key]
            self.remove(get_node)
            self.insert(get_node)
            return get_node.val
        else:
            return -1
    def put(self, key: int, value: int) -> None:
        if key in self.key_val_map:
            node = self.key_val_map[key]
            node.val = value
            self.remove(node)
            self.insert(node)
        else:
            new_node = ListNode(key, value, self.tail.prev, self.tail)
            self.key_val_map[key] = new_node
            self.insert(new_node)
        if len(self.key_val_map) > self.capacity:
            k = self.head.nxt.key
            self.remove(self.head.nxt)
            self.key_val_map.pop(k)


