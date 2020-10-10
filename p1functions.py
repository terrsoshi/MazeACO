#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def keyExist(dicti, key): 
    if key in dicti.keys(): 
        return True
    else: 
        return False
    
def get_percentage_of_dominant_path(ants):
    paths = []
    pathsCount = []
    for ant in ants:
        if len(ant.nodes) == 0:
            return 0
        if ant.nodes not in paths:
            paths.append(ant.nodes)
            pathsCount.append(1)
        else:
            pathsCount[paths.index(ant.nodes)] += 1
    percentage = max(pathsCount)/sum(pathsCount)
    return percentage  
        
def draw_maze(mazeSize, nodes, entrance, exits):
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.set_title(r"$\bf{" + "Amount\ of\ pheromones\ in\ the\ maze" + "}$" + "\n(More pheromones = thicker red lines)")
    ax.set_xlabel("x-coordinates")
    ax.set_ylabel("y-coordinates")
    ax.set_axisbelow(True)
    red_patch = mpatches.Patch(color='red', label='Pheromones')
    green_patch = mpatches.Patch(color='g', label='Entrance')
    cyan_patch = mpatches.Patch(color='c', label='Exit')
    node_patch = mpatches.Circle(xy=(0,0), color='k', label='Nodes/Paths')
    blocked_node_patch = mpatches.Patch(color='m', label='Blocked Nodes')
    ax.legend(handles = [red_patch, green_patch, cyan_patch, node_patch, blocked_node_patch], bbox_to_anchor = (0.95, 1.05), loc = "upper left")
    nodes_x = [node.coordinates[0] for key, node in nodes.items()]
    nodes_y = [node.coordinates[1] for key, node in nodes.items()]
    ax.scatter(nodes_x, nodes_y, s = 50, color = 'k')
    ax.scatter(entrance.coordinates[0], entrance.coordinates[1], s = 90, marker = ",", color = 'g')
    exits_x = [exitNode.coordinates[0] for exitNode in exits]
    exits_y = [exitNode.coordinates[1] for exitNode in exits]
    ax.scatter(exits_x, exits_y, s = 90, marker = ",", color = 'c')
    blocked_nodes_x = []
    blocked_nodes_y = []
    for x in range (1, mazeSize[0]+1):
        for y in range(1, mazeSize[1]+1):
            if not keyExist(nodes, (x, y)):
                blocked_nodes_x.append(x)
                blocked_nodes_y.append(y)
    ax.scatter(blocked_nodes_x, blocked_nodes_y, s = 50, marker = "^", color = 'm')
    ax.set_aspect(aspect=1.0)
    return ax

def draw_pheromone(ax, nodes):
    lines = []
    for node in nodes:
        for connected_node in nodes[node].connected_nodes:
            from_coord = nodes[node].coordinates
            to_coord = connected_node.coordinates
            coord_x = [from_coord[0], to_coord[0]]
            coord_y = [from_coord[1], to_coord[1]]
            lines.append(ax.plot(coord_x, coord_y, c='r', linewidth=nodes[node].pheromone*0.05, label="Pheromone"))
    return lines
