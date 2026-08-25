# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:     
        if not root:
            return False

        queue = [root]

        while queue:
            curr = queue.pop()
            
            if curr.val==subRoot.val:
                one_q = [curr, subRoot]
                is_match = True
                while one_q:
                    curr1 = one_q.pop()
                    curr2 = one_q.pop()
                    
                    if not curr1 and not curr2:
                        continue

                    if not curr1 or not curr2 or curr1.val!=curr2.val:
                        is_match = False
                        break
                    
                    one_q.append(curr2.left)
                    one_q.append(curr1.left)
                    one_q.append(curr2.right)
                    one_q.append(curr1.right)
            
                if is_match:
                    return True

            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        
        return False