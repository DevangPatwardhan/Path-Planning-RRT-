import numpy as np
import matplotlib.pyplot as plt
import random

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.parent = None
        self.cost = 0.0

def generate_random_binary_map(width, height, num_obstacles, min_obstacle_size, max_obstacle_size):
    binary_map = np.zeros((width, height), dtype=int)
    
    def generate_obstacle(binary_map):
        size = random.randint(min_obstacle_size, max_obstacle_size)
        x = random.randint(0, width - size)
        y = random.randint(0, height - size)
        binary_map[x:x+size, y:y+size] = 1
        
    for _ in range(num_obstacles):
        generate_obstacle(binary_map)
    
    return binary_map

def visualize_map(map, start, goal, path):
    plt.figure(figsize=(8, 8))
    plt.imshow(map, cmap='Greys', origin='lower')
    
    plt.plot(start[0], start[1], 'go', markersize=10, label='Start')
    plt.plot(goal[0], goal[1], 'ro', markersize=10, label='Goal')
    
    if path:
        path_x = [node.x for node in path]
        path_y = [node.y for node in path]
        plt.plot(path_x, path_y, color='b', label='Optimal Path')
    
    plt.legend()
    plt.title('Random 2D Binary Map with Start and Goal Points')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()
