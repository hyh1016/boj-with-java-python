import sys
input = sys.stdin.readline
sys.setrecursionlimit(15000)


def get_postorder(preorder, inorder, postorder):
    if len(preorder) == 0:
        return
    root = preorder[0]
    index = inorder.index(root)
    left_inorder = inorder[:index]
    right_inorder = inorder[index+1:]
    left_preorder = preorder[1:len(left_inorder)+1]
    right_preorder = preorder[len(left_inorder)+1:]
    get_postorder(left_preorder, left_inorder, postorder)
    get_postorder(right_preorder, right_inorder, postorder)
    postorder.append(root)


for i in range(int(input())):
    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    postorder = []
    get_postorder(preorder, inorder, postorder)
    print(' '.join(map(str, postorder)))
