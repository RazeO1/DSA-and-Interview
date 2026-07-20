# 🔄 Shift 2D Grid

## 📌 Problem Statement

Given an `m × n` 2D grid and an integer `k`, shift every element in the grid `k` times.

During one shift:

* Each element moves one position to the **right**.
* The last element of each row moves to the **first column of the next row**.
* The bottom-right element wraps around to the **top-left corner**.

Return the grid after performing all `k` shifts.

---

## 💡 Approach

Instead of simulating each shift individually, treat the 2D grid as a **virtual 1D array**.

### Key Idea

For a grid with:

* `rows = m`
* `cols = n`

Every cell `(row, col)` corresponds to a unique 1D index:

```text
index = row × cols + col
```

After shifting by `k` positions:

```text
new_index = (index + k) % (rows × cols)
```

Finally, convert the new 1D index back into 2D coordinates:

```text
new_row = new_index // cols
new_col = new_index % cols
```

This allows each element to be moved directly to its final position in a single traversal.

---

## 🧠 Algorithm

1. Compute the total number of elements.
2. Reduce `k` using modulo (`k %= total`) to avoid unnecessary rotations.
3. Create an empty grid of the same dimensions.
4. Traverse every element in the original grid.
5. Convert its `(row, col)` position to a 1D index.
6. Compute its shifted index.
7. Convert the shifted index back to `(row, col)`.
8. Place the element in the new grid.
9. Return the shifted grid.

---

## ✅ Python Solution

```python
from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        size = rows * cols
        k %= size

        shifted = [[0] * cols for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                current = row * cols + col
                target = (current + k) % size

                shifted[target // cols][target % cols] = grid[row][col]

        return shifted
```

---

## 📖 Example

### Input

```text
grid =
[
 [1,2,3],
 [4,5,6],
 [7,8,9]
]

k = 1
```

### Mapping

| Value | Old Index | New Index |
| ----: | --------: | --------: |
|     1 |         0 |         1 |
|     2 |         1 |         2 |
|     3 |         2 |         3 |
|     4 |         3 |         4 |
|     5 |         4 |         5 |
|     6 |         5 |         6 |
|     7 |         6 |         7 |
|     8 |         7 |         8 |
|     9 |         8 |         0 |

### Output

```text
[
 [9,1,2],
 [3,4,5],
 [6,7,8]
]
```

---

## ⏱️ Complexity Analysis

| Complexity | Value        |
| ---------- | ------------ |
| **Time**   | **O(m × n)** |
| **Space**  | **O(m × n)** |

* Every element is processed exactly once.
* The additional grid stores the shifted result.

---

## 🎯 Why This Approach?

* Avoids simulating `k` individual shifts.
* Uses direct index mapping for optimal performance.
* Simple mathematical transformation between 2D and 1D indices.
* Clean, efficient, and interview-friendly solution.

---

## 🔑 Key Takeaways

* A 2D grid can often be treated as a virtual 1D array.
* Converting between 2D coordinates and a 1D index simplifies many matrix problems.
* Using modulo (`%`) naturally handles wrap-around behavior.
* Thinking in terms of index transformations often leads to optimal solutions.
