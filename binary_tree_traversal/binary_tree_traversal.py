# Pre-order traversal
def pre_order(node):
    def traverse(node, result=[]):
        if node:
            result.append(node.data)
            traverse(node.left, result)
            traverse(node.right, result)
        return result
    return traverse(node)

# In-order traversal
def in_order(node):
    def traverse(node, result=[]):
        if node:
            traverse(node.left, result)
            result.append(node.data)
            traverse(node.right, result)
        return result
    return traverse(node)

# Post-order traversal
def post_order(node):
    def traverse(node, result=[]):
        if node:
            traverse(node.left, result)
            traverse(node.right, result)
            result.append(node.data)
        return result
    return traverse(node)
