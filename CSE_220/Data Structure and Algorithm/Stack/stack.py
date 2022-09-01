class Stack:
  def __init__(self, size=20):
      self.stack_array = []
      self._size = size



  def push(self, data):
      if len(self.stack_array) >= self._size:
          raise Exception('Stack overflow')
      else:
          self.stack_array.append(data)

  def pop(self):
      if len(self.stack_array) <= 0:
          raise Exception('Stack underflow')
      else:
          return self.stack_array.pop()

  def peek(self):
      if len(self.stack_array) <= 0:
          raise Exception('Stack underflow')
      else:
          return self.stack_array[-1]