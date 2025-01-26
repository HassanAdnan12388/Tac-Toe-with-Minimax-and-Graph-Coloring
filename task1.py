# Importing modules and libraries
from maze_visual import maze, agent
import sys
import argparse
from pprint import pprint
import math
from queue import PriorityQueue
import queue

# Import any other modules you want to use here



# ----------------------------------
ROWS = 20 # Number of rows in the maze
COLS = 20 # Number of columns in the maze
m = maze(ROWS, COLS) # Initialize the maze

# Load the maze from the csv file. You may need to change this path depending on where you save the files.
m.LoadMaze(loadMaze='maze_config.csv', theme="dark")
# ----------------------------------

def dfsGoalPath(start, visited):

    path = [visited.pop()]

    # check each node in visited, starting from goal (which is the last node in visited), for neighbors and choose the first neighbor, while popping all non-neighbors.

   #print(visited)
    while True:

        if path[-1] == (start):
            break
            
        curr = visited.pop()

    # checking if curr node is a neighbor of latest node in path by checking distance of curr node from latest node. if distance is +-1 in either direction, it is a neighbor.
        if (abs(curr[0] - path[-1][0]) == 1 and curr[1] == path[-1][1]) or (abs(curr[1] - path[-1][1]) == 1 and curr[0] == path[-1][0]):
            path.append(curr)

    # reversed path is the correct path from start to goal. ('path' is going from goal to start)
    corrected_path = path[::-1]

    print(corrected_path)

    return corrected_path

def bfs_and_astarGoalPath(predecessors, start, goal):
    path = []
    current = goal

    while current != start:  
        path.append(current)
        current = predecessors.get(current)

    path.append(start) 

    corrected_path = path[::-1]

    return corrected_path


def DFS(maze, start, goal):
    '''
    This function should implement the Depth First Search algorithm.
    The inputs to this function are:
        maze: The maze object
        start: The start position of the agent as a tuple (x,y)
        goal: The goal position of the agent as a tuple (x,y)
    The function should return:
        a list containing all the positions visited by the search algorithm
        a list containing the positions in the final path from the start to the goal
    '''

    visited_positions = []
    path_to_goal = []


    stack = [start] # the stack only keeps track of unvisited nodes

    while True:
        curr = stack.pop()
        visited_positions.append(curr)

        if curr == goal:
            break

    # push in all possible move choices from curr, into stack.
        if maze.maze_map[curr]['E'] == 1:
            pos = list(curr)
            pos[1] += 1
            
            pos = tuple(pos)

            if pos not in visited_positions:
                stack.append(pos)
        
        if maze.maze_map[curr]['S'] == 1:
            pos = list(curr)
            pos[0] += 1
            
            pos = tuple(pos)

            if pos not in visited_positions:
                stack.append(pos)

        if maze.maze_map[curr]['W'] == 1:
            pos = list(curr)
            pos[1] -= 1
            
            pos = tuple(pos)

            if pos not in visited_positions:
                stack.append(pos)

        if maze.maze_map[curr]['N'] == 1:
            pos = list(curr)
            pos[0] -= 1
            
            pos = tuple(pos)

            if pos not in visited_positions:
                stack.append(pos)


    visited_positions_copy = visited_positions.copy()

    path_to_goal = dfsGoalPath(start, visited_positions_copy)
    
    pprint(maze.maze_map)

    return visited_positions, path_to_goal


def BFS(maze, start, goal):
    '''
    This function should implement the Breadth First Search algorithm.
    The inputs to this function are:
        maze: The maze object
        start: The start position of the agent as a tuple (x,y)
        goal: The goal position of the agent as a tuple (x,y)
    The function should return:
        a list containing all the positions visited by the search algorithm
        a list containing the positions in the final path from the start to the goal
    '''

    visited_positions = []
    path_to_goal = []


    q = queue.Queue() # keeps track of unvisited nodes
    predecessor = {start: None}

    q.put(start)

    while True:
        curr = q.get()
        if curr not in visited_positions:
            visited_positions.append(curr)

        if curr == goal:
            break

    # push in all possible move choices from curr, into q.
        if maze.maze_map[curr]['N'] == 1:
            pos = list(curr)
            pos[0] -= 1
            
            pos = tuple(pos)

            if pos not in visited_positions:
                q.put(pos)
                visited_positions.append(pos)
                predecessor[pos] = curr

        if maze.maze_map[curr]['W'] == 1:
            pos = list(curr)
            pos[1] -= 1
            
            pos = tuple(pos)

            if pos not in visited_positions:
                q.put(pos)
                visited_positions.append(pos)
                predecessor[pos] = curr

        if maze.maze_map[curr]['S'] == 1:
            pos = list(curr)
            pos[0] += 1
            
            pos = tuple(pos)

            if pos not in visited_positions:
                q.put(pos)
                visited_positions.append(pos) 
                predecessor[pos] = curr

        if maze.maze_map[curr]['E'] == 1:
            pos = list(curr)
            pos[1] += 1
            
            pos = tuple(pos)

            if pos not in visited_positions:
                q.put(pos)
                visited_positions.append(pos)
                predecessor[pos] = curr

    path_to_goal = bfs_and_astarGoalPath(predecessor, start, goal)

    return visited_positions, path_to_goal



def heuristic(position, goal):
    '''
    This function should implement Euclidean Distance as the heuristic function used in A* algorithm.
    The inputs to this function are:
        position: The current position of the agent as a tuple (x,y)
        goal: The goal position of the agent as a tuple (x,y)
    The function should return:
        the heuristic value of the given position
    '''

    x1, y1 = position
    x2, y2 = goal

    # Calculate Euclidean Distance
    h = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    return h

def AStar(maze, start, goal):
    '''
    This function should implement the A* algorithm.
    The inputs to this function are:
        maze: The maze object
        start: The start position of the agent as a tuple (x,y)
        goal: The goal position of the agent as a tuple (x,y)
    The function should return:
        a list containing all the positions visited by the search algorithm
        a list containing the positions in the final path from the start to the goal
    '''

    # TODO: Implement A* Search algorithm here
    # NOTE: You can assume the cost of moving one step is 1 for this maze
    #       You can use the Euclidean distance as the heuristic function for this assignment
    visited_positions = []
    wasteful =[]
    path_to_goal = []
    custom_order = ['N', 'W', 'S', 'E']
    updated_maze_map = {coordinates: dict((direction, directions[direction]) for direction in sorted(directions, key=lambda direction: custom_order.index(direction))) for coordinates, directions in m.maze_map.items()}
    m.maze_map.update(updated_maze_map)


    pprint(m.maze_map)
    print("_____________________________")
    # coordinates = (20,20)
    coordinates = (20,20) # TESTING 
    cost =0
    f_n_dict = {}
    while (coordinates!=(1,1) and 0 <= coordinates[0] <= 20 and 0 <= coordinates[1] <= 20):
    # for i in range (20):
        pos = m.maze_map[coordinates]
        print("_____________________________")
        print("coordinates :", coordinates)
        print(pos)
        possible_dir = [letter for letter, value in pos.items() if value == 1]
        print(possible_dir)
   
        for direction in possible_dir :
            new_coordinates = magic_coordinates (direction,coordinates)
            h_n = heuristic(new_coordinates, (1,1))
            f_n = 1 + h_n
            if f_n in f_n_dict:
                f_n_dict[f_n].append((coordinates, direction))
            else:
                f_n_dict[f_n] = [(coordinates, direction)]

        print("f_n_dict =", f_n_dict)
    # Print the updated f_n_dict
        max_key = min(f_n_dict.keys())
        max_value = f_n_dict[max_key]
        mazeloster = magic_coordinates(max_value[0][1], max_value[0][0])
        print("MAZELOSTER : ", mazeloster, max_key)
        while mazeloster in visited_positions :
            print("---ERRRO")
            # wasteful.append(coordinates)
            if len(max_value) ==1 :
                del f_n_dict[max_key]
            else:
                f_n_dict[max_key].remove(max_value[0])

            max_key = min(f_n_dict.keys())
            max_value = f_n_dict[max_key]
            mazeloster = magic_coordinates(max_value[0][1], max_value[0][0])
            print("AOUT TO GET STUCK")
            print(f"The f_n  : {max_key}")
        if len(max_value) ==1 :
            next_move = max_value[0]
            print(f"The f_n  : {max_key}")

            print("options tied with this f_n : " ,len(max_value))
            print("cuurent-coordinates: ",next_move[0])
            print("next_direction: ",next_move[1])
            visited_positions.append(coordinates)
            coordinates = magic_coordinates(next_move[1], next_move[0])
            if coordinates in visited_positions:
                wasteful.append(next_move[0])
            del f_n_dict[max_key]
            # print(f_n_dict)

        else:
            next_move = max_value[0]
            print("cuurent-coordinates: ",next_move[0])
            print("next_direction: ",next_move[1])
            visited_positions.append(coordinates)
            coordinates = magic_coordinates(next_move[1], next_move[0])
            if coordinates in visited_positions:
                wasteful.append(next_move[0])
            f_n_dict[max_key].remove(max_value[0])
        cost = cost + 1
        print("COST =", cost)

    # else:
    #     print("draw between directions with the maximum value:")
    #     for direction in max_directions:
    #         print(f"Direction: {direction}, Value: {max_value}")  
        #CHOOSE THE DIRECTION WITH PRIORITY
    print("Error exceeded coordinate limits")
    path_to_goal.extend(visited_positions)

    for i in range(len(visited_positions) - 1):
        coord1 = visited_positions[i]
        coord2 = visited_positions[i + 1]
        if heuristic(coord1, coord2) > 1:
            path_to_goal.remove(coord1)
    
    # total.extend(visited_positions)
    path_to_goal = [item for item in path_to_goal if item not in wasteful]
    return visited_positions, path_to_goal

def magic_coordinates (direction, coordinates):
    if direction == 'W':
        new_coordinates = (coordinates[0], coordinates[1] -1)
        print("West move :",new_coordinates)
    if direction == 'E':
        new_coordinates = (coordinates[0], coordinates[1] +1)
        print("East move :",new_coordinates)
    if direction == 'N':
        new_coordinates = (coordinates[0] - 1, coordinates[1])
        print("North move :",new_coordinates)
    if direction == 'S':
        new_coordinates = (coordinates[0] + 1, coordinates[1])
        print("South move :",new_coordinates)
    return new_coordinates
    
def is_diagonal_move(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    return dx == dy



# -------------------------------------
# This part of the code calls the search algorithms implemented above and displays the results on the maze
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--bfs", help="Run BFS", action="store_true")
    parser.add_argument("-d", "--dfs", help="Run DFS", action="store_true")
    parser.add_argument("-a", "--astar", help="Run A* Search", action="store_true")

    args = parser.parse_args()

    start = (ROWS, COLS)
    goal = (1,1)

    explored, path_to_goal = [], []

    if args.bfs:
        explored, path_to_goal = BFS(m, start, goal)
    elif args.dfs:
        explored, path_to_goal = DFS(m, start, goal)
    elif args.astar:
        explored, path_to_goal = AStar(m, start, goal)
    else:
        print("No search algorithm specified. See help below.")
        parser.print_help()
        sys.exit()

    a = agent(m, ROWS, COLS, filled=True)
    b = agent(m, ROWS, COLS, color="red")

    m.tracePath({a: explored}, delay=20)
    m.tracePath({b: path_to_goal}, delay=20)

    m.run()


if __name__ == "__main__":
    main()











