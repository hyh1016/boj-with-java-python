import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e9))


def get_postorder(preorder, start, end):
    if start >= end:
        return
    root = preorder[start]
    right_child = end
    for i in range(start+1, end):
        if preorder[i] > root:
            right_child = i
            break
    get_postorder(preorder, start+1, right_child)
    if right_child != end:
        get_postorder(preorder, right_child, end)
    print(root)


preorder = []
while True:
    try:
        preorder.append(int(input()))
    except:
        get_postorder(preorder, 0, len(preorder))
        break
