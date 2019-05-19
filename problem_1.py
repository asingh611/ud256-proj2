import collections


class CacheLRU:

    def __init__(self, capacity=5):
        # Initialize class variables
        self.capacity = capacity  # Max size of the queue
        self.current_queue_size = 0  # How big the queue currently is
        self.cache_queue = collections.deque()
        self.cache_value_lookup = dict()  # Stores values alongside queue for lookup purposes

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.cache_value_lookup:
            return self.cache_value_lookup[key]

        return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.

        # Case 1: There is room in the queue for more items
        if self.current_queue_size < self.capacity:
            self.cache_queue.append(key)  # Add element to end of queue O(1)
            self.cache_value_lookup[key] = value  # Add element to lookup dictionary O(1)
            self.current_queue_size += 1

        # Case 2: No room left in the queue; need to remove oldest (first) element
        else:
            # Step 1: Make room in queue
            oldest_queue_key = self.cache_queue[0]  # Get key of the oldest element, which will need to be removed O(1)
            self.cache_value_lookup.pop(oldest_queue_key)  # Remove entry for oldest element from lookup dictionary O(1)
            self.cache_queue.popleft()  # Remove first element from queue O(1)

            # Step 2: Add new item
            self.cache_queue.append(key)  # Add element to end of queue O(1)
            self.cache_value_lookup[key] = value  # Add element to lookup dictionary O(1)


our_cache = CacheLRU(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
print(our_cache.get(1))         # Case 1: Value exists; returns 1
print(our_cache.get(2))         # Case 1: Value exists; returns 2
print(our_cache.get(3))         # Case 2: Value does not exist; returns -1
our_cache.set(3, 3)
our_cache.set(4, 4)
our_cache.set(5, 5)
our_cache.set(6, 6)             # Added 6th element (capacity exceeded; should remove oldest element)
print(our_cache.get(1))         # Case 3: First element inserted should no longer exist; Should return -1
print(our_cache.get(6))         # Case 4: New element should exist; Should return 6
