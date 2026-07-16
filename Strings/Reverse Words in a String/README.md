# 🔄 Reverse Words in a String

> **Difficulty:** Medium
> **Topics:** `String` • `Two Pointers` • `String Manipulation`

---

# 📝 Problem Statement

Given a string `s`, reverse the order of its words.

A word is defined as a sequence of non-space characters.

The returned string must:

* Contain the words in reverse order.
* Have exactly one space between consecutive words.
* Have no leading or trailing spaces.

---

# 💡 Intuition

The problem consists of two simple tasks:

1. Extract all valid words while ignoring extra spaces.
2. Reverse their order and join them back together.

Python's built-in `split()` function automatically handles:

* Leading spaces
* Trailing spaces
* Multiple spaces between words

making the solution remarkably simple.

---

# 🚀 Approach

### Step 1

Split the string into individual words.

```text
"  hello   world  "

↓

["hello", "world"]
```

Extra spaces are automatically discarded.

---

### Step 2

Reverse the list of words.

```text
["hello", "world"]

↓

["world", "hello"]
```

---

### Step 3

Join the reversed words using a single space.

```text
["world", "hello"]

↓

"world hello"
```

---

# 📊 Dry Run

### Input

```text
s = "a good   example"
```

### Split

```text
["a", "good", "example"]
```

---

### Reverse

```text
["example", "good", "a"]
```

---

### Join

```text
"example good a"
```

---

# ⏱️ Complexity Analysis

| Operation    | Complexity |
| ------------ | ---------: |
| Split String |       O(n) |
| Reverse List |       O(k) |
| Join String  |       O(n) |

Where:

* `n` = length of the string
* `k` = number of words

### Overall Time Complexity

```text
O(n)
```

### Space Complexity

```text
O(n)
```

The list of extracted words requires additional space.

---

# 🎯 Key Observations

* `split()` automatically removes extra spaces.
* No manual parsing is required in Python.
* `join()` guarantees exactly one space between words.
* The solution is concise, readable, and optimal for Python.

---

# 🌟 Interview Takeaways

* Demonstrates knowledge of Python's string utilities.
* Achieves linear time complexity.
* Produces clean, readable code.
* The follow-up asking for **O(1) extra space** applies mainly to languages with mutable strings (such as C++ or Java). Python strings are immutable, so this approach is considered the standard optimal solution in Python.
