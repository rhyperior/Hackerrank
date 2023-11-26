from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createTree(self, tree_list: List) -> Optional[TreeNode]:
        if not tree_list:
            return None

        root_node = TreeNode(val=tree_list.pop(0))

        if tree_list:
            root_node.left = TreeNode(val=tree_list.pop(0))
        if tree_list:
            root_node.right = TreeNode(val=tree_list.pop(0))

        return root_node


if __name__ == "__main__":
    tree_list = [4, 2, 7, 1, 3, 6, 9]
    print(Solution().threeSum(tree_list=tree_list))
