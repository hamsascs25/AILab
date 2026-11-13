
# Hill Climbing Algorithm

def objective(x):
    return -(x - 5) ** 2 + 25


def hill_climbing(start):
    current = start

    while True:
        neighbors = [current - 1, current + 1]

        best_neighbor = max(neighbors, key=objective)

        if objective(best_neighbor) <= objective(current):
            break

        current = best_neighbor

        print("Current State:", current)
        print("Current Value:", objective(current))

    return current


# Main Program
start = int(input("Enter starting point: "))

result = hill_climbing(start)

print("\nBest Solution:", result)
print("Maximum Value:", objective(result))
