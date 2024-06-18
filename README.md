# RRT* Path Planning Algorithm

## Overview
This repository contains Python code implementing the **RRT* (Rapidly-exploring Random Tree)** algorithm for path planning in a 2D binary map environment. The algorithm finds an optimal path from a start point to a goal point while avoiding obstacles represented as binary values in the map.

## Files
- **rrt_star.py**: Contains the implementation of the RRT* algorithm.
- **README.md**: Markdown file providing an overview of the project.

## Dependencies
- **numpy**: For numerical operations and array handling.
- **matplotlib**: For visualization of the map and path.

## Usage
To use the code, ensure you have Python installed along with the necessary dependencies (**numpy** and **matplotlib**). You can run the script directly:

    python rrt_star.py

## Code Structure
### Creating and Visualizing Map
- **Node Class (`Node`)**: Represents a node in the RRT* tree, containing position (`x`, `y`), parent node (`parent`), and cost (`cost`).
- **Function (`generate_random_binary_map`)**: Generates a random 2D binary map with obstacles of specified sizes and counts.
- **Function (`visualize_map`)**: Visualizes the generated map with start, goal, and optionally the optimal path.

### RRT* Implementation
- **Node Class (`Node`)**: Same as above.
- **Functions (`rrt_star`, `sample_new_node`, `nearest_neighbor`, `is_collision_free`, `find_path`)**: Implements the RRT* algorithm to find an optimal path from start to goal in the provided map. Uses random sampling, nearest neighbor search, collision checking, and path construction.

### Example Usage
- **Script (`rrt_star.py`)**: Demonstrates the usage of the RRT* algorithm with customizable parameters such as map dimensions, obstacle sizes and counts, start and goal positions, and algorithm constraints.

## Example Usage
```python
if __name__ == '__main__':
    width = 100
    height = 100
    start = (10, 10)
    goal = (90, 90)
    num_obstacles = 15
    min_obstacle_size = 5
    max_obstacle_size = 15
    max_nodes = 1000
    step_size = 5

    binary_map = generate_random_binary_map(width, height, num_obstacles, min_obstacle_size, max_obstacle_size)
    nodes, edges, cost_to_new_node, path = rrt_star(binary_map, start, goal, max_nodes, step_size)

    if path:
        visualize_map(binary_map, start, goal, path)
        print("Path found!")
        for node in path:
            print(f"({node.x}, {node.y})")
    else:
        print("Path not found.")

Notes
Adjust parameters such as width, height, num_obstacles, min_obstacle_size, max_obstacle_size, max_nodes, and step_size to customize the map and algorithm behavior.
Ensure the Python environment includes numpy and matplotlib for proper execution and visualization.
