def shiftGrid(grid, k):
    m, n = len(grid), len(grid[0])

    arr = [x for row in grid for x in row]

    k %= len(arr)
    arr = arr[-k:] + arr[:-k]

    return [arr[i : i + n] for  i in range(0, len(arr), n)]

def solve():
    grid = ast.literal_eval(input())
    k = int(input())
    print(shiftGrid(grid, k))

if __name__ == "__main__":
    import ast
    solve()