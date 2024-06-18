import numpy as np
import random

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.parent = None
        self.cost = 0.0

def rrt_star(map, start, goal, max_nodes, step_size):
    nodes = [Node(start[0], start[1])]
    edges = {}
    cost_to_new_node = {nodes[0]: 0.0}

    for _ in range(max_nodes):
        new_node = sample_new_node(goal, map.shape[1], map.shape[0])
        nearest_node = nearest_neighbor(nodes, new_node)
        if not is_collision_free(nearest_node, new_node, map):
            continue

        cost_to_new_node[new_node] = cost_to_new_node[nearest_node] + np.linalg.norm([new_node.x - nearest_node.x, new_node.y - nearest_node.y])
        nodes.append(new_node)
        edges[(new_node.x, new_node.y)] = (nearest_node.x, nearest_node.y)

        if np.linalg.norm([new_node.x - goal[0], new_node.y - goal[1]]) < step_size:
            goal_node = Node(goal[0], goal[1])
            nodes.append(goal_node)
            edges[(goal_node.x, goal_node.y)] = (new_node.x, new_node.y)
            path = find_path(nodes, edges, start, goal)
            return nodes, edges, cost_to_new_node, path

    return nodes, edges, cost_to_new_node, None

def sample_new_node(goal, width, height):
    rand_x = random.uniform(0, width)
    rand_y = random.uniform(0, height)
    return Node(rand_x, rand_y)

def nearest_neighbor(nodes, new_node):
    min_dist = np.inf
    nearest = None
    for node in nodes:
        dist = np.linalg.norm([node.x - new_node.x, node.y - new_node.y])
        if dist < min_dist:
            min_dist = dist
            nearest = node
    return nearest

def is_collision_free(node1, node2, map):
    line = np.linspace([node1.x, node1.y], [node2.x, node2.y], num=100)
    for point in line:
        if map[int(point[1]), int(point[0])] == 1:
            return False
    return True

def find_path(nodes, edges, start, goal):
    path = [Node(goal[0], goal[1])]
    node_key = (goal[0], goal[1])
    while node_key in edges:
        parent_key = edges[node_key]
        path.append(Node(parent_key[0], parent_key[1]))
        node_key = parent_key
    path.append(Node(start[0], start[1]))
    return path[::-1]
