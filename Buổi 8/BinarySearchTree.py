class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None
        self.length = 0

    def insert(self,value):
        node = Node(value)
        if self.root == None:
            self.root = node
        else:
            current_node = self.root
            while True:
                if current_node.value > value:
                    if current_node.left != None:
                        current_node =  current_node.left
                    else:
                        current_node.left = node
                        break
                elif current_node.value < value:
                    if current_node.right != None:
                        current_node = current_node.right
                    else:
                        current_node.right = node
                        break
    
    def contain(self,value)->bool:
        current_node = self.root
        while True:
            if current_node.value > value:
                if current_node.left != None:
                    current_node = current_node.left
                else:
                    return False
            elif current_node.value <value:
                if current_node.right != None:
                    current_node = current_node.right
                else:
                    return False
            elif current_node.value == value:
                return True

    def preOrderTraversal(self,current_node="default"):
        if current_node=="default":
            self.preOrderTraversal(self.root)

        else:
            if not current_node:
                return
            print(current_node.value,end=", ")
            self.preOrderTraversal(current_node.left)
            self.preOrderTraversal(current_node.right)

bst = BinarySearchTree()
bst.insert(1)
bst.insert(0)
bst.insert(2)
bst.insert(3)
bst.insert(-1)
print(bst.contain(4))
bst.preOrderTraversal(bst.root)