class Node(object):
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right


def pre_order_traversal(node):
    if node:
        print(node.value,end=" ")
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)
    
def in_order_traversal(node):
    if node:
        pre_order_traversal(node.left)
        print(node.value,end=" ")
        pre_order_traversal(node.right)

def post_order_traversal(node):
    if node:
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)
        print(node.value,end=" ")
    

a=Node('A')
b=Node('B')
c=Node('C')
d=Node('D')
e=Node('E')
f=Node('F')
g=Node('G')
h=Node('H')
i=Node('I')
j=Node('J')
k=Node('K')
l=Node('L')
m=Node('M')
n=Node('N')
o=Node('O')
p=Node('P')

a.left=b
a.right=k

b.left=c
b.right=h

k.left=l
k.right=o

c.left=d
c.right=g

h.left=i
h.right=j

l.left=m
l.right=n

d.left=e
d.right=f

pre_order_traversal(a)
print("")
in_order_traversal(a)
print("")
post_order_traversal(a)
