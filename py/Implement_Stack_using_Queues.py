class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []
        self.curr_top = 0

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue2.append(x)
        self.curr_top = x
        while len(self.queue1):
            self.queue2.append(self.queue1.pop(0))
        temp = self.queue2
        self.queue2 = self.queue1
        self.queue1 = temp
        # self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        p = self.queue1.pop(0)
        if len(self.queue1):
            self.curr_top = self.queue1[0]

        return p

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.empty() is False:
            return self.curr_top

    def empty(self) -> bool:
        """
        Returns whether the stack i
        """
        return len(self.queue1) == 0


if __name__ == '__main__':
    s = [2, 1]
    s.pop(len(s) - 1)
    print(s)