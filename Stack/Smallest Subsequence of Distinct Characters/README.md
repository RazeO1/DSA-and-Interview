# 1081. Smallest Subsequence of Distinct Characters

## Problem Statement

Given a string `s`, return the **lexicographically smallest subsequence** of `s` that contains **all the distinct characters** of `s` **exactly once**.

> **Note:** This problem is identical to **LeetCode 316 – Remove Duplicate Letters**.

### Example 1

```text
Input:  s = "bcabc"
Output: "abc"
```

### Example 2

```text
Input:  s = "cbacdcbc"
Output: "acdb"
```

---

# Approach

This problem can be solved efficiently using a **Greedy Algorithm** combined with a **Monotonic Stack**.

The idea is to build the answer character by character while ensuring:

* Every distinct character appears exactly once.
* The resulting subsequence is lexicographically smallest.

---

# Intuition

Suppose we are building our answer and encounter a new character.

We ask ourselves:

> **Can this new character be placed before the previous one to make the answer smaller?**

For example,

```text
Current Answer : c
Current Letter : b
```

Since

```text
b < c
```

it would be better if `b` appeared first.

However, we can only remove `c` if another `c` exists later in the string.

Therefore, before solving the problem, we first store the **last occurrence** of every character.

---

# Algorithm

1. Store the last occurrence of every character.
2. Maintain:

   * A stack to build the answer.
   * A set to track characters already included.
3. Traverse the string.
4. If the current character is already in the answer, skip it.
5. Otherwise:

   * While the stack is not empty,
   * The current character is smaller than the stack's top,
   * And the stack's top appears again later,
     remove the stack's top.
6. Push the current character into the stack.
7. Join the stack to obtain the final answer.

---

# Dry Run

### Input

```text
cbacdcbc
```

Last occurrence table:

| Character | Last Index |
| --------- | ---------: |
| c         |          7 |
| b         |          6 |
| a         |          2 |
| d         |          4 |

### Step-by-Step

| Character | Stack | Action                   |
| --------- | ----- | ------------------------ |
| c         | c     | Push                     |
| b         | b     | Pop `c`, Push `b`        |
| a         | a     | Pop `b`, Push `a`        |
| c         | ac    | Push                     |
| d         | acd   | Push                     |
| c         | acd   | Skip (already present)   |
| b         | acdb  | Cannot pop `d`, Push `b` |
| c         | acdb  | Skip                     |

### Final Answer

```text
acdb
```

---

# Correctness

The algorithm maintains three important properties throughout execution:

* Every character appears **at most once**.
* Larger characters are removed only when they appear again later.
* Smaller characters are placed as early as possible.

Because of these properties, the constructed subsequence is guaranteed to be the **lexicographically smallest** valid answer.

---

# Python Solution

```python
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # Store last occurrence of every character
        last = {c: i for i, c in enumerate(s)}

        stack = []
        seen = set()

        for i, c in enumerate(s):

            # Ignore duplicates
            if c in seen:
                continue

            # Maintain lexicographical order
            while (
                stack
                and stack[-1] > c
                and last[stack[-1]] > i
            ):
                seen.remove(stack.pop())

            stack.append(c)
            seen.add(c)

        return "".join(stack)
```

---

# Complexity Analysis

### Time Complexity

**O(n)**

Each character is pushed onto the stack at most once and popped at most once.

### Space Complexity

**O(k)**

Where `k` is the number of distinct characters.

For lowercase English letters:

```text
k ≤ 26
```

so the auxiliary space is effectively constant.

---

# Why This Approach Works

The stack always stores the best subsequence built so far.

Whenever a smaller character is encountered, larger characters are removed **only if they appear again later**. This guarantees that:

* No required character is lost.
* The final subsequence remains valid.
* The resulting answer is the smallest possible in lexicographical order.

---

# Key Takeaways

* Greedy algorithms make the locally optimal choice at each step.
* A monotonic stack helps maintain the smallest possible ordering.
* Tracking the last occurrence allows us to safely remove characters that can be added back later.
* Each character is processed only a constant number of times, resulting in an efficient **O(n)** solution.

---

## Tags

* Greedy
* Monotonic Stack
* Stack
* Hash Table
* String
