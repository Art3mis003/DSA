class TreeNode:
    def __init__(self,val,left,right):
        self.val= val
        self.left=left
        self.right=right
class Solution:
    def GoodNode(self, root):
        def dfs(root,maxvalue):
            if not root:
                return 0
            res= 1 if root.val>=maxvalue else 0
            maxvalue= max(maxvalue, root.val)
            res+=dfs(root.right,maxvalue)
            res+= dfs(root.left, maxvalue)
            return res
        return dfs(root,root.val)

root= TreeNode(3,TreeNode(1,TreeNode(3,None,None),None),TreeNode(4,TreeNode(1,None,None),TreeNode(5,None,None)))
print(Solution().GoodNode(root))
