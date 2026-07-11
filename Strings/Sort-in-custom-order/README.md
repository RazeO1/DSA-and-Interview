# Sort First `k` Characters Using a Custom Alphabet Order

## Problem Overview

Normally, the English alphabet follows the order:

```text
abcdefghijklmnopqrstuvwxyz
```

However, this problem introduces a **custom alphabet order** instead:

```text
abcdefghstuvwxyzijklmnopqr
```

Given:

* A string `s`
* An integer `k`

Your task is to:

1. Take only the **first `k` characters** of the string.
2. Sort those characters according to the **custom alphabet order**.
3. Leave the remaining characters unchanged.
4. Output the final string.

---

# First Principles

Instead of immediately thinking about sorting algorithms, let's understand **what the problem is actually asking**.

A sorting algorithm only needs one thing:

> A way to decide which character should come before another.

In the normal alphabet:

```text
a < b < c < d < ...
```

In this problem, the ordering is different:

```text
a < b < c < d < e < f < g < h < s < t < u < ...
```

So before sorting, we need a way to know the **priority** of every character.

---

# Step 1 — Create an Order Mapping

Store the custom alphabet in a string:

```python
custom_order = "abcdefghstuvwxyzijklmnopqr"
```

Now assign every character an index.

Example:

```text
a → 0
b → 1
c → 2
...
h → 7
s → 8
t → 9
...
r → 25
```

This allows us to instantly determine which character comes first.

Implementation:

```python
order_map = {char: index for index, char in enumerate(custom_order)}
```

---

# Step 2 — Separate the String

Only the first `k` characters need to be sorted.

Example:

```text
String = "zyxabcdef"
k = 4

First Part : "zyxa"
Remaining  : "bcdef"
```

Python:

```python
to_sort = list(s[:k])
the_rest = s[k:]
```

---

# Step 3 — Sort Using the Custom Order

Python's `sort()` allows a **key function**.

Instead of comparing characters directly, compare their position in the custom alphabet.

```python
to_sort.sort(key=lambda ch: order_map[ch])
```

For example:

```text
Letters:

z
a
s

Ranks:

17
0
8

Sorted by rank:

a
s
z
```

---

# Step 4 — Rebuild the String

After sorting:

```text
Sorted Part + Remaining Part
```

Python:

```python
result = "".join(to_sort) + the_rest
```

Print the answer.

---

# Complete Algorithm

1. Read the input.
2. Store the custom alphabet.
3. Create a character → index mapping.
4. Extract the first `k` characters.
5. Sort them using the mapping.
6. Append the untouched remainder.
7. Print the final string.

---

# Complexity Analysis

Let `k` be the number of characters being sorted.

### Time Complexity

Creating the mapping:

```text
O(26)
```

Sorting:

```text
O(k log k)
```

Joining strings:

```text
O(n)
```

Overall:

```text
O(k log k)
```

Since the alphabet size is fixed (26 letters), building the mapping is effectively constant time.

---

# Reference Implementation

```python
import sys

def solve():
    input_data = sys.stdin.read().splitlines()

    if not input_data:
        return

    s = input_data[0].strip()
    k = int(input_data[1].strip())

    custom_order = "abcdefghstuvwxyzijklmnopqr"

    order_map = {
        char: index
        for index, char in enumerate(custom_order)
    }

    to_sort = list(s[:k])
    the_rest = s[k:]

    to_sort.sort(key=lambda ch: order_map[ch])

    result = "".join(to_sort) + the_rest

    print(result)

if __name__ == "__main__":
    solve()
```

---

# Key Takeaways

* The challenge is **not** implementing a new sorting algorithm.
* The important part is defining **how characters should be compared**.
* By assigning every character a rank in the custom alphabet, Python's built-in `sort()` can handle the ordering automatically.
* Only the first `k` characters are modified; the remainder of the string stays exactly as it was.

This makes the solution simple, readable, and efficient.
