import random
import time


# Set the dimensions of the grid
GRID_WIDTH = 60
GRID_HEIGHT = 30


def initialize_grid():
    grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
    pattern_choice = input("Enter 'manual' to enter a pattern manually or 'file' to load from a file: ")

    if pattern_choice.lower() == 'manual':
        print("Enter the initial pattern (use 0 for dead cells and 1 for live cells):")
        pattern_height = int(input("Enter the height of the pattern: "))
        pattern_width = int(input("Enter the width of the pattern: "))
        start_row = GRID_HEIGHT // 2 - pattern_height // 2
        start_col = GRID_WIDTH // 2 - pattern_width // 2
        for i in range(pattern_height):
            row = input(f"Enter row {i + 1}: ")
            for j in range(pattern_width):
                grid[start_row + i][start_col + j] = int(row[j])

    elif pattern_choice.lower() == 'file':
        with open('patterns.txt', 'r') as file:
            patterns = file.read().split('\n\n')  # Split patterns by empty lines

        pattern_choice = input("Enter the pattern number (1, 2, 3, ...): ")
        if 1 <= int(pattern_choice) <= len(patterns):
            pattern_lines = patterns[int(pattern_choice) - 1].split('\n')
            pattern_height = len(pattern_lines)
            pattern_width = len(pattern_lines[0])
            start_row = GRID_HEIGHT // 2 - pattern_height // 2
            start_col = GRID_WIDTH // 2 - pattern_width // 2
            for i in range(pattern_height):
                row = pattern_lines[i]
                for j in range(pattern_width):
                    grid[start_row + i][start_col + j] = 1 if row[j] == '#' else 0
        else:
            print("Invalid pattern number.")

    else:
        print("Invalid choice. Using an empty grid.")

    return grid


def count_neighbors(grid, row, col):
    neighbors = 0
    for i in range(max(0, row - 1), min(GRID_HEIGHT, row + 2)):
        for j in range(max(0, col - 1), min(GRID_WIDTH, col + 2)):
            if i != row or j != col:
                neighbors += grid[i][j]
    return neighbors



def update_grid(grid):
    new_grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
    for i in range(GRID_HEIGHT):
        for j in range(GRID_WIDTH):
            neighbors = count_neighbors(grid, i, j)
            if grid[i][j] == 1:
                if neighbors < 2 or neighbors > 3:
                    new_grid[i][j] = 0
                else:
                    new_grid[i][j] = 1
            else:
                if neighbors == 3:
                    new_grid[i][j] = 1
    return new_grid

# Print the grid
def print_grid(grid):
    for row in grid:
        print(''.join(['\033[92m#\033[0m' if cell else '\033[37m.\033[0m' for cell in row]))
