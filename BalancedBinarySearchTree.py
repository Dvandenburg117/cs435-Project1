
import random
class Node():
    def __init__(self,value):
        self.right = None
        self.left = None
        self.val = value
        self.height = 1
        self.lvlctr = 0

#get height of given node
def getHeight(root):
    if root is None:
        return 0
    return root.height

def getTravLevel(root):
    if root is None:
        return 0
    return root.lvlctr
#check for the balance factor by subtracting height of children
def getBalance(root):
    if root is None:
        return 0
    return getHeight(root.left) - getHeight(root.right)

#return the smallest value in the tree , will always be in left subtree
def getMinRec(root):
    if root.left is None:
        return root
    return getMinRec(root.left)

def getMinIter(root):
    while root.left is not None:
        root = root.left
    return root

#return the largest value in the tree , will always be in the right subtree
def getMaxRec(root):
    if root.right is None:
        return root
    return getMaxRec(root.right)

def getMaxIter(root):
    while root.right is not None:
        root = root.right
    return root

#rotate root.left.right to root / root.left to root.left.right
def rightRotate(root):
    y = root.left
    T3 = y.right

    # Perform rotation
    y.right = root
    root.left = T3

    # Update heights
    root.height = 1 + max(getHeight(root.left),getHeight(root.right))
    y.height = 1 + max(getHeight(y.left),getHeight(y.right))

    # Return the new root
    return y

#rotate root.right.left to root / root.right to root.right.left
def leftRotate(root):
    y = root.right
    T2 = y.left

    # Perform rotation
    y.left = root
    root.right = T2

    # Update heights
    root.height = 1 + max(getHeight(root.left),getHeight(root.right))
    y.height = 1 + max(getHeight(y.left),getHeight(y.right))

    # Return the new root
    return y

#insert into tree (same as reg bst), then rebalance it
def insertRecBBST(root,node):
    if root is None:
        return node
    elif node.val < root.val:
        root.left = insertRecBBST(root.left,node)
    else:
        root.right = insertRecBBST(root.right,node)

    #update parent height
    root.height = 1 + max(getHeight(root.left),getHeight(root.right))

    #get BF to balance tree
    balance = getBalance(root)

    #start to balance tree for 4 cases
    #Left Left
    if balance > 1 and node.val < root.left.val:
        return rightRotate(root)
    #right right
    if balance < -1 and node.val > root.right.val:
        return leftRotate(root)
    #right left
    if balance < -1 and node.val < root.right.val:
        root.right = rightRotate(root.right)
        return leftRotate(root)
    #left right
    if balance > 1 and node.val > root.left.val:
        root.left = leftRotate(root.left)
        return rightRotate(root)

    return root

def insertIterBST(root,node):#ripped from BST code to compare efficiency
    if root is None:
        root = node
    else:
        while root is not None:
            if root.val > node.val:
                if root.left is None:
                    root.left = node
                    root.height = 1 + max(getHeight(root.left), getHeight(root.right))
                    return node
                else:
                    root = root.left
                    root.height = 1 + max(getHeight(root.left), getHeight(root.right))
            else:
                if root.right is None:
                    root.right = node
                    root.height = 1 + max(getHeight(root.left), getHeight(root.right))
                    return node
                else:
                    root = root.right
                    root.height = 1 + max(getHeight(root.left), getHeight(root.right))
    root.height = 1 + max(getHeight(root.left), getHeight(root.right))
    return node

def insertRecBST(root,node):#ripped from BST code to compare effeciency
    if root is None:
        return node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                root.right = insertRecBST(root.right,node)
        else:
            if root.left is None:
                root.left = node
            else:
                root.left = insertRecBST(root.left,node)
    root.height = 1 + max(getHeight(root.left), getHeight(root.right))
    return root

def insertIterBBST(root,node):
    if root is None:
        root = node
    else:
        while root is not None:
            if root.val > node.val:
                if root.left is None:
                    root.left = node
                    root.lvlctr+=1
                    root.height = 1 + max(getHeight(root.left), getHeight(root.right))
                    return node
                else:
                    root = root.left
                    root.lvlctr += 1
                    root.height = 1 + max(getHeight(root.left), getHeight(root.right))
            else:
                if root.right is None:
                    root.right = node
                    root.lvlctr += 1
                    root.height = 1 + max(getHeight(root.left), getHeight(root.right))
                    return node
                else:
                    root = root.right
                    root.lvlctr += 1
                    root.height = 1 + max(getHeight(root.left), getHeight(root.right))
    root.lvlctr += 1
    root.height = 1 + max(getHeight(root.left), getHeight(root.right))
    while getBalance(root) > 1 or getBalance(root) < -1:
        if getBalance(root) > 1 and node.val < root.left.val:
            root  = rightRotate(root)
        # right right
        if getBalance(root) > 1 and node.val > root.right.val:
            root = leftRotate(root)
        # right left
        if getBalance(root) < -1 and node.val < root.right.val:
            root.right = rightRotate(root.right)
            root = leftRotate(root)
        # left right
        if getBalance(root) > 1 and node.val > root.left.val:
            root.left = leftRotate(root.left)
            root = leftRotate(root)
    return root

#delete node with given key from tree (same as BST), then rebalance it
def deleteRec(root,value):
    if root is None:
        return root

    if value < root.val:
        root.left = deleteRec(root.left,value)
    elif value > root.val:
        root.right = deleteRec(root.right,value)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = getMinRec(root.right)
        root.val = temp.val
        root.right = deleteRec(root.right,temp.val)

    # handle case of 1 node having no parent
    if root is None:
        return root

    #update height of parent
    root.height = 1 + max(getHeight(root.left),getHeight(root.right))

    #get BF for rotations
    balance = getBalance(root)

    # start to balance tree for 4 cases
    #left left
    if balance > 1 and getBalance(root.left) >= 0:
        return rightRotate(root)
    #right right
    if balance > 1 and getBalance(root.right) <= 0:
        return leftRotate(root)
    #right left
    if balance < -1 and getBalance(root.right) > 0:
        root.right = rightRotate(root.right)
        return leftRotate(root)
    #left right
    if balance > 1 and getBalance(root.left) < 0:
        root.left = leftRotate(root.left)
        return leftRotate(root)

    return root

def printTree(root):
    if root is not None:
        printTree(root.left)
        printTree(root.right)
        print(root.val)

def getRandomArray(n):#return random list of unique values
    lst = []
    while len(lst) < n:
        val = random.randint(1,n)
        if val in lst:
            continue
        lst.append(val)
    return lst

def getSortedArray(n):#return list containing n,n-1....n-n-1
    lst = []
    while n > 0:
        lst.append(n)
        n-=1
    return lst

def getList(lst,root):#helper for sort that inserts elements of tree into a lst
    if root is not None:
        getList(root.left)
        getList(root.right)
        lst.append(root.val)

def sort(root):#sorting elements of bst
    lst = []
    getList(lst,root)
    n = len(lst)
    for i in range(n):
        for j in range(1, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

root = Node(6)
root2 = Node(6)
lst = getRandomArray(10000)
print(lst)
for i in lst:
   insertRecBST(root,Node(i))
for i in lst:
    insertIterBBST(root2,Node(i))
print("Non balanced tree has height of:", getHeight(root))


print("---------")
print("balanced tree has height of:" , getHeight(root2))

