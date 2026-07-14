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
    
    
def hasPathSum(root, targetSum):
    
    if not root:
        return False
        
    if not root.left and not root.right:
        return root.val == targetSum
        
    remaining = targetSum - root.val
    
    return(
        hasPathSum(root.left, remaining) or
        hasPathSum(root.right, remaining)
        )
        
        
def solve():
    raw = input().split()
    
    arr = [None if x == "None" else int(x) for x in raw]
    
    target = int(input())
    
    root = build_tree(arr)
    ans = hasPathSum(root, target)
    print(ans)
    
if __name__ == "__main__":
    solve()
    
    