# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        hashMap = {} #{num: [preorder index, inorder index]}
        for index, num in enumerate(preorder):
            hashMap[num] = [index]
        for index, num in enumerate(inorder):
            hashMap[num].append(index)
        inOrderIndex = hashMap[preorder[0]][1]
        leftHalf, rightHalf = inorder[:inOrderIndex], inorder[inOrderIndex+1:]
        root = TreeNode(preorder[0])
        root.left = self.buildTree(preorder[1:len(leftHalf) + 1], leftHalf)
        root.right = self.buildTree(preorder[len(leftHalf)+1:], rightHalf)
        return root