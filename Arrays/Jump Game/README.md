# Jump Game

## Problem Statement

You are given an integer array `nums`, where each element represents your **maximum jump length** from that position.

Starting from the first index, determine whether it is possible to reach the last index.

Return:

* `true` if you can reach the last index.
* `false` otherwise.

---

## Example 1

### Input

```text
nums = [2,3,1,1,4]
```

### Output

```text
true
```

### Explanation

* Start at index `0` (jump length = `2`).
* Jump to index `1`.
* From index `1` (jump length = `3`), jump directly to the last index.

---

## Example 2

### Input

```text
nums = [3,2,1,0,4]
```

### Output

```text
false
```

### Explanation

No matter which path is chosen, you will eventually reach index `3`, whose maximum jump length is `0`. Since you cannot move any further, reaching the last index is impossible.

---

# Approach

## Greedy Strategy (Working Backwards)

Instead of asking:

> **"Can I reach the end from the current index?"**

we reverse the thinking:

> **"Which indices can reach the end?"**

Initially, the **last index** is our goal because it can obviously reach itself.

We then iterate from **right to left**.

For every index:

* If the current index can jump to or beyond the current goal, it becomes the new goal.
* This means reaching the current index guarantees reaching the end.

If, after processing the entire array, the goal has moved back to index `0`, then the last index is reachable.

---

# Why This Works

Suppose the current goal is index `7`.

If index `5` can jump to index `7` (or beyond), then reaching index `5` automatically guarantees reaching the end.

So instead of remembering every possible path, we only need to maintain the **leftmost index that can reach the destination**.

This greedy observation allows us to solve the problem in a single pass with constant extra space.

---

# Algorithm

1. Set the last index as the initial goal.
2. Traverse the array from right to left.
3. If `i + nums[i] >= goal`, update the goal to `i`.
4. After the traversal, check whether the goal is `0`.
5. Return the result.

---

# Dry Run

### Input

```text
nums = [2,3,1,1,4]
```

| Index | Jump Length | Current Goal |  Can Reach Goal?  | New Goal |
| ----: | ----------: | -----------: | :---------------: | -------: |
|     4 |           4 |            4 |        Yes        |        4 |
|     3 |           1 |            4 | Yes (`3 + 1 = 4`) |        3 |
|     2 |           1 |            3 | Yes (`2 + 1 = 3`) |        2 |
|     1 |           3 |            2 | Yes (`1 + 3 = 4`) |        1 |
|     0 |           2 |            1 | Yes (`0 + 2 = 2`) |        0 |

Since the final goal becomes index `0`, the answer is:

```text
true
```

---

# Complexity Analysis

* **Time Complexity:** `O(n)`

  * Each index is visited exactly once.

* **Space Complexity:** `O(1)`

  * Only one extra variable (`goal`) is used.

---

# Key Takeaways

* This is a **Greedy Algorithm**.
* Working **backwards** simplifies the problem significantly.
* The algorithm maintains the **leftmost index that can reach the end**.
* No recursion, dynamic programming, or extra memory is required.
* The solution is optimal with **O(n)** time and **O(1)** space complexity.

---

## Interview Insight

The key invariant maintained throughout the algorithm is:

> **`goal` always represents the leftmost index currently known to be able to reach the last index.**

Whenever another index can reach this goal, it becomes the new goal. If the goal eventually moves back to index `0`, the last index is reachable from the start.
