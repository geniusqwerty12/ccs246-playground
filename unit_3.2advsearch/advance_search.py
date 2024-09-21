from search_node import SearchNode
from search_agent import SearchAgent

# Initialize the Node Tree
# each row represents the level of the tree, 0 -> first level, n-1 -> last level

node_tree = { 
    'A': SearchNode('A', 0, ['B', 'C']),
    'B': SearchNode('B', 0, ['D', 'E']),
    'C': SearchNode('C', 0, ['F']),
    'D': SearchNode('D', 0, []),
    'E': SearchNode('E', 0, ['F']),
    'F': SearchNode('F', 0, []),
}

# Initialize the agent
my_agent = SearchAgent('F')

# Execute the search
# for loop here is not viable since we are not going through each nodes by index 
# my_agent.searchDFS('A', node_tree)
my_agent.searchBFS('A', node_tree)

# Output the optimal Path