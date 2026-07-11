import sys

def solve():
    s = input().strip()
    k = int(input())

    order = "abcdefghstuvwxyzijklmnopqr"

    # Count frequency of each letter
    freq = {}
    for ch in s[:k]:
        freq[ch] = freq.get(ch, 0) + 1

    ans = ""

    # Build the sorted prefix
    for ch in order:
        ans += ch * freq.get(ch, 0)

    # Append the remaining string
    ans += s[k:]

    print(ans)

solve()