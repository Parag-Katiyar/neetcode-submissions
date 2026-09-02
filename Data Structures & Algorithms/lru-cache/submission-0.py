class Node:
    def __init__(self, key: int = 0, val: int = 0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> Node
        # Dummy head and tail to eliminate null-checks
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        """Internal helper to disconnect a node from the doubly linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_tail(self, node: Node):
        """Internal helper to insert a node right before the dummy tail (most recent)."""
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        # Mark as recently used by moving it to the tail
        self._remove(node)
        self._add_to_tail(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update value and refresh position
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._add_to_tail(node)
        else:
            if len(self.cache) >= self.capacity:
                # Evict the least recently used item (node right after head)
                lru_node = self.head.next
                self._remove(lru_node)
                del self.cache[lru_node.key]
            
            # Create and insert new node
            new_node = Node(key, value)
            self._add_to_tail(new_node)
            self.cache[key] = new_node
