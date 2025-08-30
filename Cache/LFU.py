from collections import defaultdict

class Node:
    def __init__(self,key, value ):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None

class DLL:

    def __init__(self):
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
        self.size = 0

    def insert(self, node):
        prev = self.right.prev
        prev.next = node
        self.right.prev = node
        node.prev = prev
        node.next = self.right
        self.size += 1

    def remove(self, node):
        node_nxt = node.next
        node_prev = node.prev
        node_nxt.prev , node_prev.next = node_prev, node_nxt
        self.size -= 1

    def pop_last(self):
        if self.size == 0: return None
        node =self.left.next
        node_next = node.next
        self.right.next , node_next.prev = node_next,  self.left

        return node

class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.min_freq = 0
        self.size = 0
        self.key_node = {}
        self.freq_ddl = defaultdict(DDL)

    def _update(self, node):
        freq = node.freq
        self.freq_ddl[freq].remove(node)

        if freq == self.min_freq and self.freq_ddl[freq].size == 0:
            self.min_freq += 1

        node.freq += 1
        self.freq_ddl[node.freq].insert(node)

    def get(self,key):
        if key not in self.key_node:
            return -1
        node = self.key_node[key]
        self._update(node)

        return node.value
    
    def put(self, key , value):
        if self.capacity == 0: return

        if key in self.key_node:
            node = self.key_node[key]
            node.value = value
            self._update(node)

        else:

            if self.size == self.capacity:
                node_remove = self.freq_ddl[self.min_freq].pop_last()
                del self.key_node[node_remove.key]
                self.size -= 1

            new_node = Node(key, value)
            self.key_node[key] = new_node
            self.freq_ddl[1].insert(new_node)
            self.min_freq = 1
            self.size += 1

    

