def rotate(nums, k):
    n = len(nums)
    k %= n

    nums.reverse()

    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k:])

    print(nums)

if __name__ == "__main__":
    nums = list(map(int, input().split()))
    k = int(input())
    rotate(nums, k)
