def delete_middle_node(node):
    if node is None or node.next is None:
        return 0
    node.data = node.next.data
    node.next = node.next.next
    return 1
    