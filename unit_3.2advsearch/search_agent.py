class SearchAgent:
    # Some algorithms may or may not use this property

    def __init__(self, goal_node):
        # set the goal
        self.goal_node = goal_node
        # ambot lang
        self.cost = 0

    # current refers to the initial/current node the agent is in
    #  tree refers to the node tree/map
    def searchBFS(self, current, tree):
        # nodes that are connected, to be explored by the agent
        fringe = []
        path = []
        fringe.append(current)

        while(len(fringe) != 0):
            print("Agent is currently at {}".format(current))

            if(self.isGoal(current)):
                print('Goal node found')
                return current 
            # append the explored nodes to the frontier
            fringe.extend( tree[current].children )
            # remove the first item, since it is the current node where the agent is
            fringe = fringe[1:]
            # update the current node
            current = fringe[0]
            print('New frontier: {}'.format(fringe))

    # END searchBFS

    # agent performs DFS
    # uses recursion to go deep within the children nodes
    def searchDFS(self, current, tree):
        explored = []
        explored.append(current)

        print("Currently in node {}".format(current))

        for neighbor in tree[current].children:
            if neighbor not in explored:
                if self.isGoal(neighbor):
                    # double check
                    return
                else: 
                    self.searchDFS(neighbor, tree)
    # END searchDFS

    # Check the goal
    def isGoal(self, node):
        if(node == self.goal_node):
            print("Goal node found!")
        return node == self.goal_node
    