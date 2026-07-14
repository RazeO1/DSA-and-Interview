class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

def build_tree(arr):
    if not arr or arr[0] == -1:
        return None
    
    nodes = [TreeNode(x) if x != -1 else None for x in arr]

    for i in range(len(arr)):
        if nodes[i] is not None:
            left_index = 2 * i + 1
            right_index = 2 * i + 2

            if left_index < len(arr):
                nodes[i].left = nodes[left_index]
            if right_index < len(arr):
                nodes[i].right = nodes[right_index]

    return nodes[0]

def maxDepth(root):
    if root is None:
        return 0
    
    leftDepth = maxDepth(root.left)
    rightDepth = maxDepth(root.right)

    return max(leftDepth, rightDepth) + 1

def solve():
    raw = input().split()
    arr = [None if x == "None" else int(x) for x in raw]
    
    root = build_tree(arr)
    depth = maxDepth(root)
    print(depth)

if __name__ == "__main__":
    solve()