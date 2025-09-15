class Tree:
    def __init__(self, root):
        self.root = root

    def get_element_by_id(self, target_id):
        nodes_to_visit = [self.root]

        while nodes_to_visit:
            node = nodes_to_visit.pop(0)  # Remove first node (queue behavior)
            if node['id'] == target_id:
                return node
            nodes_to_visit.extend(node['children'])  # Add children at end

        return None


root = {
    "id": 1,
    "children": [
        {"id": 2, "children": []},
        {"id": 3, "children": [
            {"id": 4, "children": []}
        ]}
    ]
}


tree = Tree(root)

print(tree.get_element_by_id(3))


print(tree.get_element_by_id(4))

print(tree.get_element_by_id(10))








         

