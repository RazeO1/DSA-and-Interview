# Product of Array Except Self

## Problem Statement

Given an integer array `nums`, return an array `answer` such that:

* `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.
* You **must not use the division operator**.
* The solution must run in **O(n)** time.

### Example 1

```text
Input:
nums = [1,2,3,4]

Output:
[24,12,8,6]
```

### Example 2

```text
Input:
nums = [-1,1,0,-3,3]

Output:
[0,0,9,0,0]
```

---

# Intuition

For every index `i`, we need:

```text
answer[i] =
(Product of all elements to the left of i)
×
(Product of all elements to the right of i)
```

Instead of recalculating these products for every index (which would take **O(n²)** time), we compute them efficiently using two passes:

1. **Left to Right:** Store the product of all elements before each index (prefix product).
2. **Right to Left:** Maintain a running suffix product and multiply it with the stored prefix product.

This avoids division, naturally handles zeros, and achieves the required **O(n)** time complexity.

---

# Approach

### Step 1: Build Prefix Products

Traverse the array from left to right.

For every index:

* Store the product of all previous elements.
* Update the running prefix product.

Example:

```text
nums = [1,2,3,4]

Prefix Products

Index:      0  1  2  3
Result:     1  1  2  6
```

---

### Step 2: Multiply by Suffix Products

Now traverse from right to left.

Maintain a running suffix product.

For every index:

* Multiply the stored prefix product with the current suffix product.
* Update the suffix product.

Example:

```text
Suffix Traversal

Suffix Products:

Index 3 → 1
Index 2 → 4
Index 1 → 12
Index 0 → 24
```

Final result:

```text
[24,12,8,6]
```

---

# Dry Run

```text
nums = [1,2,3,4]

Initial

result = [1,1,1,1]

---------------------------------
Prefix Pass

prefix = 1

i = 0
result = [1,1,1,1]
prefix = 1

i = 1
result = [1,1,1,1]
prefix = 2

i = 2
result = [1,1,2,1]
prefix = 6

i = 3
result = [1,1,2,6]
prefix = 24

---------------------------------
Suffix Pass

suffix = 1

i = 3
result = [1,1,2,6]
suffix = 4

i = 2
result = [1,1,8,6]
suffix = 12

i = 1
result = [1,12,8,6]
suffix = 24

i = 0
result = [24,12,8,6]

Final Answer

[24,12,8,6]
```

---

# Why This Works

For every index:

```text
answer[i]
=
(Product of all elements before i)
×
(Product of all elements after i)
```

The first pass stores the left product.

The second pass multiplies the right product.

Since each element is visited only twice, the algorithm runs in linear time.

---

# Complexity Analysis

| Complexity  | Value                                   |
| ----------- | --------------------------------------- |
| Time        | **O(n)**                                |
| Extra Space | **O(1)** *(excluding the output array)* |

---

# Key Interview Takeaways

* No division operation is used.
* Handles arrays containing one or multiple zeros naturally.
* Meets the required **O(n)** time complexity.
* Uses only the output array, satisfying the **O(1)** extra space follow-up.
* Clear two-pass approach (prefix + suffix) that is easy to explain during interviews.

---

## Pattern Learned

This problem demonstrates an important interview pattern:

> **Prefix and Suffix Computation**

Instead of recomputing information for every index, precompute values from the left and the right, then combine them to obtain the final answer efficiently.

This pattern frequently appears in array, dynamic programming, and interview problems involving cumulative computations.
