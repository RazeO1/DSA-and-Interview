class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


def build_tree(arr):
    if not arr or arr[0] == -1:
        return None

    nodes = [TreeNode(x) if x != -1 else None for x in arr]

    for i in range(len(arr)):
        if nodes[i]:
            left = 2 * i + 1
            right = 2 * i + 2

            if left < len(arr):
                nodes[i].left = nodes[left]

            if right < len(arr):
                nodes[i].right = nodes[right]

    return nodes[0]


def max_difference(root):
    ans = float("-inf")

    def dfs(node, max_ancestor):
        nonlocal ans

        if not node:
            return

        ans = max(ans, max_ancestor - node.val)
        max_ancestor = max(max_ancestor, node.val)

        dfs(node.left, max_ancestor)
        dfs(node.right, max_ancestor)

    dfs(root, root.val)
    return ans


def solve():
    # Height is part of the input format but not used
    height = int(input())

    # Read tree in level-order
    arr = list(map(int, input().split()))

    # Empty tree
    if arr == [-1]:
        print(-1)
        return

    # Single node
    if sum(x != -1 for x in arr) == 1:
        print(0)
        return

    root = build_tree(arr)
    print(max_difference(root))


if __name__ == "__main__":
    solve()