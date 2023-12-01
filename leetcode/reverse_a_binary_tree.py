from typing import List, Optional
import math


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createTree(
        self, tree_list: List, depth=None, parent_node=None, root=None
    ) -> Optional[TreeNode]:
        if not tree_list or depth == 1:
            return None

        if not depth:
            depth = math.ceil(math.log(len(tree_list) + 1, 2))

        if not root:
            root = TreeNode(val=tree_list.pop(0))
            parent_node = root
        elif not parent_node:
            return

        if tree_list:
            val = val = tree_list.pop(0)
            if val:
                parent_node.left = TreeNode(val=val)

        if tree_list:
            val = val = tree_list.pop(0)
            if val:
                parent_node.right = TreeNode(val=val)

        self.createTree(
            tree_list, depth=depth - 1, parent_node=parent_node.left, root=root
        )

        self.createTree(
            tree_list, depth=depth - 1, parent_node=parent_node.right, root=root
        )

        return parent_node

    def traverse_tree(self, root):
        if not root:
            return []

        _stack = [root]
        visited = [root.val]
        current_node = None

        while _stack:
            current = _stack.pop()

            children = []
            if getattr(current, "right") or getattr(current, "left"):
                if getattr(current, "right"):
                    _stack.append(current.right)

                if getattr(current, "left"):
                    _stack.append(current.left)

                if getattr(current, "right"):
                    children.append(current.right.val)
                else:
                    children.append(None)
                if getattr(current, "left"):
                    children.append(current.left.val)
                else:
                    children.append(None)

            # if getattr(current, "left"):
            #     _stack.append(current.left)
            #     children.append(current.left.val)

            children.reverse()
            visited.extend(children)

        return visited

    def reverse_tree(self, root):
        if not root:
            return None

        _stack = [root]
        current = None

        while _stack:
            current = _stack.pop()
            if hasattr(current.right, "left"):
                _stack.append(current.right)
            if hasattr(current.left, "left"):
                _stack.append(current.left)
            current.right, current.left = current.left, current.right
        return


if __name__ == "__main__":
    tree_list = [4, 2, 7, 1, 3, 6, 9]
    # tree_list = [4, 2, 7, 1, 3, 10, 11, 12, 13, 6, 9, 14, 15, 16, 17]
    tree_list = [2, 3, None, 1]
    # tree_list = []
    # tree_list = [1]
    root = Solution().createTree(tree_list=tree_list)
    print(Solution().traverse_tree(root=root))
    Solution().reverse_tree(root=root)
    print(Solution().traverse_tree(root=root))
