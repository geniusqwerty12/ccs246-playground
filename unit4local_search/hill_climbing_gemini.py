# generated by Gemini @ October 22, 2024

import random

def hill_climbing(objective_function, initial_solution, neighborhood_function, max_iterations):
    """
    Implements the local hill climbing search algorithm.

    Args:
        objective_function: The function to be minimized.
        initial_solution: The starting solution.
        neighborhood_function: A function that generates neighboring solutions.
        max_iterations: The maximum number of iterations.

    Returns:
        The optimized solution.
    """

    current_solution = initial_solution
    best_solution = current_solution
    best_value = objective_function(current_solution)

    for i in range(max_iterations):
        neighbors = neighborhood_function(current_solution)
        best_neighbor = None
        best_neighbor_value = float('inf')

        for neighbor in neighbors:
            neighbor_value = objective_function(neighbor)
            if neighbor_value < best_neighbor_value:
                best_neighbor = neighbor
                best_neighbor_value = neighbor_value

        if best_neighbor_value < best_value:
            current_solution = best_neighbor
            best_solution = best_neighbor
            best_value = best_neighbor_value
        else:
            break  # No improvement found, terminate

    return best_solution

# Example usage
def objective_function(x):
    return x**2

def neighborhood_function(x):
    neighbors = []
    for step in [-1, 1]:
        neighbors.append(x + step)
    return neighbors

initial_solution = 5.0
max_iterations = 100

optimized_solution = hill_climbing(objective_function, initial_solution, neighborhood_function, max_iterations)
print("Optimized solution:", optimized_solution)