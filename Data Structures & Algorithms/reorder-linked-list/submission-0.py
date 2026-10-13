# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        nodes = []

        while curr!=None:
            nodes.append(curr)
            curr=curr.next
        
        n = len(nodes)

        left, right = 1, n-1
        curr = head
        while left<=right:
            curr.next = nodes[right]
            curr = curr.next
            
            if left<right:
                curr.next = nodes[left]
                curr = curr.next

            left+=1
            right-=1

        curr.next = None