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
        for entity_id, metadata in fs.items():
            if metadata['type'] == 'file':
                node = Node(entity_id, metadata['name'], is_file=True, size=metadata['size'])
            elif metadata['type'] == 'dir':
                node = Node(entity_id, metadata['name'], is_file=False, size=0)
            else:
                raise ValueError(f"Invalid type: {metadata['type']}")

            self.nodes[entity_id] = node

        # build parent-child relationship
        for entity_id, entity in fs.items():
            if entity['type'] == 'dir':
                parent_node: Node = self.nodes[entity_id]
                for child in entity['children']:
                    child_node = self.nodes[child]
                    child_node.parent = parent_node
                    parent_node.children[child] = child_node
                    self._update_parent_size(child_node)

    def _update_parent_size(self, child_node: Node) -> None:
        size_delta = child_node.size
        current = child_node
        while current:
            current.size += size_delta
            current = current.parent

    def get_size(self, entity_id) -> int:
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
