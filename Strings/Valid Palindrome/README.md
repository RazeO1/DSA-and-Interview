# 🔄 Valid Palindrome

## 🔗 Problem Statement

A phrase is considered a **palindrome** if, after:

* Converting all uppercase letters to lowercase.
* Removing all non-alphanumeric characters.

it reads the same forward and backward.

Given a string `s`, return:

* `true` if it is a palindrome.
* `false` otherwise.

---

## 📝 Examples

### Example 1

**Input**

```text
"A man, a plan, a canal: Panama"
```

**Output**

```text
true
```

**Explanation**

After removing non-alphanumeric characters and converting to lowercase:

```text
amanaplanacanalpanama
```

It reads the same from left to right and right to left.

---

### Example 2

**Input**

```text
"race a car"
```

**Output**

```text
false
```

---

### Example 3

**Input**

```text
" "
```

**Output**

```text
true
```

---

## 💡 Intuition

A palindrome reads the same from both ends.

Instead of creating a new cleaned string, we can use **two pointers**:

* One pointer starts from the beginning.
* The other starts from the end.
* Skip all non-alphanumeric characters.
* Compare the remaining characters after converting them to lowercase.
* If any pair doesn't match, the string is **not** a palindrome.
* If all pairs match, it **is** a palindrome.

This avoids creating extra strings and uses constant extra space.

---

## 🚀 Approach

1. Initialize two pointers:

   * `left = 0`
   * `right = len(s) - 1`
2. Move the left pointer until it points to an alphanumeric character.
3. Move the right pointer until it points to an alphanumeric character.
4. Compare both characters (after converting to lowercase).
5. If they are different, return `False`.
6. Otherwise, move both pointers inward.
7. Continue until the pointers meet.
8. If no mismatch is found, return `True`.

---

## 🔍 Dry Run

### Input

```text
"A man, a plan, a canal: Panama"
```

### Step 1

```
Left  → A
Right → a
```

Compare

```
a == a ✅
```

Move both pointers.

---

### Step 2

```
Left → ' '
```

Space is ignored.

Move left pointer.

```
Left → m
```

Similarly,

```
Right → ':'
```

Skip punctuation until

```
Right → m
```

Compare

```
m == m ✅
```

Continue moving inward.

---

### Remaining Comparisons

```
a == a ✅
n == n ✅
a == a ✅
p == p ✅
...
```

Every comparison matches.

Return

```text
True
```

---

## 🎯 Two Pointer Visualization

```
A man, a plan, a canal: Panama

L                               R
↓                               ↓
A                               a
✔

Move inward

  L                         R
  ↓                         ↓
  m                         m
  ✔

Move inward

      L                 R
      ↓                 ↓
      a                 a
      ✔

Continue until both pointers meet.
```

---

## 📊 Complexity Analysis

### Time Complexity

Each character is visited at most once.

**Time:** `O(n)`

where `n` is the length of the string.

---

### Space Complexity

No extra string or array is created.

**Space:** `O(1)`

---

## 🆚 Comparison with Filtering Approach

### Filtering Approach

```python
cleaned = "".join(c.lower() for c in s if c.isalnum())
return cleaned == cleaned[::-1]
```

* Time: **O(n)**
* Space: **O(n)**

---

### Two Pointer Approach (Current Solution)

* Time: **O(n)**
* Space: **O(1)** ✅

The two-pointer solution is more memory-efficient and is the preferred approach in coding interviews.

---

## 🎯 Key Takeaways

* Use **two pointers** to compare characters from both ends.
* Skip spaces and punctuation using `isalnum()`.
* Convert characters to lowercase before comparison.
* Avoid creating additional strings for better space efficiency.
* This is the standard optimal solution for the Valid Palindrome problem.

---

## 📚 Concepts Practiced

* Two Pointers
* String Traversal
* Character Manipulation
* Case Conversion
* In-Place Comparison
* Time & Space Optimization
