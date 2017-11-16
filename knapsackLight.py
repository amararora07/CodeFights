def knapsackLight(value1, weight1, value2, weight2, maxW):
    if weight1 + weight2 <= maxW:
        return value1 + value2
    if min(weight1, weight2) > maxW:
        return 0
    t=max(weight1, weight2)
    if max(weight1, weight2) <= maxW:
        if weight1 <= t and value1>=value2:
            return value1
        else:
            return value2
    if weight1 <= maxW:
        return value1
    return value2
