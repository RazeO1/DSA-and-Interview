def maxActiveSectionAfterTrade(s: str) -> int:
    zeros = map(len, filter(None, s.split('1')))

    maxZeros = max(map(sum, pairwise(zeros)), default=0)

    return s.count('1') + maxZeros

def solve():
    s = input().strip()
    print(maxActiveSectionAfterTrade(s))

if __name__ == "__main__":
    from itertools import pairwise
    solve()

