#  associative array aka map (abstract data type) - a collection of (key, value) pairs
# Hash map (data structure) that implements associative array
import math


class HashMap:
    def __init__(self, initial_size=16, initial_load_factor=0.75):  # recommend powers of two
        self.initial_size = initial_size
        self.internal_array = [None] * initial_size
        self.target_load_factor = initial_load_factor
        self.number_of_items = 0

    def insert(self, key, value):  # aka put
        if self.get_load_factor() > self.target_load_factor:
            print("Resizing & Rehashing - load factor", self.get_load_factor(), " > ", self.target_load_factor)
            self.resize_and_rehash()
        array_index = self.get_array_index(key, len(self.internal_array))
        self.stick_item_in(self.internal_array, array_index, key, value)
        self.number_of_items += 1

    def stick_item_in(self, array, array_index, key, value):
        list_in_this_bucket = array[array_index]
        if list_in_this_bucket is None:
            list_in_this_bucket = []
        list_in_this_bucket.append((key, value))
        array[array_index] = list_in_this_bucket

    def resize_and_rehash(self):
        # x = self.number_of_items * self.target_load_factor
        # print("x", x)
        # power_of_two = math.ceil(math.log(x) / math.log(2))
        # print("power_of_two", power_of_two)
        # new_number_of_buckets = int(math.pow(2, power_of_two))
        new_number_of_buckets = len(self.internal_array) * 2
        print("New internal array size:", new_number_of_buckets)
        # print("new_number_of_buckets", new_number_of_buckets)
        new_internal_array = [None] * new_number_of_buckets
        new_internal_array_length = len(new_internal_array)
        for bucket in self.internal_array:
            if bucket is None:
                continue
            for (k, v) in bucket:
                new_array_index = self.get_array_index(k, new_internal_array_length)
                self.stick_item_in(new_internal_array, new_array_index, k, v)
        self.internal_array = new_internal_array

    # we need an injective function from the hash space to the array size range
    # mod is ok, but computationally inefficient - instead use bit masking a la Java
    def get_array_index(self, key, internal_array_length):
        hash_of_key = hash(key)
        mask = internal_array_length - 1
        array_index = mask & hash_of_key
        return array_index

    def delete(self, key):  # aka remove
        # TODO
        pass

    def modify(self, key, new_value):
        # TODO
        pass

    def lookup(self, key):
        index = self.get_array_index(key, len(self.internal_array))
        list_in_this_bucket = self.internal_array[index]
        if list_in_this_bucket is None:
            return None
        else:
            for (k, v) in list_in_this_bucket:  # huh?
                if k == key:
                    return v
            return None

    def get_load_factor(self):
        number_of_bins = len(self.internal_array)
        # print("number_of_bins", number_of_bins, "self.number_of_items", self.number_of_items)
        return self.number_of_items / number_of_bins  # (aka number of entries / number of buckets)


init_size = 16
hmap = HashMap(init_size)
for k in range(0, 100):
    val = str(chr(k + 97))
    print(k, val)
    hmap.insert(k, val)
    # print(k)
    # print("load factor", hmap.get_load_factor())
print("Map contents: ", hmap.internal_array)
# print("load factor", hmap.get_load_factor())
for k in range(0, 100):
    value = hmap.lookup(k)
    print("Looking up:", k, " - Found value:", value)
