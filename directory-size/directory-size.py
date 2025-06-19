"""
Given a file system structure how can you find the size of a folder 
given each item is either folder with id of the items inside of it,
or a file with name and size.
"""

#If can be represented as a graph, using DFS you can identify (in the stack | queue) if your item is a 
#directory, if a directory continue DFS and increment a total count if you find a valid file node.

