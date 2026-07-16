from math import gcd

def gcdSum(nums):
    maxi, n = 0, len(nums)

    for i in range(n):
        maxi = max(maxi, nums[i])
        nums[i] = gcd(nums[i], maxi)

    nums.sort()

    print(sum(gcd(nums[i], nums[~i]) for i in range(n // 2)))

def solve():
    nums = list(map(int, input().split()))
    gcdSum(nums)

if __name__ == "__main__":
    solve()