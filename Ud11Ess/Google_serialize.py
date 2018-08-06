""""
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.
For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""

class Node(object):
    def __init__(self,val=None,left=None,right=None):
        self.val = val
        self.right = right
        self.left = left
    
def serialize(node):
    if not node:
        return '#'
    return node.val+ " "+serialize(node.left) + " "+ serialize(node.right)

"""
The deserialize function uses closure to be able to iterate through the list inside the recursive calls
vals represent a iterative list of values in the passed string.
"""
def deserialize(data):
    vals = iter(data.split())

    def helper():
        val = next(vals)
        if val=='#':
            return None
        node = Node(val)
        node.left = helper()
        node.right = helper()
        return node

    return helper()

    
    
root = Node('root')
root.left = Node('left')
root.right = Node('right')
root.left.left = Node('left.left')

print(deserialize(serialize(root)).left.left.val)




