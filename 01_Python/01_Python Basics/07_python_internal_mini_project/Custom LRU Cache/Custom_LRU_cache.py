# Custom LRU cache
# Steps for this project
# 1: Create a Node class to store key, value, prev, next
# 2: Create an LRUCache class.
# 3: Store cache capacity
# 4: Create a dictionary for O(1) lookup
# 5: Create two dummy nodes: 
#           left = least recently used side
#           right = most recently used side
# 6: Connect left and right
# 7: For get(key):
#        a: If key not present, return -1
#        b: Get the node from dictionary
#        c: Remove node from currect position
#        d: Insert node near right side.
#        e: Return node value.
# 8: For put(key, value):
#        a: If key already exists, remove old node.
#        b: Create new node
#        c: Store it in dictionary.
#        d: Insert it near right side.
#        e: If cache size > capacity:
#           - Remove node after left.
#           - Delete node after left




class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def insert(self, node):
        prev_node = self.right.prev

        prev_node.next = node
        node.prev = prev_node

        node.next = self.right
        self.right.prev = node

    def get(self, key):
        if key not in self.cache:
            return -1

        node = self.cache[key]

        self.remove(node)
        self.insert(node)

        return node.value

    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])

        new_node = Node(key, value)
        self.cache[key] = new_node
        self.insert(new_node)

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


# ------------------
# TEST CODE
# ------------------

cache = LRUCache(2)

cache.put(1, "A")
cache.put(2, "B")

print(cache.get(1))

cache.put(3, "C")

print(cache.get(2))
print(cache.get(3))