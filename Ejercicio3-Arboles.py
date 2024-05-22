class Node:
    __slots__ = 'value', 'next'

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

    def __str__(self):
        result = [str(x.value) for x in self]
        return ' '.join(result)


class queue:

    def __init__(self):
        self.linkedlist = LinkedList()

    def __str__(self):
        result = [str(x.value) for x in self.queue]
        return ' '.join(result)

    def is_empty(self):
        return self.linkedlist.head == None

    def enqueue(self, e):
        new_node = Node(e)
        if self.linkedlist.head == None:
            self.linkedlist.head = new_node
            self.linkedlist.tail = new_node
        else:
            new_node.next = None
            self.linkedlist.tail.next = new_node
            self.linkedlist.tail = new_node

    def dequeue(self):
        if self.is_empty():
            return "No hay elementos en la lista"
        else:
            popped_node = self.linkedlist.head
            if self.linkedlist.head == self.linkedlist.tail:
                self.linkedlist.head = None
                self.linkedlist.tail = None
            else:
                self.linkedlist.head = self.linkedlist.head.next
            popped_node.next = None
            return popped_node


class BSTNode:

    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None

    def __str__(self, level=0):
        ret = "  " * level + str(self.data) + "\n"

        if self.leftchild:
            ret += self.leftchild.__str__(level + 1)

        if self.rightchild:
            ret += self.rightchild.__str__(level + 1)

        return ret


def printTree(Node, prefix="", is_left=True):
    if not Node:
        return

    if Node.rightchild:
        printTree(Node.rightchild, prefix + ("│    " if is_left else "    "), False)

    print(prefix + ("└── " if is_left else "┌── ") + str(Node.data))

    if Node.leftchild:
        printTree(Node.leftchild, prefix + ("     " if is_left else "│   "), True)


def preOrderTraversal(rootNode):
    if not rootNode:
        return

    print(rootNode.data)
    preOrderTraversal(rootNode.leftchild)
    preOrderTraversal(rootNode.rightchild)


def inOrderTraversal(rootNode, values):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftchild, values)
    values.append(rootNode.data)
    inOrderTraversal(rootNode.rightchild, values)


def postOrderTraversal(rootNode):
    if not rootNode:
        return

    postOrderTraversal(rootNode.leftchild)
    postOrderTraversal(rootNode.rightchild)
    print(rootNode.data)


def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customqueue = queue()
        customqueue.enqueue(rootNode)

        while not (customqueue.is_empty()):
            current = customqueue.dequeue()
            print(current.value.data)
            if (current.value.leftchild is not None):
                customqueue.enqueue(current.value.leftchild)
            if (current.value.rightchild is not None):
                customqueue.enqueue(current.value.rightchild)


def insertNode(rootNode, value):
    if rootNode.data == None:
        rootNode.data = value
    elif value < rootNode.data:
        if rootNode.leftchild is None:
            rootNode.leftchild = BSTNode(value)
        else:
            insertNode(rootNode.leftchild, value)
    else:
        if rootNode.rightchild is None:
            rootNode.rightchild = BSTNode(value)
        else:
            insertNode(rootNode.rightchild, value)


def searchNode(rootNode, value):
    if rootNode is None:
        return

    if value < rootNode.data:
        print("ingresa izquierda")
        print(rootNode.data)
        if rootNode.leftchild is not None:
            if rootNode.leftchild.data == value:
                return "el nodo con valor {} SI fue encontrado".format(value)
            return searchNode(rootNode.leftchild, value)
        else:
            return "el nodo con valor {} NO fue encontrado".format(value)
    else:
        print("ingresa derecha")
        print(rootNode.data)
        if rootNode.rightchild is not None:
            if rootNode.rightchild.data == value:
                return "el nodo con valor {} SI fue encontrado".format(value)
            return searchNode(rootNode.rightchild, value)
        else:
            return "el nodo con valor {} NO fue encontrado".format(value)


def deleteNode(rootNode, value):
    if rootNode is None:
        return rootNode

    if value < rootNode.data:
        rootNode.leftchild = deleteNode(rootNode.leftchild, value)
    elif value > rootNode.data:
        rootNode.rightchild = deleteNode(rootNode.rightchild, value)
    else:
        # caso 1 no tiene hijos
        if rootNode.leftchild is None and rootNode.rightchild is None:
            return None
        # caso 2 tiene ambos hijos
        elif rootNode.leftchild is not None and rootNode.rightchild is not None:
            tempNode = minsuccesor(rootNode.rightchild)
            tempData = tempNode.data
            deleteNode(rootNode, tempData)
            rootNode.data = tempData
        # caso hijo a la izquierda
        elif rootNode.leftchild is not None:
            return rootNode.leftchild
        # caso hijo a la derecha
        else:
            return rootNode.rightchild

    return rootNode


def minsuccesor(rootNode):
    if rootNode.leftchild is not None:
        return minsuccesor(rootNode.leftchild)

    return rootNode

def min_absolute_diff(root):
    aux = []
    inOrderTraversal(root, aux)
    print(aux)
    num_min = 99999999999999
    for i in range(1, len(aux)):
        num_min = min(num_min, aux[i] - aux[i - 1])
    return num_min


root = BSTNode(4)
insertNode(root, 2)
insertNode(root, 6)
insertNode(root, 1)
insertNode(root, 3)
printTree(root)
print(min_absolute_diff(root))
