class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.stack2) == 0:
            while len(self.stack1):
                curr = self.stack1.pop()
                self.stack2.append(curr)
        return self.stack2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.stack2) == 0:
            while len(self.stack1):
                curr = self.stack1.pop()
                self.stack2.append(curr)
        return self.stack2[-1]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack1) + len(self.stack2) == 0


if __name__ == '__main__':
    s = [1, 2, 3]
    s.pop()
    print(s)

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()