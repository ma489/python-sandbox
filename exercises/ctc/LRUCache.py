from queue import PriorityQueue
import time


def get_time():
    return time.time()


class KeyPriority:
    def __init__(self, keye, priority):
        self.key = keye
        self.priority = priority

    def __lt__(self, other):
        print("lt", self.key, self.priority, other.key, other.priority)
        return self.priority < other.priority

    def __gt__(self, other):
        print("gt", self.key, self.priority, other.key, other.priority)
        return self.priority > other.priority

    def __eq__(self, other):
        print("eq", self.key, self.priority, other.key, other.priority)
        return self.priority == other.priority

    def __hash__(self, *args, **kwargs):
        return super().__hash__(*args, **kwargs)


class LRUCache:
    def __init__(self, max_size):
        self.max_size = max_size
        self.item_count = 0
        self.internal_dict = {}
        self.lru_queue = PriorityQueue(max_size)
        self.lru_random_access_helper = {}

    def insert(self, key, value):
        if self.item_count == self.max_size:
            self.evict_lru_item()
            self.item_count -= 1
        if self.internal_dict.get(key) is not None:  # Item already present
            return False
        self.internal_dict.update({key: value})
        if self.internal_dict.get(key) is not None:  # check if item inserted correctly
            self.item_count += 1
            time = get_time()
            self.lru_queue.put(KeyPriority(key, time))  # add to LRU_queue
            self.lru_random_access_helper.update({key: time})
            return True
        return False

    def delete(self, key):
        if self.internal_dict.get(key) is None:  # check if item is even present
            return False
        k = self.internal_dict.pop(key)
        if key == k:  # check it was removed correctly
            self.item_count -= 1
            return True
        return False

    def lookup(self, key):
        print("Looking up", key)
        value = self.internal_dict.get(key)
        if value is not None:
            self.adjust_lru(key)
            return value
        return None

    def evict_lru_item(self):
        print("aux", self.lru_random_access_helper)
        print(list(map(lambda x: (x.key, x.priority), self.lru_queue.queue)))
        kp = self.lru_queue.get()
        print("Evicting:", kp.key)
        self.delete(kp.key)

    def adjust_lru(self, keye):
        # print("Adjusting", key)
        old_time = self.lru_random_access_helper.get(keye)
        # print("millis for", key, millis)
        self.lru_queue.queue.remove(KeyPriority(keye, old_time))
        new_time = get_time()
        self.lru_queue.put(KeyPriority(keye, new_time))
        self.lru_random_access_helper.update({keye: new_time})


print("LRU Cache example")
size = 10
lru_cache = LRUCache(size)
print("Initial LRU Cache, with max size", size)
print(lru_cache.internal_dict)
for key in range(0, 10):
    time.sleep(0.5)
    val = str(chr(key + 97))
    print("Key, Value: ", key, val)
    print("LRU Cache before:", lru_cache.internal_dict)
    lru_cache.insert(key, val)
    print("LRU Cache after:", lru_cache.internal_dict)
lru_cache.lookup(9)
ten_val = str(chr(10 + 97))
print("Inserting", 10, ten_val)
print("LRU Cache before:", lru_cache.internal_dict)
lru_cache.insert(10, ten_val)
print("LRU Cache after:", lru_cache.internal_dict)
lru_cache.lookup(1)
elev_val = str(chr(11 + 97))
print("Inserting", 11, elev_val)
print("LRU Cache before:", lru_cache.internal_dict)
lru_cache.insert(11, elev_val)
print("LRU Cache after:", lru_cache.internal_dict)
lru_cache.lookup(2)
lru_cache.lookup(4)
lru_cache.lookup(8)
twelv_val = str(chr(12 + 97))
print("Inserting", 12, twelv_val)
print("LRU Cache before:", lru_cache.internal_dict)
lru_cache.insert(12, twelv_val)
print("LRU Cache after:", lru_cache.internal_dict)
print("Done")
