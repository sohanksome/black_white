import maze
import generate_maze
import sys
import random


BIT_SOLUTION = 0b0000010010010110
# Solve maze using Pre-Order DFS algorithm, terminate with solution

def is_goal(mazes, current_cell):
    return current_cell[0] == mazes.total_cells-1

def dfs_recursive(mazes, current_cell):
    """
    current_cell: 現在的節點
    mazes.cell_neighbors(current_cell): 
        回傳一個串列，裡面是每個current_cell還沒走過的新節點

    mazes.visit_cell(current_cell, new_cell):
        讓new_cell這個節點被標記為走過了
    
    mazes.refresh_maze_view():
        更新畫面
    """
    if not is_goal(mazes, current_cell):
    # 如果還沒走到終點
        for new_cell in mazes.cell_neighbors(current_cell): # new_cell: 可以走的新節點
            # 如果有可以走的路要做什麼?
            # START YOUR CODE #
            mazes.visit_cell(current_cell, new_cell)         # 1. 要讓節點標示為走過
            mazes.refresh_maze_view()        # 2. 更新迷宮畫面
            if dfs_recursive(mazes, new_cell):   # 3. DFS 新的點 (填入"__fill_in__")
            # END YOUR CODE #
                return True
            else:                                           # 如果還沒走到終點
                mazes.backtrack(current_cell)
                mazes.refresh_maze_view()
                
        mazes.backtrack(current_cell)
        mazes.refresh_maze_view()
        return False
    else:
        print("Goal!")
        return True

def solve_dfs(mazes):
    current_cell = (0, 'RIGHT')
    try:
        dfs_recursive(mazes, current_cell)
    except:
        print('你寫錯了!')
    mazes.state = 'idle'


# Solve maze using BFS algorithm, terminate with solution
def solve_bfs(mazes):
    """
    create a queue
    set current cell to 0
    set in direction to 0b0000
    set visited cells to 0
    enqueue (current cell, in direction)

    while current cell not goal and queue not empty
        dequeue to current cell, in direction
        visit current cell with bfs_visit_cell
        add 1 to visited cells
        call refresh_maze_view to update visualization

        get unvisited neighbors of current cell using cell_neighbors, add to queue

    trace solution path and update cells with solution data using reconstruct_solution

    set state to 'idle'
    """
    queue = []
    cur_cell = 0
    in_direction = 0b0000
    visited_cells = 0
    queue.insert(0, (cur_cell, in_direction))
    while not cur_cell == len(mazes.maze_array) - 1 and len(queue) > 0:
        cur_cell, in_direction = queue.pop()
        mazes.bfs_visit_cell(cur_cell, in_direction)
        visited_cells += 1
        mazes.refresh_maze_view()
        neighbors = mazes.cell_neighbors(cur_cell)
        for neighbor in neighbors:
            queue.insert(0, neighbor)
    mazes.reconstruct_solution(cur_cell)
    mazes.state = "idle"

def print_solution_array(mazes):
    solution = mazes.solution_array()
    print('Solution ({} steps): {}'.format(len(solution), solution))


def main(solver='dfs'):
    current_maze = maze.Maze('create')
    generate_maze.create_dfs(current_maze)
    if solver == 'dfs':
        solve_dfs(current_maze)
    elif solver == 'bfs':
        solve_bfs(current_maze)
    while 1:
        maze.check_for_exit()
    return

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()
