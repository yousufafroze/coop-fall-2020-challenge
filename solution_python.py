class EventSourcer():
    # Do not change the signature of any functions

    def __init__(self):
        self.value = 0
        self.stack = [0]
        self.redo_lst = []

    def add(self, num: int):
        self.value += num
        self.stack.append(self.value)
        return self.value

    def subtract(self, num: int):
        self.value -= num
        self.stack.append(self.value)
        return self.value

    def undo(self):
        if self.stack:
          old_val = self.stack.pop()
          self.redo_lst.append(old_val)
          self.value = self.stack[-1]
        return self.value
        

    def redo(self):
        if self.redo_lst:
          old_val = self.redo_lst.pop()
          self.stack.append(old_val)
          self.value = self.stack[-1]
        return self.value

    def bulk_undo(self, steps: int):
        for i in range(steps):
          res = self.undo()
        return res
    def bulk_redo(self, steps: int):
        for i in range(steps):
          res = self.redo()
        return res
  

  