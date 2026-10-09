class MyQueue:

    def __init__(self):
        self.s1 = []   # input stack: new elements go here
        self.s2 = []   # output stack: elements are popped from here

    def push(self, x: int) -> None:
        self.s1.append(x)

    def _transfer(self) -> None:
        # only refill s2 when it's empty, so order is preserved
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

    def pop(self) -> int:
        if self.empty():
            return -1
        self._transfer()
        return self.s2.pop()

    def peek(self) -> int:
        if self.empty():
            return -1
        self._transfer()
        return self.s2[-1]

    def empty(self) -> bool:
        return not self.s1 and not self.s2

    def size(self) -> int:
        return len(self.s1) + len(self.s2)