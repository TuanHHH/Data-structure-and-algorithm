class StackSet:
    def __init__(self,threshold) -> None:
        self.threshold = threshold
        self.stack = [[]]

    def push(self,value):
        if len(self.stack[-1]) == self.threshold:
            self.stack.append([value])
        else:
            self.stack[-1].append(value)
    
    def pop(self):
        # no stacks
        if not self.stack:
            self.stack = [[]]
            return None
        # one stack but it is empty
        elif len(self.stack) == 0 or len(self.stack[-1]) == 0:
            self.stack.pop()  #Loai bo stack rong
            return self.pop()
        else:
            return self.stack[-1].pop()

    def pop_at(self,index):
        if not self.stack or index>= len(self.stack):
            return None
        elif len (self.stack[index])>0:
            res = self.stack[index].pop()
            return res
        else:
            return None

plate_stack = StackSet(3)
plate_stack.push(1)
plate_stack.push(2)
plate_stack.push(3)
plate_stack.push(4)
plate_stack.push(5)
plate_stack.push(6)
plate_stack.push(7)
plate_stack.push(8)
print(plate_stack.pop())
print(plate_stack.pop())
print(plate_stack.pop())
print(plate_stack.pop())
print(plate_stack.pop())
print(plate_stack.pop())
print(plate_stack.pop())
print(plate_stack.pop())
print(plate_stack.pop())
print(plate_stack.stack)
plate_stack.push(1)
plate_stack.push(2)
plate_stack.push(3)
plate_stack.push(4)
plate_stack.push(5)
plate_stack.push(6)
plate_stack.push(7)
plate_stack.push(8)
print(plate_stack.stack)
print(plate_stack.pop_at(1))
print(plate_stack.stack)
plate_stack.push(10)
plate_stack.push(10)
plate_stack.push(10)
plate_stack.push(10)
print(plate_stack.pop_at(1))
print(plate_stack.pop_at(1))
print(plate_stack.pop_at(1))
print(plate_stack.pop_at(0))
print(plate_stack.stack)
print(plate_stack.pop())
print(plate_stack.pop())
print(plate_stack.stack)
print(plate_stack.pop())
print(plate_stack.pop())
print(plate_stack.stack)
print(plate_stack.pop())
print(plate_stack.stack)
print(plate_stack.pop())
print(plate_stack.stack)
print(plate_stack.pop())
print(plate_stack.stack)
print(plate_stack.pop())
print(plate_stack.stack)
