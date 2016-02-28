# Stack implementation (LIFO)

#TODO check bounds? size?
class Stack:
    def __init__(self):
        self.internal_array = []  # well, actually a list
        self.stack_pointer = 0

    def pop(self):
        self.stack_pointer -= 1
        print("Popping item at position", self.stack_pointer)
        value = self.internal_array[self.stack_pointer]
        self.internal_array[self.stack_pointer] = None
        return value

    def push(self, value):
        print("Pushing %d to position %d" % (value, self.stack_pointer))
        self.internal_array.insert(self.stack_pointer, value)
        self.stack_pointer += 1

my_stack = Stack()
for i in range(0,10):
    my_stack.push(i)
print("Stack:", my_stack.internal_array)
for i in range(0,10):
    print("Popped:", my_stack.pop())
    print("Stack:", my_stack.internal_array)