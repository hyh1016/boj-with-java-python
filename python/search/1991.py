import sys
input = sys.stdin.readline


def preorder(tree, node):
    print(node, end='')
    if tree[node][0] != '.':
        preorder(tree, tree[node][0])
    if tree[node][1] != '.':
        preorder(tree, tree[node][1])


def inorder(tree, node):
    if tree[node][0] != '.':
        inorder(tree, tree[node][0])
    print(node, end='')
    if tree[node][1] != '.':
        inorder(tree, tree[node][1])


def postorder(tree, node):
    if tree[node][0] != '.':
        postorder(tree, tree[node][0])
    if tree[node][1] != '.':
        postorder(tree, tree[node][1])
    print(node, end='')


n = int(input())
tree = {}
for i in range(n):
    parent, left, right = input().split()
    tree[parent] = (left, right)
preorder(tree, 'A')
print()
inorder(tree, 'A')
print()
postorder(tree, 'A')
print()
