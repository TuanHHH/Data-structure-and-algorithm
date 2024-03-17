class Animal:
    def __init__(self,species = None,name = None) -> None:
        assert species in ["dog",'cat'], f'only dog and cat'
        self.name = name
        self.next:Animal = None
        self.species = species

class LinkedList:
    def __init__(self) -> None:
        self.head:Animal = None
        self.tail:Animal = None

class Queue:
    def __init__(self) -> None:
        self.LinkedList = LinkedList()

    def isEmpty(self):
        return self.LinkedList.head == None

    def enqueue(self,animal:Animal):
        if isinstance(animal,list):
            for i in animal:
                self.enqueue(i)
        else:
            if self.LinkedList.head == None and self.LinkedList.tail == None:
                self.LinkedList.head = animal
                self.LinkedList.tail = animal
            else:
                self.LinkedList.tail.next = animal
                self.LinkedList.tail = animal

    def dequeue_any(self):
        if self.isEmpty():
            return "There isn't any to adopt"
        else:
            animal = self.LinkedList.head
            if animal.species == 'dog':
                self.LinkedList.head = self.LinkedList.head.next
                if animal.name == None:
                    return f'The animal has been adopt is a dog'
                else:
                    return f'The dog has been adopted has name {animal.name}'
            if self.LinkedList.head.species == 'cat':
                self.LinkedList.head = self.LinkedList.head.next
                if animal.name == None:
                    return f'The animal has been adopt is a cat'
                else:
                    return f'The cat has been adopted has name {animal.name}'
                
    def dequeue_dog(self):
        if self.isEmpty():
            return "There isn't any animal to adopt"
        else:
            animal_obj = self.LinkedList.head
            if animal_obj.species == 'dog':
                self.LinkedList.head = self.LinkedList.head.next
                if animal_obj.name == None:
                    return f'The animal has been adopt is a dog'
                else:
                    return f'The dog has been adopted has name {animal_obj.name}'
            else:
                return f'Next animal is not a Dog'
            
    def dequeue_cat(self):
        if self.isEmpty():
            return f"There isn't any animal to adopt"
        else:
            animal = self.LinkedList.head
            if animal.species =='cat':
                self.LinkedList.head = self.LinkedList.head.next
                if animal.name !=  None:
                    return f'The cat has been adopted has name {animal.name}'
                else:
                    return f'The animal has been adopt is a cat'
            else:
                return f'Next animal is not a Cat'
            
    def peek(self):
        if self.isEmpty():
            return "There isn't any animal to adopt"
        else:
            animal = self.LinkedList.head
            if animal.name == None:
                return f'Next animal is a {animal.species}'
            else:
                return f'Next animal is a {animal.species} and has name is {animal.name}'
    def deleteQueue(self):
        self.LinkedList.head = None

c1 = Animal('cat')
c2 = Animal('cat')
c3 = Animal('cat')
d1 = Animal('dog')
d2 = Animal('dog')
animal_shelter = Queue()
animal_shelter.enqueue([c1,c2,d1,d2,c3])
print(animal_shelter.peek())
print(animal_shelter.dequeue_any())
print(animal_shelter.dequeue_cat())
print(animal_shelter.dequeue_dog())
print(animal_shelter.dequeue_cat())
print(animal_shelter.dequeue_cat())
print(animal_shelter.dequeue_dog())
print(animal_shelter.dequeue_dog())
print(animal_shelter.dequeue_dog())
print(animal_shelter.dequeue_cat())
print(animal_shelter.dequeue_cat())