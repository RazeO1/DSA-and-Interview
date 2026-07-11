# Maximum Difference Between an Ancestor and a Descendant in a Binary Tree

## Problem Statement

Given a binary tree represented in **level-order traversal**, where `-1` denotes a missing node, find the **maximum difference** between an ancestor node and any of its descendants.

For every ancestor-descendant pair, compute:

```text
Difference = Ancestor Value - Descendant Value
```

Return the **maximum** such difference.

### Example

#### Input

```text
3
8 3 10 1 6 -1 14 -1 -1 4 7
```

#### Tree

```text
         8
       /   \
      3     10
     / \      \
    1   6      14
       / \
      4   7
```

#### Output

```text
7
```

**Explanation**

The maximum difference is obtained from the ancestor-descendant pair `(8, 1)`:

```text
8 - 1 = 7
```

---

# First Principles

Instead of comparing every ancestor with every descendant, think about what information is actually needed while traversing the tree.

When moving from the root to any node, the only ancestor that can produce the largest difference is the **largest-valued ancestor encountered so far**.

For example:

```text
        8
       /
      3
     /
    6
```

While visiting node `6`, the ancestors are:

```text
8, 3
```

The only value we need to remember is:

```text
max(8, 3) = 8
```

The difference becomes:

```text
8 - 6 = 2
```

There is no need to store the entire list of ancestors because only the maximum ancestor value affects the answer.

---

# Approach

Perform a Depth-First Search (DFS).

At every node:

1. Compute:

   ```text
   maxAncestor - currentNode
   ```

2. Update the global maximum difference.

3. Update the maximum ancestor value:

   ```text
   maxAncestor = max(maxAncestor, currentNode)
   ```

4. Continue recursively for the left and right subtrees.

Since each node is visited exactly once, the solution is efficient.

---

# Algorithm

1. Build the binary tree from its level-order array representation.
2. Start DFS from the root.
3. Maintain the maximum ancestor value along the current path.
4. Update the answer at every node.
5. Return the maximum difference found.

---

# Complexity Analysis

**Time Complexity**

```text
O(n)
```

Each node is visited exactly once.

**Space Complexity**

```text
O(h)
```

where `h` is the height of the tree due to the recursion stack.

* Best case (balanced tree): `O(log n)`
* Worst case (skewed tree): `O(n)`

---

# Sample Input

```text
3
8 3 10 1 6 -1 14 -1 -1 4 7
```

# Sample Output

```text
7
```

---

# Technologies Used

* Python 3
* Depth-First Search (DFS)
* Binary Trees
* Recursion

---

# Learning Outcomes

This project demonstrates:

* Binary Tree construction from level-order traversal
* Recursive DFS traversal
* Maintaining state during recursion
* Optimizing from a naïve `O(n²)` solution to an `O(n)` solution
* Thinking from first principles by identifying the minimum information required to solve the problem efficiently
