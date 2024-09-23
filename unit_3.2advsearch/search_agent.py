class SearchAgent:
    # Some algorithms may or may not use this property
    def __init__(self, goal_node):
        # set the goal
        self.goal_node = goal_node
        
    # current refers to the initial/current node the agent is in
    #  tree refers to the node tree/map
    def searchBFS(self, current, tree):
        # nodes that are connected, to be explored by the agent
        fringe = []
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

    def searchDFS(self, current, tree):
        fringe = []
        fringe.append(current)
        while(len(fringe) != 0):
            print("Agent is currently at {}".format(current))

            if(self.isGoal(current)):
                break
            
            # remove the first item, since it is the current node where the agent is
            fringe = fringe[1:]
            # append the explored nodes in front of the frontier
            fringe = tree[current].children + fringe
            # update the current node
            current = fringe[0]
            print('New frontier: {}'.format(fringe))


    # agent performs DFS
    # uses recursion to go deep within the children nodes
    def searchDFS2(self, current, tree):
        explored = []
        explored.append(current)

        print("Currently in node {}".format(current))

        for neighbor in tree[current].children:
            if neighbor not in explored:
                if self.isGoal(neighbor):
                    return
                else: 
                    self.searchDFS2(neighbor, tree)
    # END searchDFS

    # Agent performs best fit search
    def searchBest(self, current, tree):
        # list of nodes that the agent has chosen as th path
        selected_path = []

        # nodes that are connected, to be explored by the agent
        fringe = []
        fringe.append(current)

        while(len(fringe) != 0):
            selected_path.append(current)
            # print("Agent is currently at {}".format(current))

            # instead of appending all of the neighbor nodes
            # select the node with the least cost
            best_cost_node = 0
            for index, item in enumerate(tree[current].children):

                if self.isGoal(item[0]):
                    selected_path.append(item[0])
                    fringe.pop(0)
                    break

                if index == 0:
                    best_cost_node = item[1]
                    current = item[0]
                else:
                    if item[1] < best_cost_node and item[0] not in selected_path:
                        best_cost_node = item[1]
                        current = item[0]
        
            # update the fringe
            fringe.append(current)
            fringe.pop(0)

        print("Best path is: {}".format(selected_path))

    def searchBest2(self, current, tree):
        total_cost = 0
        # list of nodes that the agent has chosen as th path
        selected_path = []

        # nodes that are connected, to be explored by the agent
        fringe = []
        fringe.append(current)
        
        while(len(fringe) != 0):
            selected_path.append(current)
            print("Agent is currently at {}".format(current))

            # instead of appending all of the neighbor nodes
            # select the node with the least cost
            # expand
            # keep track of the best node in the loop
            best_cost_node = 0
            for index, item in enumerate(tree[current].children):

                # calculate the action of the agent
                # if it will choose this node
                action_cost = total_cost + item[1]

                # initialize the value of the best cost node
                if index == 0:
                    best_cost_node = action_cost
                    current = item[0]
                else:
                    if self.isGoal(item[0]):
                        selected_path.append(item[0])
                        fringe.pop(0)
                        break
                    # check if the agent has already chosen the path or not
                    if action_cost < best_cost_node and item[0] not in selected_path:
                        best_cost_node = action_cost
                        current = item[0]
            # Update the total cost after the loop
            total_cost = best_cost_node

            # update the fringe
            fringe.append(current)
            fringe.pop(0)

        print("Best path is: {}".format(selected_path))

    # A Star 
    # uses a heuristic function
    # most likely we will be using a grid map/structure for this type of problem
    # both initial and goal are X-Y coordinates
    # tuple values
    def searchAStar(self, current, node_grid):
        # keep track of the costs done of the agent from the start node

        # keep track of the explored nodes so that it will not traverse back
        explored = []
        # find a way to calculate the heuristic function

        # utilize the idea of fringe to select the next node to explore
        fringe = []
        fringe.append(current)
        while(len(fringe) != 0):
            explored.append(current)
            print("Agent is currently at {}".format(current))
            
            if self.isGoal(current):
                fringe.pop()
                break
            
            else :
                # expand the node and look for possible nodes to add to the fringe
                # since this is a 2D dimensions, we will consider nodes up, down, left and right as adjacent
                node_eval = []

                # Check the adjacent nodes if it is a wall or not
                # up, down, left, right
                neighbors = [(0,-1), (0,1), (-1, 0), (1,0)]

                for neighbor in neighbors:
                    # check if the new position is valid
                    # within the grid space
                    neighbor_pos = (current[0] + neighbor[0], current[1] + neighbor[1])

                    #               X                                   Y 
                    if (0 <= neighbor_pos[0] < len(node_grid)) and (0 <= neighbor_pos[1] < len(node_grid[0])):
                        if (node_grid[neighbor_pos[0]][neighbor_pos[1]].isWall == False) and (neighbor_pos not in explored):
                            node_eval.append( neighbor_pos )

                # print('nodes to be evaluated: {}'.format(node_eval))
                # call the heuristic function to select the node to append to the fringe

                current = self.heuristicFunction(node_eval, len(explored))
                fringe.pop()
                fringe.append(current)

        print("path chosen are: {}".format(explored))

    # Heuristic
    def heuristicFunction(self, nodes, total_action_cost):
        # agent evaluates the nodes and its closeness to the goal
        # evaluate the cost of the agent taken

        # use manhattan distance
        # absolute_value( x1-x2 ) + absolute_value(y1-y2)

        # consider also the total action taken by the agent
        # refers to as the distance of the agent from the start/initial node
        # score = total action cost from the beginning + distance to the end
        nearest_node = nodes[0]
        for node in nodes:
            near_node_score = total_action_cost + (abs(nearest_node[0]-self.goal_node[0]) + abs(nearest_node[0]-self.goal_node[0]))
            node_score = total_action_cost + abs(node[0]-self.goal_node[0]) + abs(node[0]-self.goal_node[0])
            if node_score <= near_node_score:
                nearest_node = node
        return nearest_node

    # Check the goal
    def isGoal(self, node):
        if(node == self.goal_node):
            print("Goal node found!")
        return node == self.goal_node
    