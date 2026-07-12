def solve(nums):
    write = 0

    for num in nums:
        if write < 2 or num != nums[write - 2]:
            nums[write] = num
            write += 1

    print(write)
    print(nums[:write])

if __name__ == "__main__":
    nums = list(map(int, input().split()))
    solve(nums)