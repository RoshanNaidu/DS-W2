import numpy as np


# update/add code below ...

def ways(n):
    result = [] # list of (pennies, nickels) tuples
    for nickels in range(n // 5 + 1): # nickels can be 0, 1, ..., n//5
        pennies = n - nickels * 5 # remaining cents are pennies
        result.append((pennies, nickels)) # add the combination to the list
    return len(result), result # return number of ways and the list of combinations

def lowest_score(names, scores):
    return names[np.argmin(scores)] # returns the name with the lowest score

def sort_names(names, scores):
    # indices that would sort scores in descending order
    sorted_indices = np.argsort(scores)[::-1]
    # return names list
    return names[sorted_indices]