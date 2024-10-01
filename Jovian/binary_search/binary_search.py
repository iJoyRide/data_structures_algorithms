from jovian.pythondsa import evaluate_test_case

tests = [
    # {"input": {"cards": [13, 11, 10, 7, 4, 3, 1, 0], "query": 7}, "output": 3},
    # {"input": {"cards": [13, 11, 10, 7, 4, 3, 1, 0], "query": 1}, "output": 6},
    # {"input": {"cards": [4, 2, 1, -1], "query": 4}, "output": 0},
    # {"input": {"cards": [3, -1, -9, -127], "query": -127}, "output": 3},
    # {"input": {"cards": [6], "query": 6}, "output": 0},
    # {"input": {"cards": [9, 7, 5, 2, -9], "query": 4}, "output": -1},
    # {"input": {"cards": [], "query": 7}, "output": -1},
    # {"input": {"cards": [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], "query": 3},"output": 7,},
    {"input": {"cards": list(range(1, 10000000, 1)), "query": 2},"output": 1,},
]

#Binary Search
def binary_locate_card(cards, query):
    lo = 0
    hi = len(cards) - 1
    
    while lo <= hi:
        mid = (lo + hi) // 2
        mid_val = cards[mid]
        
        if mid_val == query:
            return mid
        elif mid_val < query:
            lo = mid +1
        else:
            hi = mid -1
    return -1
        

if __name__ == "__main__":
    for test in tests:
        #evaluate_test_case(linear_locate_card, test)
        evaluate_test_case(binary_locate_card, test)