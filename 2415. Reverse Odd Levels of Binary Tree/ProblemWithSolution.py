'''

Given the root of a perfect binary tree, reverse the node values at each odd level of the tree.

For example, suppose the node values at level 3 are [2,1,3,4,7,11,29,18], then it should become [18,29,11,7,4,3,1,2].
Return the root of the reversed tree.

A binary tree is perfect if all parent nodes have two children and all leaves are on the same level.

The level of a node is the number of edges along the path between it and the root node.

 

Example 1: Tree image


Input: root = [2,3,5,8,13,21,34]
Output: [2,5,3,8,13,21,34]
Explanation: 
The tree has only one odd level.
The nodes at level 1 are 3, 5 respectively, which are reversed and become 5, 3.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        v=[root]
        l=0
        while v:
            l+=1
            vc=[]
            for i in v:
                if(i.left):
                    vc+=[i.left]
                if(i.right):
                    vc+=[i.right]
            if(l%2==1):
                for i in range((len(vc)+1)//2):
                    vc[i].val,vc[len(vc)-i-1].val=vc[len(vc)-i-1].val,vc[i].val
            v=vc
        return root
        
