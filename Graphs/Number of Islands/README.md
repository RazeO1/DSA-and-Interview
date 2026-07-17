# 🌊 Number of Islands

## 🔗 Problem Statement

Given an `m × n` binary grid `grid`, where:

* `'1'` represents **land**
* `'0'` represents **water**

Return the **number of islands**.

An **island** is formed by connecting adjacent land cells **horizontally** or **vertically**. You may assume all four edges of the grid are surrounded by water.

---

## 📝 Example

### Input

```text
[["1","1","1","1","0"],
 ["1","1","0","1","0"],
 ["1","1","0","0","0"],
 ["0","0","0","0","0"]]
```

### Output

```text
1
```

---

## 💡 Intuition

Think of every `'1'` (land) as a node in a graph.

Whenever we encounter an unvisited land cell:

* We have discovered a **new island**.
* We perform a **Depth-First Search (DFS)** to visit every connected land cell.
* Every visited land cell is marked as `'0'` so it won't be counted again.

By the time DFS finishes, the entire island has been explored.

---

## 🚀 Approach

1. Traverse every cell in the grid.
2. If the current cell is `'1'`:

   * Increment the island count.
   * Start a DFS from that cell.
3. During DFS:

   * Stop if the current position is outside the grid.
   * Stop if the current cell is water (`'0'`) or already visited.
   * Mark the current land cell as visited by changing it to `'0'`.
   * Explore all four directions:

     * Down
     * Up
     * Right
     * Left
4. Continue until every cell has been processed.

---

## 🔍 Dry Run

### Initial Grid

```text
🟩 🟩 🟩 🟩 🌊
🟩 🟩 🌊 🟩 🌊
🟩 🟩 🌊 🌊 🌊
🌊 🌊 🌊 🌊 🌊
```

Start scanning from the top-left.

The first land cell (`0,0`) starts a DFS.

DFS visits every connected land cell and marks it as visited.

### Grid After DFS

```text
🌊 🌊 🌊 🌊 🌊
🌊 🌊 🌊 🌊 🌊
🌊 🌊 🌊 🌊 🌊
🌊 🌊 🌊 🌊 🌊
```

The outer loops continue scanning.

No more land cells are found.

**Number of Islands = 1**

---

## 🌳 DFS Traversal

```text
Start
  │
  ▼
Found Land ('1')
  │
  ▼
Count Island (+1)
  │
  ▼
DFS
 ├── Down
 ├── Up
 ├── Right
 └── Left
  │
  ▼
Mark all connected land as visited ('0')
  │
  ▼
Continue scanning the grid
```

---

## 📊 Complexity Analysis

### Time Complexity

Every cell is visited at most once.

**Time:** `O(m × n)`

---

### Space Complexity

The recursive DFS uses the function call stack.

Worst case (entire grid is land):

**Space:** `O(m × n)`

---

## 💻 VS Code Input Format

The driver program uses:

```python
import ast

grid = ast.literal_eval(input())
```

So you can paste the input exactly as shown on LeetCode.

### Input

```text
[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
```

### Output

```text
1
```

---

## 🎯 Key Takeaways

* A 2D grid can be treated as a **graph**.
* Each island is a **connected component**.
* DFS explores one complete island at a time.
* Marking visited cells in-place eliminates the need for an extra `visited` array.
* Every cell is processed only once, making the solution optimal.

---

## 📚 Concepts Practiced

* Graph Traversal
* Depth-First Search (DFS)
* Flood Fill
* Connected Components
* Matrix Traversal
* Recursion
* Grid-Based Graph Problems
