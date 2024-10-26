from item import Item
from solution import Solution

import random

max_iterations = 20
budget = 1000
menu_item_count = 20
meal_count = 10

menu = []

# randomly generate menu items
for count in range(menu_item_count):
    menu.append( Item("Combo Meal-{}".format(count+1), random.randint(80, 150)) )

# items can be arranged by price
menu.sort(key=lambda x: x.price, reverse=True)

for item in menu:
    print(item)

print("############################")

# create initial state
initial_state = []
# random
# for count in range( random.randint(6, 10)):

# specific set of meals
for count in range(meal_count):
    initial_state.append( menu[random.randint(0, len(menu)-1)] )

current_sol = Solution(initial_state)
print("Cost of initial solution: {}".format(current_sol.cost()))
 
for item in current_sol.items:
    print(item)

for iteration in range(max_iterations):
    if current_sol.cost() < budget:
        print("############################")
        print("Objective reached at iteration: {}".format(iteration))
        break

    # arrange the current solution items in decreasing order
    current_sol.items.sort(key=lambda x: x.price, reverse=True)

    # get neighborhood values
    item_index = current_sol.getItemByPrice( menu, current_sol.items[0].price )
    print("Meal to be replaced: {}".format(menu[item_index]))
    # update the highest value with 2 random values
    # make sure the new indexes are not out of bounds
    neighbor_1 = menu[item_index-1]
    
    if item_index == len(current_sol.items):      
        neighbor_2 = menu[item_index-2]
    else:
        neighbor_2 = menu[item_index+1]

    
    print("Neighbor 1: {}".format(neighbor_1))
    print("Neighbor 2: {}".format(neighbor_2))

    # select the solution which agrees with the objective function
    best_neighbor = 0
    # minimizing the value, looking for the smallest value
    if neighbor_1.price < neighbor_2.price:
        best_neighbor = neighbor_1
    else:
        best_neighbor = neighbor_2

    # print(best_neighbor)
    new_solution = Solution(current_sol.items.copy())
    new_solution.items[0] = best_neighbor

    # check the new solution if it is good
    if new_solution.cost() < current_sol.cost():
        current_sol.items[0] = best_neighbor
    else:
        print("############################")
        # no improvements, break the loop
        print("No improvements found on iteration: {}".format(iteration))
        break

    if iteration == max_iterations-1:
        print("Maximum iteration reached!")

print("############################")
print("Found solution has a cost of: {}".format(current_sol.cost()))
print("Final solution list: ")
for item in current_sol.items:
    print(item)