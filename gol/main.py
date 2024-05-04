import time
import os
from grid import initialize_grid, print_grid, update_grid

def main():
    grid = initialize_grid()
    print_grid(grid)

    while True:
        grid = update_grid(grid)
        os.system("cls")
        print("\033[H\033[J", end="") 
        print_grid(grid)
        time.sleep(0.1)


if __name__ == "__main__":
    main()