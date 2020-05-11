class Node():
    def __init__(self,value):
        self.right = None
        self.left = None
        self.val = value

def insertRec(root,node):
    if root is None:
        return node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                root.right = insertRec(root.right,node)
        else:
            if root.left is None:
                root.left = node
            else:
                root.left = insertRec(root.left,node)
    return root

def insertIter(root,node):
    if root is None:
        root = node
    else:
        while root is not None:
            if root.val > node.val:
                if root.left is None:
                    root.left = node
                    return node
                else:
                    root = root.left
            else:
                if root.right is None:
                    root.right = node
                    return node
                else:
                    root = root.right
    return root

def findMinRec(root):#guarenteed to be in left subtree
    if root.left is None:
        return root
    return findMinRec(root.left)

def findMinIter(root):
    while root.left is not None:
        root = root.left
    return root.val

def findMaxRec(root):#guarenteed to be in right subtree
    if root.right is None:
        return root
    return findMaxRec(root.right)

def findMaxIter(root):
    while root.right is not None:
        root = root.right
    return root.val

def deleteRec(root,value):
    #if tree is empty return None
    if root is None:
        return root
    #determine is key is smaller or larger than root
    if value < root.val:
        root.left = deleteRec(root.left,value)
    elif value > root.val:
        root.right = deleteRec(root.right,value)
    #if we get here then root.val = value and work to delete node
    else:
        #case1 - only one child exists
        if root.left is None:
            temp = root.right
            root = None
            return temp
        if root.right is None:
            temp = root.left
            root = None
            return temp
        #case2 - 2 children exist - find min of right subtree so it remains a BST
        temp = findMinRec(root.right)
        root.val = temp.val
        root.right = deleteRec(root.right,temp.val)
    return root

def deleteIter(root,value):
    if root is None:
        return root
    while root is not None:
        #check if value is on right side
        if root.val < value:
            root = root.right
        #check if value is smaller
        elif root.val > value:
            root = root.left
        #root.val is equal to value
        else:
            #case1 - 1 child exists
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            else:
                #case2 - 2 children exist to find min of right subtree to replace parent
                temp = findMinIter(root.right)
                root.val = temp
    return root


def printTree(root):
    if root is not None:
        printTree(root.left)
        print(root.val)
        printTree(root.right)

def getSortedArray(n):
    lst = 0
    while n > 0:
        lst.append(n)
        n-=1
    return lst

first = Node(10)
lst = list(range(1,100))
for i in lst:
    insertIter(first,Node(i))
printTree(first)
deleteRec(first,37)
print("-------")
printTree(first)
print("-------")
print(findMaxIter(first))







