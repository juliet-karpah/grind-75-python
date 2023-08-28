class Stack:
    """last In First Out
    
    """

    def __init__(self):
        self._data = []

    def top(self):
        if self.is_empty():
            raise Exception("stack is empty")
        return self._data[-1]
    
    def push(self, el):
        self._data.append(el)

    def is_empty(self):
        return len(self._data) == 0
    
    def pop(self):
        if self.is_empty():
            raise Exception("stack is empty")
        return self._data.pop()

    def __len__(self):
        return len(self._data)
