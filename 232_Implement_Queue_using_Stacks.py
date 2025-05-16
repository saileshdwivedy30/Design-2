# The queue is implemented using two stacks: one for incoming elements and one for outgoing elements.
# When an element is pushed, it is added to stack_in. When performing pop or peek operations elements moved from stack_in to stack_out if stack_out is empty.
# This allows for FIFO behavior while using only stack operations, achieving amortized O(1) time complexity for all operations.

# TC - O(1)
# SC - O(n), we store all elements in two stacks

class MyQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()

    def peek(self) -> int:
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out[-1]

    def empty(self) -> bool:
        return not self.stack_in and not self.stack_out

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()