# 🔢 Prefix GCD Pair Sum

> **Difficulty:** Medium
> **Topics:** `Math` • `Array` • `Sorting` • `Greatest Common Divisor (GCD)`

---

# 📝 Problem Statement

Given an integer array `nums` of length `n`, construct a new array `prefixGcd` such that for every index `i`:

* Let `maxi` be the maximum value among `nums[0...i]`.
* `prefixGcd[i] = gcd(nums[i], maxi)`.

After constructing `prefixGcd`:

1. Sort it in non-decreasing order.
2. Pair the smallest element with the largest element.
3. Continue pairing inward until no more pairs can be formed.
4. Compute the **GCD** of every pair.
5. If the array length is odd, ignore the middle element.

Return the **sum of the GCDs** of all formed pairs.

---

# 💡 Intuition

The problem naturally breaks into three independent phases:

### 1️⃣ Build the Prefix GCD Array

Maintain the maximum value seen so far.

For every element:

```text
prefixGcd[i] = gcd(nums[i], currentMaximum)
```

---

### 2️⃣ Sort the Array

Sorting arranges the values so that pairing can be performed exactly as required.

---

### 3️⃣ Pair Smallest with Largest

After sorting:

```text
smallest  ↔  largest
2nd small ↔ 2nd large
...
```

For every pair:

```text
answer += gcd(leftElement, rightElement)
```

Since the pairing order is fixed by the problem statement, there is no optimization or greedy decision to make—just simulate the required process.

---

# 🚀 Approach

### Step 1

Traverse the array while maintaining the running maximum.

Convert each element into:

```text
gcd(currentElement, runningMaximum)
```

This transforms the original array into the required `prefixGcd` array.

---

### Step 2

Sort the transformed array.

---

### Step 3

Use two pointers:

* Left pointer starts from the beginning.
* Right pointer starts from the end.

For each pair:

```text
answer += gcd(nums[left], nums[right])
```

Move both pointers inward until they cross.

---

# 📊 Dry Run

### Input

```text
nums = [3, 6, 2, 8]
```

### Build Prefix GCD

| Index | Running Max | gcd |
| ----: | ----------: | --: |
|     0 |           3 |   3 |
|     1 |           6 |   6 |
|     2 |           6 |   2 |
|     3 |           8 |   8 |

```text
prefixGcd = [3, 6, 2, 8]
```

---

### Sort

```text
[2, 3, 6, 8]
```

---

### Pair Elements

```text
gcd(2, 8) = 2

gcd(3, 6) = 3
```

Total:

```text
2 + 3 = 5
```

---

# ⏱️ Complexity Analysis

| Operation        | Complexity |
| ---------------- | ---------: |
| Build Prefix GCD |       O(n) |
| Sorting          | O(n log n) |
| Pairing          |       O(n) |

### Overall Time Complexity

```text
O(n log n)
```

### Space Complexity

```text
O(1)
```

> The transformation is performed **in-place** (excluding the internal memory used by Python's sorting algorithm).

---

# 🎯 Key Observations

* Maintain only a single running maximum while traversing the array.
* The original array can be reused to store the `prefixGcd` values.
* Sorting enables direct pairing from both ends.
* The pairing order is fixed, so no greedy strategy or dynamic programming is required.
* A two-pointer approach keeps the implementation simple and efficient.

---

# 🌟 Interview Takeaways

* Efficient use of a running maximum.
* In-place transformation to minimize extra memory.
* Clean two-pointer traversal after sorting.
* Optimal overall complexity of **O(n log n)**.

This solution is concise, easy to explain in interviews, and scales efficiently to the maximum input constraints.
