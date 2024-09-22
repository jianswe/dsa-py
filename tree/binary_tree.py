from collections import deque
from typing import List, Optional
from tree.tree_node import TreeNode

class BinaryTree: 
    def __init__(self, nums: List[int]):
        if not nums or nums[0] is None:
            self.root = None
            return 
        self.root = TreeNode(nums[0])
        queue = deque([self.root])
        i=1
        while queue and i<len(nums): # Iterate over the array and build the tree
            node = queue.popleft()
            if nums[i] is not None: # Assign left child
                node.left = TreeNode(nums[i]) 
                queue.append(node.left)
            i+=1 
            if i >= len(nums): # Check if we've reached the end of the array
                break
            if nums[i] is not None: # Assign right child
                node.right = TreeNode(nums[i])
                queue.append(node.right)
            i+=1

    @staticmethod
    def levelOrderTraversal(root: Optional[TreeNode]):
        if not root: 
            return []
        result = []
        queue = deque([root])
        while queue: 
            node = queue.popleft()
            if node: 
                result.append(node.val)
                queue.append(node.left)  # Add left child, could be None
                queue.append(node.right) # Add right child, could be None
            else: 
                result.append(None)  # Append null if node is None
            
        # Remove trailing None values that represent missing nodes at the last level
        while result and result[-1] is None:
            result.pop()
        return result
