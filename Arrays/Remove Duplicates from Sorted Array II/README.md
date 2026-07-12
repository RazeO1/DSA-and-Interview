# Remove Duplicates from Sorted Array II

## Problem Statement

Given a sorted integer array `nums`, remove duplicates **in-place** such that each unique element appears **at most twice**.

The relative order of the elements must remain the same, and the operation must be performed using **O(1)** extra space.

Return the number of valid elements `k`, where the first `k` positions of the array contain the final answer.

---

## Examples

### Example 1

**Input**

```text
nums = [1,1,1,2,2,3]
```

**Output**

```text
k = 5
nums = [1,1,2,2,3,_]
```

---

### Example 2

**Input**

```text
nums = [0,0,1,1,1,1,2,3,3]
```

**Output**

```text
k = 7
nums = [0,0,1,1,2,3,3,_,_]
```

---

# Approach

Since the array is already **sorted**, all duplicate elements are consecutive.

We maintain a **write pointer** that indicates the position where the next valid element should be placed.

For each element:

* If fewer than two elements have been written, always keep it.
* Otherwise, compare the current element with the element located **two positions before the write pointer**.

  * If they are different, the current element has appeared fewer than two times, so we keep it.
  * If they are the same, adding it would create a third occurrence, so we skip it.

This allows us to modify the array **in-place** without using any additional data structures.

---

# Algorithm

1. Initialize `write = 0`.
2. Traverse every element in the array.
3. If `write < 2`, copy the element.
4. Otherwise, compare the current element with `nums[write - 2]`.
5. If they are different, copy the element and increment `write`.
6. Return `write`.

---

# Dry Run

### Input

```text
nums = [1,1,1,2,2,3]
```

| Current | Action                    | Result      |
| ------: | ------------------------- | ----------- |
|       1 | Keep                      | [1]         |
|       1 | Keep                      | [1,1]       |
|       1 | Skip (already two copies) | [1,1]       |
|       2 | Keep                      | [1,1,2]     |
|       2 | Keep                      | [1,1,2,2]   |
|       3 | Keep                      | [1,1,2,2,3] |

Returned value:

```text
5
```

Final array:

```text
[1,1,2,2,3]
```

---

# Correctness

The algorithm maintains the following invariant:

* The first `write` elements always contain the correct answer.
* Every value in this prefix appears at most twice.
* Since the array is sorted, comparing the current element with `nums[write - 2]` is sufficient to determine whether adding it would create a third occurrence.

Thus, every valid element is retained, and every extra duplicate is removed.

---

# Complexity Analysis

* **Time Complexity:** `O(n)`

  * The array is traversed exactly once.

* **Space Complexity:** `O(1)`

  * Only a single write pointer is used.

---

# Key Takeaways

* Uses the **Two Pointers** technique.
* Performs the operation **in-place**.
* Requires **constant extra space**.
* Demonstrates how maintaining a write pointer can efficiently solve array modification problems.
