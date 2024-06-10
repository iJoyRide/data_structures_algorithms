def totalCost(costs, k, candidates):
        
    sorted_costs = sorted(costs)
    
    # Summing up the k smallest costs
    total_cost = sum(sorted_costs[:k])
    
    return total_cost

if __name__ == "__main__":
    k = 3
    costs = [17, 12, 10, 2, 7, 2, 11, 20, 8]
    candidates = 3
    
    print(totalCost(costs, k, candidates))
