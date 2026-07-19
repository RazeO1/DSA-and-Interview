# 20. Valid Parentheses

## Problem Statement

Given a string `s` containing only the characters:

```text id="6a6u89"
'(', ')', '{', '}', '[' and ']'
```

Determine whether the string is **valid**.

A string is valid if:

* Every opening bracket has a corresponding closing bracket of the same type.
* Brackets are closed in the correct order.
* Every closing bracket has a matching opening bracket.

---

## Examples

### Example 1

```text id="g6q8gq"
Input:  s = "()"
Output: true
```

### Example 2

```text id="qmxn4h"
Input:  s = "()[]{}"
Output: true
```

### Example 3

```text id="cv6uuz"
Input:  s = "(]"
Output: false
```

### Example 4

```text id="hnxjve"
Input:  s = "([])"
Output: true
```

### Example 5

```text id="fbgxgm"
Input:  s = "([)]"
Output: false
```

---

# Approach

This problem is a classic application of the **Stack** data structure.

Since the **last opening bracket must always be the first one to close**, the problem follows the **Last-In, First-Out (LIFO)** principle, making a stack the perfect choice.

We also use a hash map to quickly determine which opening bracket corresponds to each closing bracket.

---

# Intuition

Whenever we encounter an opening bracket:

```text id="5gf3j7"
(
[
{
```

we push it onto the stack.

Whenever we encounter a closing bracket:

```text id="mklslg"
)
]
}
```

we check whether it matches the most recently opened bracket (the top of the stack).

If:

* The stack is empty, or
* The brackets do not match,

then the string is invalid.

After processing the entire string, the stack must be empty.

---

# Algorithm

1. Create a hash map of matching brackets.
2. Initialize an empty stack.
3. Traverse the string character by character.
4. If the current character is an opening bracket, push it onto the stack.
5. Otherwise:

   * If the stack is empty, return `False`.
   * Pop the top element.
   * If it does not match the expected opening bracket, return `False`.
6. After traversal, return `True` only if the stack is empty.

---

# Dry Run

### Input

```text id="q17ut5"
s = "([])"
```

| Character | Stack | Action  |
| --------- | ----- | ------- |
| (         | (     | Push    |
| [         | ( [   | Push    |
| ]         | (     | Pop `[` |
| )         | Empty | Pop `(` |

Final Result:

```text id="9t18cp"
True
```

---

### Another Example

Input:

```text id="lby93m"
s = "([)]"
```

| Character | Stack | Action                               |
| --------- | ----- | ------------------------------------ |
| (         | (     | Push                                 |
| [         | ( [   | Push                                 |
| )         | ( [   | Expected `(` but found `[` → Invalid |

Final Result:

```text id="p8m6kl"
False
```

---

# Correctness

The algorithm maintains the following invariant:

* The stack always contains unmatched opening brackets.
* Every closing bracket must match the most recent unmatched opening bracket.
* If a mismatch occurs, the string cannot be valid.
* If the stack is empty after processing the entire string, every opening bracket has been matched correctly.

Thus, the algorithm correctly determines whether the given parentheses sequence is valid.

---

# Python Solution

```python id="p9zmb7"
class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = []

        for ch in s:
            if ch not in pairs:
                stack.append(ch)
            else:
                if not stack:
                    return False

                if stack.pop() != pairs[ch]:
                    return False

        return not stack
```

---

# Complexity Analysis

### Time Complexity

**O(n)**

Each character is pushed onto the stack at most once and popped at most once.

---

### Space Complexity

**O(n)**

In the worst case, the stack stores all opening brackets.

Example:

```text id="n5myy6"
((((((((
```

---

# Why This Approach Works

The stack always keeps track of the opening brackets that are waiting to be matched.

Whenever a closing bracket is encountered:

* It must match the most recently opened bracket.
* If it doesn't, the string is immediately invalid.
* Successfully matched brackets are removed from the stack.

After processing every character, an empty stack guarantees that every opening bracket has been matched exactly once and in the correct order.

---

# Key Takeaways

* Stack is the ideal data structure for matching parentheses.
* Bracket matching follows the **Last-In, First-Out (LIFO)** principle.
* A hash map allows constant-time lookup of matching bracket pairs.
* Every character is processed only once, resulting in an efficient **O(n)** solution.

---

## Tags

* Stack
* String
* Hash Table
