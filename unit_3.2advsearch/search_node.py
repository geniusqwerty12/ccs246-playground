class SearchNode:
    # Initialize Node
    def __init__(self, name, children):
        self.name = name
    # this list will hold the keys that refers to the neighboring nodes connected to it
        self.children = children
    # No other methods attached here