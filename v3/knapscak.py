value = [120, 100, 60]
weight = [30, 20, 10]
MAX_WEIGHT = 50


def knapsack(n, current_weight):
    if n == 0 or current_weight <= 0:
        return 0

    if weight[n] > current_weight:
        return knapsack(n - 1, current_weight)

    return max(
        value[n] + knapsack(n - 1, MAX_WEIGHT - current_weight),
        knapsack(n - 1, current_weight),
    )


# go top down, Right to left

print(knapsack(len(value) - 1, MAX_WEIGHT))
