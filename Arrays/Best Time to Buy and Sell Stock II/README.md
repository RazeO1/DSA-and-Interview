# Best Time to Buy and Sell Stock II

## Problem Statement

You are given an integer array `prices` where `prices[i]` represents the price of a stock on the `iᵗʰ` day.

You may complete as many transactions as you like (buy one and sell one share of the stock multiple times). However, you can hold **at most one share** of the stock at any given time.

Return the **maximum profit** you can achieve.

---

## Example

### Input

```text
prices = [7,1,5,3,6,4]
```

### Output

```text
7
```

### Explanation

* Buy on Day 2 at price **1**, sell on Day 3 at price **5** → Profit = **4**
* Buy on Day 4 at price **3**, sell on Day 5 at price **6** → Profit = **3**

**Total Profit = 4 + 3 = 7**

---

# Approach

## Greedy Strategy

The key observation is that **every positive increase in stock price contributes to the maximum profit**.

Instead of trying to identify every local minimum and maximum, we simply add the profit whenever today's price is higher than yesterday's.

For every pair of consecutive days:

* If the price increases, add the difference to the total profit.
* If the price decreases, ignore it.

This works because any continuous increase can be broken into multiple smaller profitable transactions without changing the overall profit.

For example:

```text
1 → 2 → 3 → 5

Profit = (2-1) + (3-2) + (5-3)
       = 1 + 1 + 2
       = 4

which is equal to

5 - 1 = 4
```

Thus, summing every positive day-to-day increase always produces the maximum possible profit.

---

# Algorithm

1. Initialize `profit = 0`.
2. Traverse the array from the second day.
3. Compute the difference between the current day's price and the previous day's price.
4. If the difference is positive, add it to `profit`.
5. Return the accumulated profit.

---

# Dry Run

**Input**

```text
prices = [7,1,5,3,6,4]
```

| Previous | Current | Difference | Profit |
| -------: | ------: | ---------: | -----: |
|        7 |       1 |         -6 |      0 |
|        1 |       5 |         +4 |      4 |
|        5 |       3 |         -2 |      4 |
|        3 |       6 |         +3 |      7 |
|        6 |       4 |         -2 |      7 |

**Final Answer**

```text
7
```

---

# Complexity Analysis

* **Time Complexity:** `O(n)`
  Each element is visited exactly once.

* **Space Complexity:** `O(1)`
  Only a single variable is used to store the accumulated profit.

---

# Key Takeaways

* This is a **Greedy Algorithm**.
* Every profitable day-to-day increase contributes to the final answer.
* Summing all positive differences is mathematically equivalent to buying at the start of each increasing sequence and selling at its end.
* The solution is optimal with **O(n)** time and **O(1)** space complexity.
