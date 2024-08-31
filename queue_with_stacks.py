class OptimizedQueueWithStacks:
    def __init__(self):
        self.stack_in = []  # Stack for enqueue operations
        self.stack_out = []  # Stack for dequeue operations

    def enqueue(self, x: int):
        """Add an element to the end of the queue."""
        self.stack_in.append(x)

    def dequeue(self) -> int:
        """
        Remove and return the front element of the queue.
        Amortized O(1) time complexity due to occasional full transfer of stack_in to stack_out.
        """
        if not self.stack_out:  # Only transfer if stack_out is empty
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

        if not self.stack_out:
            raise IndexError("dequeue from empty queue")  # Queue is empty

        return self.stack_out.pop()

# Example usage:
if __name__ == "__main__":
    q = OptimizedQueueWithStacks()
    q.enqueue(1)
    q.enqueue(2)
    print(q.dequeue())  # Output: 1
    print(q.dequeue())  # Output: 2
