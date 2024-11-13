# Source code taken from: https://www.geeksforgeeks.org/constraint-satisfaction-problems-csp-in-artificial-intelligence/
from csp import CSP

# Define the Sudoku puzzle as a 9x9 grid
puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 0, 0]]

# Function to display the Sudoku puzzle
def print_sudoku(puzzle):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - ")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            print(puzzle[i][j], end=" ")
        print()

# Print the initial puzzle
print_sudoku(puzzle)



# Variables
variables = [(i, j) for i in range(9) for j in range(9)]
print(variables)

# Domains
Domains = {var: set(range(1, 10)) if puzzle[var[0]][var[1]] == 0 
           else {puzzle[var[0]][var[1]]} for var in variables}
print(Domains)

# Add constraint function
def add_constraint(var):
    constraints[var] = []
    for i in range(9):
        if i != var[0]:
            constraints[var].append((i, var[1]))  # Column constraint
        if i != var[1]:
            constraints[var].append((var[0], i))  # Row constraint
    sub_i, sub_j = var[0] // 3, var[1] // 3
    for i in range(sub_i * 3, (sub_i + 1) * 3):
        for j in range(sub_j * 3, (sub_j + 1) * 3):
            if (i, j) != var:
                constraints[var].append((i, j))  # Subgrid constraint

# Constraints
constraints = {}
for i in range(9):
    for j in range(9):
        add_constraint((i, j))

# Solve the Sudoku puzzle using CSP
print('*'*7, 'Solution', '*'*7)
csp = CSP(variables, Domains, constraints)
sol = csp.solve()

# Format the solution for output
solution = [[0 for i in range(9)] for i in range(9)]
for i, j in sol:
    solution[i][j] = sol[i, j]

# Print the solved Sudoku puzzle
print_sudoku(solution)