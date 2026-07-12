# Rotate Array

## Problem Statement

Given an integer array `nums`, rotate the array to the **right** by `k` steps, where `k` is non-negative.

The rotation must be performed **in-place**, modifying the original array without creating another array.

---

## Examples

### Example 1

**Input**

```text
nums = [1,2,3,4,5,6,7]
k = 3
```

**Output**

```text
[5,6,7,1,2,3,4]
```

**Explanation**

```text
Rotate 1 step : [7,1,2,3,4,5,6]
Rotate 2 steps: [6,7,1,2,3,4,5]
Rotate 3 steps: [5,6,7,1,2,3,4]
```

---

### Example 2

**Input**

```text
nums = [-1,-100,3,99]
k = 2
```

**Output**

```text
[3,99,-1,-100]
```

---

# Approach

A straightforward solution is to move the last `k` elements to the front using an extra array. However, this requires **O(n)** additional space.

A more efficient approach is to use the **Reverse Algorithm**, which performs the rotation in-place.

The idea is:

1. Reverse the entire array.
2. Reverse the first `k` elements.
3. Reverse the remaining `n-k` elements.

After these three reversals, the array becomes correctly rotated.

---

# Why Does This Work?

Suppose the array consists of two parts:

```text
A | B
```

where

* `A` = first `n-k` elements
* `B` = last `k` elements

Initially:

```text
A B
```

Reverse the entire array:

```text
reverse(B) reverse(A)
```

Reverse the first part:

```text
B reverse(A)
```

Reverse the remaining part:

```text
B A
```

This is exactly the required rotated array.

---

# Algorithm

1. Compute `k %= n` to handle cases where `k` is greater than the array size.
2. Reverse the complete array.
3. Reverse the first `k` elements.
4. Reverse the remaining elements.
5. The array is now rotated in-place.

---

# Dry Run

### Input

```text
nums = [1,2,3,4,5,6,7]
k = 3
```

### Step 1: Reverse Entire Array

```text
[7,6,5,4,3,2,1]
```

### Step 2: Reverse First 3 Elements

```text
[5,6,7,4,3,2,1]
```

### Step 3: Reverse Remaining Elements

```text
[5,6,7,1,2,3,4]
```

Final Answer:

```text
[5,6,7,1,2,3,4]
```

---

# Correctness

The algorithm maintains the following property:

* Reversing the complete array places the last `k` elements at the beginning, but in reverse order.
* Reversing the first `k` elements restores their original order.
* Reversing the remaining elements restores the order of the first `n-k` elements.

Thus, every element ends up in its correct rotated position.

---

# Complexity Analysis

### Time Complexity

* Reverse entire array → **O(n)**
* Reverse first `k` elements → **O(k)**
* Reverse remaining `n-k` elements → **O(n-k)**

Overall Time Complexity:

```text
O(n)
```

---

### Space Complexity

Only a few variables are used, and the array is modified in-place.

```text
O(1)
```

> **Note:** The algorithm itself is an **O(1)** extra-space approach. In Python, slice operations (`nums[:k]` and `nums[k:]`) create temporary slices internally. For a strict O(1) implementation (as expected in some interviews), the same reverse algorithm can be implemented using index-based swaps instead of slicing.

---

# Key Takeaways

* Uses the **Reverse Algorithm** to perform rotation efficiently.
* Solves the problem in **linear time**.
* Modifies the array **in-place**.
* Avoids repeated rotations, making it efficient even for very large values of `k`.
* A classic interview problem that demonstrates in-place array manipulation and the power of reversing.
