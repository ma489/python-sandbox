class BloomFilter:
    DEFAULT_K = 10  # "10 bits per element are required for a 1% false positive probability"
    FNV_OFFSET_BASIS = 14695981039346656037
    FNV_PRIME = 1099511628211
    THIRTYTWO_ONES = 0b11111111111111111111111111111111
    EIGHT_ONES = 0b11111111

    def __init__(self, size, k=DEFAULT_K):
        self.k = k
        self.size = size
        self.backing_array = [0] * size

    def add(self, element):
        indices = self.apply_hash_functions(element)
        for index in indices:
            self.backing_array[index] = 1

    def query(self, element):
        indices = self.apply_hash_functions(element)
        for index in indices:
            if self.backing_array[index] == 0:
                return False
        return True

    def apply_hash_functions(self, element):
        fnv_result = self.apply_fnv_hash(element)
        upper_bits, lower_bits = self.split_integer(fnv_result)
        indices = []
        for i in range(0, self.k):
            hash_i = ((upper_bits + lower_bits) * i) % self.size
            indices.append(hash_i)
        return indices

    # Fowler–Noll–Vo_hash_function
    def apply_fnv_hash(self, element):
        fnv_hash = BloomFilter.FNV_OFFSET_BASIS
        bytes = self.get_bytes(element)
        for byte in bytes:
            fnv_hash *= BloomFilter.FNV_PRIME
            fnv_hash ^= byte
        return fnv_hash

    def get_bytes(self, element):
        bytes = []
        for i in range(0, 8):
            byte = element & BloomFilter.EIGHT_ONES
            bytes.append(byte)
            element >>= 8
        return bytes

    def split_integer(self, element):
        upper_thirtytwo_bits = element >> 32
        lower_thirtytwo_bits = element & BloomFilter.THIRTYTWO_ONES
        return upper_thirtytwo_bits, lower_thirtytwo_bits


def is_even(i):
    return i % 2 == 0


bloom_filter = BloomFilter(size=8000)
print("Testing Bloom filter")
test_size = 1000
print("Adding", test_size, "elements...")
for i in range(0, test_size):
    if is_even(i): bloom_filter.add(i)

print("Querying...")
number_incorrect = 0
for i in range(0, test_size):
    result = bloom_filter.query(i)
    truth = is_even(i)
    if result != truth: number_incorrect += 1

print("Results:")
percentage_wrong = round((number_incorrect / float(test_size)) *100,2)
print("Got", number_incorrect, "incorrect, out of", test_size, "-", percentage_wrong, "%")
