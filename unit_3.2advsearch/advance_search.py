from search_node import SearchNode
from search_agent import SearchAgent
from search_node_grid import SearchNodeGrid

# Initialize the Node Tree
# each row represents the level of the tree, 0 -> first level, n-1 -> last level

node_tree = { 
    'A': SearchNode('A', ['B', 'C']),
    'B': SearchNode('B', ['D', 'E']),
    'C': SearchNode('C', ['F']),
    'D': SearchNode('D', []),
    'E': SearchNode('E', ['F']),
    'F': SearchNode('F', []),
}

# Initialize the agent
my_agent = SearchAgent('F')

# Execute the search
# for loop here is not viable since we are not going through each nodes by index 
# my_agent.searchDFS('A', node_tree)
# my_agent.searchDFS2('A', node_tree)
# my_agent.searchBFS('A', node_tree)


# Search Algorithms that calculates cost to find the goal node, or best path to the node
# modified the children nodes to be a list of tuples
# first value represents the neighbor node
# second value represnts the 
node_tree = { 
    'A': SearchNode('A', [('B', 10), ('C', 15)]),
    'B': SearchNode('B', [('D', 9), ('E', 11)]),
    'C': SearchNode('C', [('F', 20)]),
    'D': SearchNode('D', []),
    'E': SearchNode('E', [('F', 16)]),
    'F': SearchNode('F', []),
}

# might lead to infinite loop
# my_agent.searchBest('A', node_tree)

# Create another instance of 
another_agent = SearchAgent('E')
# another_agent.searchBest('A', node_tree)
# another_agent.searchBest2('A', node_tree)

# Applying A* search

# create a 2D map
grid_map = [
    [SearchNodeGrid('A1', False), SearchNodeGrid('A2', False), SearchNodeGrid('A3', False), SearchNodeGrid('A4', False), SearchNodeGrid('A5', False), SearchNodeGrid('A6', False)],
    [SearchNodeGrid('B1', False), SearchNodeGrid('B2', True), SearchNodeGrid('B3', True), SearchNodeGrid('B4', True), SearchNodeGrid('B5', True), SearchNodeGrid('B6', False)],
    [SearchNodeGrid('C1', False), SearchNodeGrid('C2', True), SearchNodeGrid('C3', True), SearchNodeGrid('C4', True), SearchNodeGrid('C5', True), SearchNodeGrid('C6', False)],
    [SearchNodeGrid('D1', False), SearchNodeGrid('D2', False), SearchNodeGrid('D3', False), SearchNodeGrid('D4', False), SearchNodeGrid('D5', False), SearchNodeGrid('D6', False)],
    [SearchNodeGrid('E1', False), SearchNodeGrid('E2', True), SearchNodeGrid('E3', True), SearchNodeGrid('E4', True), SearchNodeGrid('E5', True), SearchNodeGrid('E6', False)],
    [SearchNodeGrid('F1', False), SearchNodeGrid('F2', False), SearchNodeGrid('F3', False), SearchNodeGrid('F4', False), SearchNodeGrid('F5', False), SearchNodeGrid('F6', False)],
]

grid_agent = SearchAgent((3, 5))
grid_agent.searchAStar((3,0), grid_map)