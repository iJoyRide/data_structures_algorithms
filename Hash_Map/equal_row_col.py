from collections import defaultdict

def equalPairs(grid):
    
    row_counts = defaultdict(int)
    print(row_counts)
    count = 0
    
    for row in grid:
        row_counts[tuple(row)] += 1
        print(tuple(row))
        print(f"row count: {row_counts[tuple(row)]}")
    
    print("\n")
    
    for column in zip(*grid):
        print(column)
        count += row_counts[column]
        print(f"column count: {row_counts[column]}")
        print(f"Total count:{count}")
        
        
    return count 

if __name__ == "__main__":
    grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
    print(equalPairs(grid))