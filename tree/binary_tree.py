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

    def preorder(self) -> List[int]:
        return self._preorderTraversal(self.root)
    
    def _preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: 
            return []
        ans = [root.val]
        ans += self._preorderTraversal(root.left)
        ans += self._preorderTraversal(root.right)
        return ans 
    
    def inorder(self) -> List[int]: 
        return self._inorderTraversal(self.root)

    def _inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: 
            return []
        ans = []
        ans += self._inorderTraversal(root.left)
        ans.append(root.val) 
        ans += self._inorderTraversal(root.right)
        return ans 
    
    def postorder(self) -> List[int]:
        return self._postorderTraversal(self.root)

    def _postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: 
            return []
        ans = self._postorderTraversal(root.left)
        ans += self._postorderTraversal(root.right)
        ans += [root.val]
        return ans 

    def levelOrder(self) -> List[List[int]]:
        if not self.root: 
            return []
        queue, result = [self.root], []
        while queue: 
            next_queue, ans = [], []
            for node in queue: 
                ans.append(node.val)
                if node.left: 
                    next_queue.append(node.left)
                if node.right: 
                    next_queue.append(node.right)
            result.append(ans)
            queue = next_queue
        return result 

    def levelOrderTraversal(self, root: Optional[TreeNode]) -> List[int]:
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
