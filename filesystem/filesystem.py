#!/usr/bin/env python3

"""
Implement an augmented tree representing the filesystem
"""

class Node:
    def __init__(self, entity_id: int, name: str, is_file: bool = False, size: int = 0) -> None:
        self.entity_id = entity_id
        self.name = name
        self.size = size
        self.is_file = is_file
        self.children = {}
        self.parent = None


class FileSystemTree:
    def __init__(self) -> None:
        self.nodes = {}

    def build_file_system_tree(self, fs: dict) -> None:
        """
        Creates nodes and establish parent-child relationships

        Args:
            fs: dict - dictionary ionput of filesystem objects. Iterated twice: first to create nodes, second to create parent-child relationships.
        """
        # iterate fs dictionary, if entity is file, create file node with is_file=True, size=metadata['size']. If entity is dir, create dir node with is_file=False, size=0
        # if key is invalid entity_id, raise ValueError
        for entity_id, metadata in fs.items():
            if metadata['type'] == 'file':
                node = Node(entity_id, metadata['name'], is_file=True, size=metadata['size'])
            elif metadata['type'] == 'dir':
                node = Node(entity_id, metadata['name'], is_file=False, size=0)
            else:
                raise ValueError(f"Invalid type: {metadata['type']}")

            # add created node to tree without p-c relationship
            self.nodes[entity_id] = node

        # build parent-child relationship
        for entity_id, entity in fs.items():
            if entity['type'] == 'dir':
                parent_node: Node = self.nodes[entity_id]
                for child in entity['children']:
                    child_node = self.nodes[child]
                    child_node.parent = parent_node
                    parent_node.children[child] = child_node
                    # once parent-child relationship is built, update parent size.
                    self._update_parent_size(child_node)

    def _update_parent_size(self, child_node: Node) -> None:
        """
        Updates the parent nodes by the added child node's size size_delta

        Args:
            node: Node - actual child node

        obtain size_delta from the added node's size attribute
        set the immediate parent to current which will be updated
        while there is a current, update current size by size_delta
        continue, update current to current.parent - this updates parent at each level above.
        """
        size_delta = child_node.size
        current = child_node
        while current:
            current.size += size_delta
            current = current.parent

    def get_size(self, entity_id) -> int:
        """
        Returns folder/file/entity size

        Args:
            entity_id: id of the entity.

        Check if entity_id is valid - in self.nodes.keys()
        If not, raise KeyError
        Else return node's actual size
        """
        if entity_id not in self.nodes.keys():
            raise KeyError(f"Key not found: {entity_id}")
        else:
            return self.nodes[entity_id].size


if __name__ == "__main__":
    
    fs_dict: dict = {
        1: {'type':'dir', 'name':'dir', 'children':[5]},
        2: {'type':'dir', 'name':'root', 'children':[1,3,4]},
        3: {'type':'file', 'name':'file1', 'size': 200},
        4: {'type':'file', 'name':'file2', 'size': 100},
        5: {'type':'file', 'name':'file3', 'size': 300}
    }

    fs: FileSystemTree = FileSystemTree()
    fs.build_file_system_tree(fs_dict)

    print(fs.get_size(2))
