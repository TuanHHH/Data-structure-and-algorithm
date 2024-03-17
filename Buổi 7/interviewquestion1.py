class Stack:
    def __init__(self,list:list) -> None:
        self.list = list

    def isEmpty(self):
        return len(self.list) == 0
    
    def peek(self):
        if self.isEmpty():
            return 'There is not any element in stack'
        else:
            return self.list[0]
        
    def push(self,value):
        if isinstance(value,list):
            self.list.insert(0,value)
        else:
            for i in value:
                self.push(i)

    def pop_first(self):
        if self.isEmpty():
            return "There is not any element in stack"
        else:
            return self.list.pop(0)

class ThreeInOne:
    def __init__(self,list:list) -> None:
        self.list = list

        lenlist = len(self.list)
        print(len(self.list))
        l = [0,0,0]
        for i in range(0,3):
            l[i] = lenlist - lenlist//(3-i)
            lenlist = lenlist - lenlist//(3-i)
        
        l.reverse()
        l.append(len(self.list))
        st1,st2,st3 = [],[],[]
        st1 = self.list[l[0]:l[1]]
        st2 = self.list[l[1]:l[2]]
        st3 = self.list[l[2]:l[3]]
        print(self.list)
        print(self.list[l[0]:l[1]])
        print(l)
        print(st1,st2,st3)

        self.Stack1 = Stack(st1)
        self.Stack2 = Stack(st2)
        self.Stack3 = Stack(st3)

    def get_all_stack1(self):
        temp ="Stack1:"
        print(self.Stack1.isEmpty())
        while self.Stack1.isEmpty() == False:
            temp+=f' {self.Stack1.pop_first()}, '
        return temp.rstrip(", ")
    
    def get_all_stack2(self):
        temp ="Stack2:"
        while self.Stack2.isEmpty() == False:
            temp+=f' {self.Stack2.pop_first()}, '
        return temp.rstrip(", ")
    
    def get_all_stack3(self):
        temp ="Stack3:"
        while self.Stack3.isEmpty() == False:
            temp+=f' {self.Stack3.pop_first()}, '
        return temp.rstrip(", ")
    
my_list = [0,1,2,3,4,5,6,7,8,9]
threeInOne = ThreeInOne(my_list)
print(threeInOne.get_all_stack1())
print(threeInOne.get_all_stack2())
print(threeInOne.get_all_stack3())