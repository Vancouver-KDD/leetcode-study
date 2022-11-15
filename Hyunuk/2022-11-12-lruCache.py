"""
dll
key, val, prev, next
head, tail
hashmap
"""
class ListNode():
    def __init__(self, key=-1, val=-1, prev=None, next_=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next_


class LRUCache:
    def __init__(self, capacity: int):
        self.size = capacity
        self.hash = dict()
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        if key in self.hash:
            self._move_to_top(self.hash[key])
            return self.hash[key].val
        return -1
    
    def _remove_node(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
        
    def _add_node(self, node):
        node.prev, node.next = self.head, self.head.next
        self.head.next.prev, self.head.next = node, node

    def _move_to_top(self, node):
        self._remove_node(node)
        self._add_node(node)
        
    def _drop_last(self):
        node = self.tail.prev
        self._remove_node(node)

    def put(self, key: int, value: int) -> None:
        node = self.hash.get(key)
        if not node:
            node = ListNode(key, value)
            self.hash[key] = node
            self._add_node(node)
            if len(self.hash) > self.size:
                last = self.tail.prev
                self._drop_last()
                del self.hash[last.key]
        else:
            node.val = value
            self._move_to_top(node)
        return
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
