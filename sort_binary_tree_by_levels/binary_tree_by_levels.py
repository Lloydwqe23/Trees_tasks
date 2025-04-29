from collections import deque
def tree_by_levels(node):
    if not node:
        return []
    queue = deque([node])
    result = [node.value]

    while queue:
        element = queue.popleft()

        if element.left:
            queue.append(element.left)
            result.append(element.left.value)
        if element.right:
            queue.append(element.right)
            result.append(element.right.value)
    return result