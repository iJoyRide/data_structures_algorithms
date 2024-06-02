def matrix(grid):
    return list(zip(*grid))


if __name__ == "__main__":
    grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
    print(grid)
    print(matrix(grid))