def solve(nums):
    goal = len(nums) - 1

    for i in range(len(nums) - 2, -1, -1):
        max_reach = i + nums[i]

        if max_reach >= goal:
            goal = i

    print(goal == 0)

if __name__ == "__main__":
    nums = list(map(int, input().split()))
    solve(nums)
