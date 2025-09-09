import numpy as np


# update/add code below ...

def ways(n):
    result = []
    # nickels can be 0, 1, ..., n//5
    for nickels in range(n // 5 + 1):
        # remaining cents are pennies
        pennies = n - nickels * 5
        result.append((pennies, nickels))
    return len(result), result

'''#Another method using backtracking to find all combinations of coins (Optional variation)
def ways(cents, coin_types=[1, 5]):
    result = []
    def backtrack(remaining, coins, current):
        # Found a valid combination
        if remaining == 0:
            result.append(current)
            return
        # No valid combination
        if remaining < 0 or not coins: 
            return
        coin = coins[0]
        # maximum number of this coin we can use
        max_count = remaining // coin
        for count in range(max_count + 1):
            # maximum number of this coin we can use
            backtrack(remaining - count * coin, coins[1:], current + [(coin, count)])
    
    backtrack(cents, sorted(coin_types, reverse=True), [])
    return len(result), result'''

def lowest_score(names, scores):
    # returns the name with the lowest score
    return names[np.argmin(scores)]

def sort_names(names, scores):
    # indices that would sort scores in descending order
    sorted_indices = np.argsort(scores)[::-1]
    return names[sorted_indices], scores[sorted_indices]