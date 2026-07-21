# 💡 Maximize Active Sections with Trade I

## 📌 Problem Statement

Given a binary string s of length n:

* '1' represents an active section.
* '0' represents an inactive section.

You can perform at most one trade to maximize the number of active sections in s. 

During one trade:

* Convert a contiguous block of '1's that is completely surrounded by '0's to all '0's.
* Afterward, convert a contiguous block of '0's that is completely surrounded by '1's to all '1's.

Note: Treat s as if it is augmented with a '1' at both ends (i.e., 1 + s + 1). These augmented '1's enable edge trades but do not contribute to the final count. Return the maximum number of active sections possible.

---

## 💡 Approach

Instead of manually simulating the string replacements, evaluate the net mathematical result of a trade.

### Key Idea

When you sacrifice a block of '1's (turning them into '0's), you bridge the gap between two adjacent blocks of '0's. This creates one massive, continuous block of '0's. 

During the reward phase, you flip that entire new block into '1's. Because the '1's you originally sacrificed are immediately refunded back to you in this phase, your true net gain is simply:

net_gain = length_of_zero_block_A + length_of_zero_block_B

Therefore, the problem is solved by finding the sizes of all '0' groups, taking the two largest adjacent groups, and adding their lengths to our starting score.

---

## 🧠 Algorithm

1. Count the Baseline: Find the total number of '1's currently in the string. We save this as our starting score.
2. Isolate the Zeros: Split the string at every '1'. This removes the '1's and isolates the chunks of '0's.
3. Clean and Measure: Filter out any empty chunks (caused by consecutive '1's) and map the remaining chunks to their lengths. You now have a list of zero-group sizes.
4. Pair Up Neighbors: Since one trade merges exactly two neighboring groups, look at every pair of adjacent zero groups. 
5. Find the Maximum Gain: Add the lengths of each pair together. The largest sum is your maximum "bonus" from the trade. (If the string is entirely '1's, the bonus defaults to 0).
6. Calculate Final Score: Add this maximum bonus to your baseline '1' count and return the result.

---

## ✅ Python Solution

from itertools import pairwise

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        # Count all existing '1's
        base_ones = s.count("1")
        
        # Get lengths of all contiguous '0' blocks
        zeros = map(len, filter(None, s.split("1")))
        
        # Find the maximum sum of two adjacent '0' blocks
        maxzeros = max(map(sum, pairwise(zeros)), default=0)
        
        # Return total score
        return base_ones + maxzeros

---

## 📖 Example

### Input
s = "01010"

### Mapping
* Original string: "01010"
* Baseline '1' count: 2
* Split by '1': ["0", "0", "0"]
* Zero block lengths: [1, 1, 1]
* Adjacent pairs: (1, 1) and (1, 1)
* Pair sums: 2 and 2
* Max bonus: 2

### Output
4
(Explanation: The 2 baseline '1's + the max bonus of 2 = 4 total active sections)

---

## ⏱️ Complexity Analysis

* Time Complexity: O(n)
* Space Complexity: O(n)

- The string is traversed a constant number of times via count, split, and map.
- The split array and generator results take up additional memory proportional to the length of the string in the worst-case scenario (e.g., alternating "101010").

---

## 🎯 Why This Approach?

* Completely avoids O(n^2) or O(n^3) brute-force string manipulation and simulation.
* Uses Python's highly optimized built-in C-functions (split, count, map).
* Focuses on the core logic (net gain) rather than getting bogged down in state changes.
* Clean, compact, and extremely fast.

---

## 🔑 Key Takeaways

* In game-theory or "trading" algorithms, always look for the net delta instead of simulating the steps literally.
* Sacrificing resources to bridge a gap is a common pattern; recognizing that the sacrifice is refunded simplifies the math completely.
* Python's itertools.pairwise is the perfect tool for sliding windows of size 2.