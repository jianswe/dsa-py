import pytest
from tree.binary_tree import BinaryTree

@pytest.mark.parametrize("nums", [
    ([3,9,20,None,None,15,7]),
    ([1]),
    ([])
])
def test_binary_tree(nums): 
    bt = BinaryTree(nums)
    assert BinaryTree.levelOrderTraversal(bt.root) == nums