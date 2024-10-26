from item import Item
from solution import Solution

import random

budget = 500

menu = []

# randomly generate menu items
for count in range(30):
    menu.append( Item("Combo Meal-{}".format(count+1), random.randint(50, 200)) )
# print(menu)

# create initial state
initial_state = []
# random
for count in range( random.randint(6, 10)):
    initial_state.append( menu[random.randint(0, len(menu)-1)] )

current_sol = Solution(initial_state)
print("Cost of initial solution: {}".format(current_sol.cost()))

# Objective function 1
# Minimize the spending of items, not getting over the given budget

iter_count = 0

while current_sol.cost() > budget:
    # update the current solution

    # choosing what item to replace
        # either it will pick the same item
        # or you can exclude other items

    # Replacing a random item from the menu to a random index  
    # Sometimes finds a solution
    # otherwise is stuck in a loop
    # current_sol.items[random.randint(0, len(current_sol.items)-1)] = menu[ random.randint(0, len(menu)-1) ]

    # sort the items
    current_sol.items.sort(key=lambda x: x.price, reverse=True)
    # replace the highest with a random item
    current_sol.items[0] = menu[ random.randint(0, len(menu)-1) ] 

    iter_count+= 1
print("Number of iterations: {}".format(iter_count))
print("Found solution has a cost of: {}".format(current_sol.cost()))

# Objective function 2
# Maximize the number of items within the given budget
# Only N items must be present
max_items = 7
print("Length of current solution is: {}".format(len(current_sol.items)))

while current_sol.cost() > budget or len(current_sol.items) != max_items:

    if len(current_sol.items) < max_items:
        # add item
        current_sol.items.append( menu[random.randint(0, len(menu)-1)] )
    elif len(current_sol.items) > max_items:
        # remove item, maybe the item with the highest value
        current_sol.items.remove( current_sol.items[random.randint(0, len(current_sol.items)-1)] )
    else:
        # since the number of items is reached, time to change the items
        current_sol.items[random.randint(0, len(current_sol.items)-1)] = menu[ random.randint(0, len(menu)-1) ]

        # current_sol.items.sort(key=lambda x: x.price, reverse=True)
        # current_sol.items[0] = menu[ random.randint(0, len(menu)-1) ] 
    iter_count += 1

print("Number of iterations: {}".format(iter_count))
print("Found solution has a cost of: {}".format(current_sol.cost()))