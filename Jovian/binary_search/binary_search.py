from jovian.pythondsa import evaluate_test_case

tests = [
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