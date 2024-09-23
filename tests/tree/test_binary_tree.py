import pytest
from tree.binary_tree import BinaryTree

@pytest.mark.parametrize("nums, expected", [
    ([1,None,2,3], [1,2,3]),
    ([1,2,3,4,5,None,8,None,None,6,7,9], [1,2,4,5,6,7,3,8,9]), 
    ([], []), 
    ([1], [1])
])
def test_preorder(nums, expected): 
    bt = BinaryTree(nums)
    assert bt.preorder() == expected

@pytest.mark.parametrize("nums, expected", [
    ([1,None,2,3], [1,3,2]),
    ([1,2,3,4,5,None,8,None,None,6,7,9], [4,2,6,5,7,1,3,9,8]), 
    ([], []), 
    ([1], [1])
])
def test_inorder(nums, expected): 
    bt = BinaryTree(nums)
    assert bt.inorder() == expected

@pytest.mark.parametrize("nums, expected", [
    ([1,None,2,3], [3,2,1]),
    ([1,2,3,4,5,None,8,None,None,6,7,9], [4,6,7,5,2,9,8,3,1]), 
    ([], []), 
    ([1], [1])
])
def test_postorder(nums, expected): 
    bt = BinaryTree(nums)
    assert bt.postorder() == expected

@pytest.mark.parametrize("nums, expected", [
    ([3,9,20,None,None,15,7], [[3],[9,20],[15,7]]), 
    ([1], [[1]]), 
    ([], [])
])
def test_levelOrder(nums, expected): 
     bt = BinaryTree(nums)
     assert bt.levelOrder() == expected

@pytest.mark.parametrize("nums", [
    ([3,9,20,None,None,15,7]),
    ([1]),
    ([])
])
def test_levelOrderTraversal(nums): 
    bt = BinaryTree(nums)
    assert bt.levelOrderTraversal(bt.root) == nums



