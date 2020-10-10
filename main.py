#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from node import Node
from ant import Ant
from p1functions import *
import matplotlib.pyplot as plt
  


node_list = [
    [3, 1],
    [5, 1],
    [6, 1],
    [1, 2],
    [2, 2],
    [3, 2],
    [5, 2], 
    [1, 3], 
    [3, 3],
    [4, 3],
    [5, 3], 
    [6, 3],
    [1, 4], 
    [3, 4],
    [6, 4], 
    [1, 5],
    [2, 5],
    [3, 5], 
    [4, 5], 
    [5, 5], 
    [6, 5], 
    [1, 6], 
    [3, 6], 
    [5, 6],
    ]

if __name__ == '__main__':
    nodes = {}
    for nodeCoor in node_list:
        nodes[tuple(nodeCoor)] = Node(tuple(nodeCoor))
    for nodeCoor in nodes:
        for x in range(7):
            for y in range(7):
                if (x, y) != nodeCoor and keyExist(nodes, (x,y)):
                    if (x==nodeCoor[0] and abs(y-nodeCoor[1]) == 1) or (y==nodeCoor[1] and abs(x-nodeCoor[0]) == 1):
                        nodes[nodeCoor].add_connected_node(nodes[(x, y)])
    
    #Edit these variables to edit the maze 
    entrance = nodes[(1, 4)]
    exits = [nodes[(5, 6)], nodes[(6, 1)]]
    mazeSize = [6, 6] #[x, y]
    
    n_ant = 50
    alpha = 1
    rho = 0.1
    initial_pheromone = 0.1
    for nodeCoor in nodes:
        nodes[nodeCoor].set_pheromone(initial_pheromone)
    ants = [Ant() for _ in range(n_ant)]
        
    max_iteration = 200
    percentage_of_dominant_path = 0.9
    iteration = 0
    
    ax = draw_maze(mazeSize, nodes, entrance, exits)
    lines = draw_pheromone(ax, nodes)
    
    while iteration < 200 and get_percentage_of_dominant_path(ants) < percentage_of_dominant_path:
        for ant in ants:
            ant.reset()
            ant.get_path(entrance, exits, alpha)
        
        for node in nodes:
            nodes[node].evaporate_pheromone(rho)
            nodes[node].deposit_pheromone(ants)
            
        iteration += 1
        for l in lines:
            del l
        lines = draw_pheromone(ax, nodes)
        plt.pause(0.05)
        
    paths = []
    pathsCount = []
    for ant in ants:
        if ant.nodes not in paths:
            paths.append(ant.nodes)
            pathsCount.append(1)
        else:
            pathsCount[paths.index(ant.nodes)] += 1
    pathIndex = pathsCount.index(max(pathsCount))
    solution = paths[pathIndex]
    print("Solution = [", end = "")
    for i in range(len(solution)-1):
        print(solution[i].coordinates, end = ", ")
    print(str(solution[-1].coordinates) + "]")
    print("Path Length: " + str(len(solution)))
    print("Iteration: " + str(iteration))

    
            
        
        
        


