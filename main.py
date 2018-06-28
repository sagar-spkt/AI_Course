import numpy as np
from problems import NQueen
from uninformed_search_algo import breadth_first_search, depth_first_search, depth_limit_search


class Node:
    search_data = None

    def __init__(self, data=None, parent=None):
        self.left = None
        self.right = None
        self.data = data
        self.parent = parent

    def insert(self, data):
        if self.data:
            if data <= self.data:
                if not self.left:
                    self.left = Node(data, parent=self)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if not self.right:
                    self.right = Node(data, parent=self)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def generate_successors(self):
        return [self.left, self.right]

    def goal_test(self):
        return self.data == Node.search_data

    def is_in(self, array_list):
        if not self:
            return False
        return any([self.data == iter_item.data for iter_item in array_list])


if __name__ == '__main__':
    tree_data = [int(item) for item in input('Enter data: ').split()]
    Node.search_data = int(input('Enter what you want to search: '))
    root_node = Node()
    for data in tree_data:
        root_node.insert(data)
    solution = depth_first_search(root_node)
    if solution:
        path = []
        while solution:
            path.append(solution.data)
            solution = solution.parent
        print(path)

