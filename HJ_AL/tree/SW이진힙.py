class Node:
    def __init__(self,value,parents=None):
        self.value = value
        self.parents = parents
        self.left = None
        self.right = None

class Binaryheap:
    def __init__(self):
        self.root=None
        self.size = 0

    def insert(self,value):
        self.size += 1
        #case 1, root 없을 때
        if self.root == None:
            self.root = Node(value)
        elif value > self.root:
            temp = self.root
            while True:
                if temp.left == None:
                    temp.left = Node(value)
                if temp.right == None:
                    temp.right = Node(value)


