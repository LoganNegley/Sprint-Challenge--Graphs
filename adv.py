from room import Room
from player import Player
from world import World

from graph import Graph
from graph import Queue
from graph import Stack

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']



# loop through graph until every room has been visited
# start with current room
# if not in visited add that room to visited
# prev room added to path



################################### My Code Below Line#################

traversal_path = []
path = []
visited_rooms = {}
opposite = {'n': 's', 'e':'w', 's': 'n', 'w': 'e'}


# Starting in room 0------only exit is north small map
# print(player.current_room.get_exits())

visited_rooms[player.current_room.id] = player.current_room.get_exits()

while len(visited_rooms) < len(room_graph) -1: #if we haven't been to all rooms---keep going
    if player.current_room.id not in visited_rooms: # if current is not in visited
        visited_rooms[player.current_room.id] = player.current_room.get_exits()  #add current to visited
        previous = path[-1] #add last room in to our path at end
        visited_rooms[player.current_room.id].remove(previous)
    while len(visited_rooms[player.current_room.id]) < 1: #while theres rooms in visited
        previous = path.pop()  #take from prev and add to traversal
        traversal_path.append(previous)
        player.travel(previous)






























################### My code above this line##################
# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
