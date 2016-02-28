# Queue implementation (FIFO)

class Queue:
    def __init__(self, size): # TODO remove size? extend "array"?
        self.internal_array = [None] * size
        self.start_pointer = 0
        self.end_pointer = 0
        self.size = size

    def enqueue(self, value):
        if self.start_pointer == self.end_pointer and self.start_pointer != 0:
            return False
        self.internal_array[self.end_pointer] = value
        self.end_pointer += 1
        if self.end_pointer >= self.size:
            self.end_pointer = 0
        # print(self.end_pointer)
        return True

    def dequeue(self):
        value = self.internal_array[self.start_pointer]
        self.internal_array[self.start_pointer] = None
        self.start_pointer += 1
        if self.start_pointer >= self.size:
            self.start_pointer = 0
        return value

    def peek(self):
        return self.internal_array[self.start_pointer]  # TODO


my_queue = Queue(10)
for i in range(0, 9):
    my_queue.enqueue(i)
print("Queue:", my_queue.internal_array)
for i in range(0, 5):
    print("Dequeued:", my_queue.dequeue())
    print("Queue:", my_queue.internal_array)
for i in range(9, 18):
    print("Enqueuing", i)
    is_enqueued = my_queue.enqueue(i)
    if not is_enqueued:
        print("Failed to enqueue", i)
    print("Queue:", my_queue.internal_array)