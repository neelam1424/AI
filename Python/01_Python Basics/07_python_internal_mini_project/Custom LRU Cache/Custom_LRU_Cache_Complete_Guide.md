# Custom LRU Cache in Python — Complete Beginner Guide

# 1. Problem Statement

Build a cache with fixed capacity.

When the cache becomes full:

- Remove the Least Recently Used (LRU) item.

LRU means:

> The item that has not been used for the longest time.

---

# 2. What Is a Cache?

A cache is temporary storage used to make programs faster.

Examples:

- Browser cache
- API cache
- Database cache
- Redis
- Operating systems

Example:

First request:

Server → Slow

Second request:

Cache → Fast

---

# 3. Why LRU Cache?

Suppose cache size is 2.

Add:

A, B

Cache:

A B

Use A:

B A

Now add C.

Cache full.

Remove:

B

because B is least recently used.

Final:

A C

---

# 4. Core Idea

LRU Cache uses two data structures.

1. Dictionary (Hash Map)
2. Doubly Linked List

Why?

Dictionary:

- Fast lookup
- O(1)

Linked List:

- Maintains usage order
- O(1) insert/remove

Together:

- O(1) get
- O(1) put

---

# 5. Project Algorithm

1. Create Node class.
2. Create LRUCache class.
3. Store capacity.
4. Create dictionary.
5. Create left and right dummy nodes.
6. Connect dummy nodes.
7. Write remove().
8. Write insert().
9. Write get().
10. Write put().
11. Add test code.

---

# 6. Node Concept

A node stores:

- key
- value
- previous node
- next node

Example:

Node(1, "A")

Diagram:

prev ← Node → next

Code:

```python
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
```

Why needed?

Each cache item must know:

- who is before it
- who is after it

So we can move/remove quickly.

---

# 7. LRUCache Constructor

Code:

```python
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
```

Meaning:

capacity:

Maximum cache size.

cache:

Dictionary for O(1) lookup.

Example:

```python
{
    1: Node(1,"A"),
    2: Node(2,"B")
}
```

---

# 8. Dummy Nodes

We create:

- left dummy
- right dummy

Code:

```python
self.left = Node(0,0)
self.right = Node(0,0)

self.left.next = self.right
self.right.prev = self.left
```

Why?

They simplify insertion and deletion.

Without dummy nodes:

Many edge cases.

With dummy nodes:

Cleaner logic.

Initial:

LEFT <-> RIGHT

Real nodes go in between.

Diagram:

LEFT <-> 1:A <-> 2:B <-> RIGHT

Meaning:

1:A → least recently used

2:B → most recently used

---

# 9. remove() Concept

Purpose:

Remove node from linked list.

Code:

```python
def remove(self, node):
    prev_node = node.prev
    next_node = node.next

    prev_node.next = next_node
    next_node.prev = prev_node
```

Example:

Before:

1:A <-> 2:B <-> 3:C

Remove:

2:B

After:

1:A <-> 3:C

Line-by-line:

1.

```python
prev_node = node.prev
```

Get previous node.

2.

```python
next_node = node.next
```

Get next node.

3.

```python
prev_node.next = next_node
```

Skip current node.

4.

```python
next_node.prev = prev_node
```

Reconnect backward link.

Diagram:

Before:

1:A <-> 2:B <-> 3:C

After:

1:A <------> 3:C

Why needed?

Whenever a node is used:

- Remove it
- Reinsert it

---

# 10. insert() Concept

Purpose:

Insert node before RIGHT.

RIGHT means:

Most recently used side.

Code:

```python
def insert(self, node):
    prev_node = self.right.prev

    prev_node.next = node
    node.prev = prev_node

    node.next = self.right
    self.right.prev = node
```

Example:

Before:

LEFT <-> 1:A <-> RIGHT

Insert:

2:B

After:

LEFT <-> 1:A <-> 2:B <-> RIGHT

Line-by-line:

1.

```python
prev_node = self.right.prev
```

Get current last node.

2.

```python
prev_node.next = node
```

Old last points to new node.

3.

```python
node.prev = prev_node
```

New node points backward.

4.

```python
node.next = self.right
```

New node points to RIGHT.

5.

```python
self.right.prev = node
```

RIGHT points back.

Why needed?

Every:

- new item
- updated item
- recently used item

becomes:

Most Recently Used.

---

# 11. get() Concept

Purpose:

Return value.

Also:

Move node to MRU side.

Code:

```python
def get(self, key):
    if key not in self.cache:
        return -1

    node = self.cache[key]

    self.remove(node)
    self.insert(node)

    return node.value
```

Example:

Before:

1:A <-> 2:B

get(1)

After:

2:B <-> 1:A

1 becomes MRU.

---

# 12. put() Concept

Purpose:

Insert or update item.

Code:

```python
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
```

Meaning:

If key exists:

Remove old node.

Create new node.

Insert near RIGHT.

If size exceeds capacity:

Remove:

LEFT.next

because:

LEFT.next = Least Recently Used.

---

# 13. Complete Code

```python
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

        self.left = Node(0,0)
        self.right = Node(0,0)

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
```

---

# 14. Test Code

Write test code at bottom.

```python
cache = LRUCache(2)

cache.put(1, "A")
cache.put(2, "B")

print(cache.get(1))

cache.put(3, "C")

print(cache.get(2))
print(cache.get(3))
```

Run:

```bash
python3 Custom_LRU_cache.py
```

Output:

```text
A
-1
C
```

---

# 15. Internal Working Flow

When:

get(1)

Steps:

1. Find node in dictionary.
2. Remove node.
3. Insert near RIGHT.
4. Return value.

When:

put(3)

Steps:

1. Create node.
2. Insert near RIGHT.
3. If size exceeded:
4. Remove LEFT.next.

---

# 16. Time Complexity

get()

O(1)

put()

O(1)

remove()

O(1)

insert()

O(1)

Why?

Dictionary:

Fast lookup.

Linked list:

Fast insertion and deletion.

---

# 17. What You Learn

This project teaches:

- Hash maps
- Linked lists
- Object-oriented programming
- Cache design
- Memory references
- Time complexity
- System design basics
- Real-world caching logic

Used in:

- Browsers
- Databases
- Redis
- APIs
- Operating systems

---

# 18. Mental Model

Remember:

Dictionary = Find fast

Linked list = Track usage

LEFT = Oldest

RIGHT = Newest

remove()

Cut node.

insert()

Attach before RIGHT.
