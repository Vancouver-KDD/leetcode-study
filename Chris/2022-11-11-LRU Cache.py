class NodeList:
    def __init__(self, key=0, val=0):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None
    
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = NodeList()
        self.tail = NodeList()
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        # Get node from hash
        nodeToGet = self.cache[key]
        
        # move node to top
        self._moveToTop(nodeToGet)
        
        # return value
        return nodeToGet.val
        
    def _moveToTop(self, node):
        self._remove_node(node)
        self._add_node(node, self.head)
        
    
    def _remove_node(self, node):
        tmp = node.prev
        tmp.next = node.next
        node.next.prev = tmp
    
    #add node1 after node2
    # node2->next == node1
    def _add_node(self, node1, node2):
        tmp = node2.next
        node2.next = node1
        node1.prev = node2
        node1.next = tmp
        tmp.prev = node1

    
    def put(self, key: int, value: int) -> None:
        # check if key is in the current cache
        if key in self.cache:
            nodeToUpdate = self.cache[key]
            nodeToUpdate.val = value
            self._moveToTop(nodeToUpdate)
            return
        # check capacity
        # if curCapa == capacity, pop LRU chache
        
        if len(self.cache) == self.capacity:
            keyToPop = self.tail.prev.key
            self._remove_node(self.tail.prev)            
            self.cache.pop(keyToPop)

            
        # create a new node with value and add it to head
        newNode = NodeList(key,value)
        
        self._add_node(newNode, self.head)
        # add it to hash
        self.cache[key] = newNode
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)