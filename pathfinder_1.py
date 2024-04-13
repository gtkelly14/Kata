'''
Path Finder Kata
'''
import sys
import random

def path_finder(check_maze):
    '''
    Path Finder #1: can you reach the exit?

    Arguments:
        maze -- the maze to solve

    Returns:
        True for Solved, False for unsolved

    '''
    # Set Start Location
    check_x = 0
    check_y = 0
    solved = False
    unsolvable = False
    direction_looking = "S"
    
    while not solved and not unsolvable:
        # First check path in straight Line
        



    solved = False
    test_maze = check_maze.splitlines()

    # Start the search at the top left corner of the maze
    solved = check_path((0, 0), 'E', test_maze)
    if not solved:
        check_path((0, 0), 'S', test_maze)

    return solved


def check_path(current_postion, direction_of_travel, maze):
    '''
    Check position and recursively check all directions

    Arguments:
        current_postion -- Where we are when checking this path
        direction_of_travel -- which direction we were traveling

    Returns:
        True if we can reach the end, false if we cannot.
    '''

    check_x = current_postion[0]
    check_y = current_postion[1]
    check_directions = []

    print(f"Taveling {direction_of_travel} from {check_x}, {check_y}")

    if direction_of_travel == 'N':
        check_x -= 1
        check_directions = ['E', 'N', 'W']
        direction_of_travel = 'S'
    elif direction_of_travel == 'E':
        check_y += 1
        check_directions = ['E', 'N', 'S']
        direction_of_travel = 'W'
    elif direction_of_travel == 'S':
        check_x += 1
        check_directions = ['E', 'S', 'W']
        direction_of_travel = 'N'
    elif direction_of_travel == 'W':
        check_directions = ['W', 'S', 'N']
        check_y -= 1
        direction_of_travel = 'E'

    if check_y < 0 or check_y > len(maze) -1 or check_x < 0 or check_x > len(maze) -1:
        print("Out of bounds")
        return False

    if maze[check_x][check_y] == 'W':
        print("Wall")
        return False

    if check_x == len(maze)-1 and check_y == len(maze) -1:
        print ("Solved!")
        return True
    
    random.shuffle(check_directions)
    for direction in check_directions:
        print(f"Checking {direction}")
        if check_path((check_x, check_y), direction, maze) is True:
            return True

    print("Dead End")
    return False


if __name__ == "__main__":

    sys.setrecursionlimit(1000000)

    TARGET_MAZE = "\n".join([
        ".W...",
        ".W...",
        ".W.W.",
        "...W.",
        "...W."])
    # test.assert_equals(path_finder(a), True)
    print(path_finder(TARGET_MAZE))

    TARGET_MAZE = "\n".join([
        ".W...",
        ".W...",
        ".W.W.",
        "...WW",
        "...W."])
    # test.assert_equals(path_finder(a), False)

    TARGET_MAZE = "\n".join([
        "..W",
        ".W.",
        "W.."])
    # test.assert_equals(path_finder(a), False)
    # print(path_finder(TARGET_MAZE))

    TARGET_MAZE = "\n".join([
        ".WWWW",
        ".W...",
        ".W.W.",
        ".W.W.",
        "...W."])
    # test.assert_equals(path_finder(a), True)

    TARGET_MAZE = "\n".join([
        ".W...",
        "W....",
        ".....",
        ".....",
        "....."])
    # test.assert_equals(path_finder(a), False)

    TARGET_MAZE = "\n".join([
        ".W",
        "W."])
    # test.assert_equals(path_finder(a), False)
