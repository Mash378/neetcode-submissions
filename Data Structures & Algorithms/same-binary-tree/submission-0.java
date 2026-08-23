
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if ((p==null && q!=null) || (p!=null && q==null)){
            return false;
        }

        Queue<TreeNode> p_queue = new LinkedList<>();
        p_queue.add(p);
        Queue<TreeNode> q_queue = new LinkedList<>();
        q_queue.add(q);

        while(!p_queue.isEmpty() && !q_queue.isEmpty()){
            int p_len = p_queue.size();
            int q_len = q_queue.size();

            for(int i=0;i<Math.min(p_len, q_len);i++){
                TreeNode p_node = p_queue.poll();
                TreeNode q_node = q_queue.poll();

                if (p_node==null && q_node==null){
                    continue;
                }
                if ((p_node==null && q_node!=null) || (p_node!=null && q_node==null)){
                    return false;
                }
                if (p_node.val!=q_node.val){
                    return false;
                }
                
                p_queue.add(p_node.left);
                q_queue.add(q_node.left);
                p_queue.add(p_node.right);
                q_queue.add(q_node.right);
            }
        }
        return true;
    }

}
