class Node:
    def __init__(self,key, value):
        self.value = value
        self.key = key
        self.prev = None
        self.next = None

class DDL:
    def __init__(self):
        self.right = Node(0,0)
        self.left = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def add(self,node):
        prev =  self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node

    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def remove_last(self):

        if self.left.next == self.right:
            return None
        node = self.left.next
        self.remove(node)

        return node

class LRU:
    
    def __init__(self,capacity):
        self.capacity = capacity
        self.cache = {}
        self.ddl = DDL()

    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.ddl.remove(node)
        self.ddl.add(node)

        return node.value
    
    def put(self, key , value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.ddl.remove(node)
            self.ddl.add(node)
        
        else:
            if len(self.cache) == self.capacity:
                last = self.ddl.remove_last()

                if last:
                    del self.cache[last.key]

            new_node = Node(key, value)
            self.ddl.add(new_node)
            self.cache[key] = new_node

    