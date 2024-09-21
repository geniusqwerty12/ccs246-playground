class SearchNode:
    # Initialize Node
    def __init__(self, name, cost, children):
        self.name = name
        self.cost = cost
    # this list will hold the keys that refers to the 
        self.children = children
    # No other methods attached here