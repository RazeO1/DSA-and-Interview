# Path Sum

## Problem Statement

Given the root of a binary tree and an integer `targetSum`, determine whether the tree has a **root-to-leaf** path such that the sum of all node values along the path equals `targetSum`.

A **leaf** is a node that has no left or right child.

---

## Examples

### Example 1

```text
Input:
root = [5,4,8,11,null,13,4,7,2,null,null,null,1]
targetSum = 22

Output:
True
```

**Explanation**

```text
        5
       / \
      4   8
     /   / \
   11   13  4
   / \        \
  7   2        1

Valid Path:
5 → 4 → 11 → 2

Sum = 22
```

---

### Example 2

```text
Input:
root = [1,2,3]
targetSum = 5

Output:
False
```

---

## Approach

This solution uses **Depth First Search (DFS)** with recursion.

Instead of keeping track of the sum collected so far, the algorithm follows a **remaining sum** approach:

1. Start from the root.
2. Subtract the current node's value from the remaining target.
3. Continue recursively to both children.
4. When a leaf node is reached, check whether its value equals the remaining target.
5. If either subtree returns `True`, a valid path exists.

This approach is simple, elegant, and naturally fits recursive tree traversal.

---

## Algorithm

1. If the current node is `None`, return `False`.
2. If the current node is a leaf:

   * Return `True` if `node.val == targetSum`.
   * Otherwise return `False`.
3. Compute the remaining target:

   ```python
   remaining = targetSum - node.val
   ```
4. Recursively search the left and right subtrees.
5. Return:

   ```python
   left_result OR right_result
   ```

---

## Solution

```python
class Solution:
    def hasPathSum(self, root, targetSum):

        if not root:
            return False

        if not root.left and not root.right:
            return root.val == targetSum

        remaining = targetSum - root.val

        return (
            self.hasPathSum(root.left, remaining)
            or
            self.hasPathSum(root.right, remaining)
        )
```

---

## Dry Run

Target Sum = **22**

```text
            5
           / \
          4   8
         /
       11
      /  \
     7    2
```

### Step 1

```text
Need = 22

Visit 5

Remaining = 17
```

### Step 2

```text
Visit 4

Remaining = 13
```

### Step 3

```text
Visit 11

Remaining = 2
```

### Step 4

Left Child

```text
Visit 7

Remaining = -5

Leaf

False
```

Backtrack.

### Step 5

Right Child

```text
Visit 2

Remaining = 0

Leaf

True
```

A valid root-to-leaf path exists.

---

## Complexity Analysis

| Complexity           | Value    |
| -------------------- | -------- |
| **Time Complexity**  | **O(n)** |
| **Space Complexity** | **O(h)** |

Where:

* `n` = Number of nodes in the tree.
* `h` = Height of the tree.

In a balanced tree:

```text
Space = O(log n)
```

In the worst case (skewed tree):

```text
Space = O(n)
```

---

## Why This Works

Each recursive call asks a single question:

> **"Starting from this node, can I complete the remaining required sum before reaching a leaf?"**

If the answer is `True` for either the left or right subtree, then a valid path exists.

This recursive definition makes the implementation concise, easy to reason about, and optimal.

---

## Key Takeaways

* Uses **Depth First Search (DFS)**.
* Applies recursion with the **remaining sum** technique.
* Visits every node at most once.
* Stops immediately when a valid path is found due to Python's **short-circuit `or`**.
* Optimal solution with **O(n)** time complexity.

---

## Tags

`Binary Tree` `DFS` `Recursion` `Tree Traversal` `LeetCode 112` `Interview Preparation`
