# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root:
            if not root.left and not root.right:
                if key == root.val:
                    return None
        def find(element, key):
            if not element:
                return None
            if element.val < key:
                element.right = find(element.right, key)
            elif element.val > key:
                element.left = find(element.left, key)
            else:
                if not element.left:
                    return element.right
                elif not element.right:
                    return element.left
                else:
                    curr = element.right
                    while curr.left:
                        curr = curr.left
                    element.val = curr.val
                    element.right = find(element.right, curr.val)

                
            return element
        return find(root, key)

        