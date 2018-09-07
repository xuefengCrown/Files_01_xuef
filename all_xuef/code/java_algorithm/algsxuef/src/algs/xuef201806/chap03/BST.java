package algs.xuef201806.chap03;

import algs.base.StdOut;
import algs.xuef201806.chap01.Queue;

/**
 * 二叉查找树
 * @author moveb
 *
 */
public class BST<Key extends Comparable<Key>, Value> {
	private Node root; // 二叉查找树的根节点
	private class Node{
		private Key key;
		private Value val;
		private Node left, right; // 指向子树的链接
		private int N; // 以该节点为根的子树中的节点总数
		
		public Node(Key key, Value val, int N){
			this.key = key;
			this.val = val;
			this.N = N;
		}
	}
	
	public int size(){
		return size(root);
	}
	public int size(Node x){
		if(x == null) return 0;
		else return x.N;
	}
	
	public Value get(Key k){
		return get(root, k);
	}
	public Value get(Node x, Key k){
		if(x == null) return null;
		// x 不为 null
		int cmp = k.compareTo(x.key);
		if(cmp > 0) return get(x.right, k);
		if(cmp < 0) return get(x.left, k);
		else return x.val;
	}
	
	public void put(Key k, Value v){
		// 查找key, 找到则更新它的值, 否则为它创建一个新的节点
		root = put(root, k, v);
	}
	/**
	 * 将(k,v)插入到以 x 为根节点的子树中。且返回节点 x 
	 * @param x
	 * @param k
	 * @param v
	 * @return
	 */
	public Node put(Node x, Key k, Value v){
		if(x == null) return new Node(k, v, 1);
		int cmp = k.compareTo(x.key);
		if(cmp < 0) // k小于x.key, 插入x的左子树
			x.left = put(x.left, k, v); // 你得信任递归!
		else if(cmp > 0)
			x.right = put(x.right, k, v);
		else
			x.val = v;
		x.N = size(x.left) + size(x.right) + 1;
		return x;
	}
	/**
	 * 删除键最小元素
	 */
	public void deleteMin(){
		deleteMin(root);
	}
	/**删除 以x为根的子树的最小节点
	 * 
	 * 我们不必太纠结于递归的执行细节;
	 * 一个递归是有效的，只要它能处理所有情况：
	 * 本例中：
	 * 1. 如果左子树为空
	 * 2. 左子树不为空
	 * @param x
	 * @return
	 */
	private Node deleteMin(Node x){
		// 不断检测左子树,直到左子树为空，此时的x即为键最小的节点。返回它的右链接
		if(x.left == null) return x.right;
		x.left = deleteMin(x.left);
		x.N = size(x.left) + size(x.right) + 1; // 这个x.N的计算方法是通用的
		return x; // 这个返回值很重要, 要保持一致性。
	}
	
	public void delete(Key k){
		root = delete(root, k);
	}
	
	public Node delete(Node x, Key k){
		if(x == null) return null;
		// 寻找要删除的节点
		int cmp = k.compareTo(x.key);
		if(cmp < 0) x.left = delete(x.left, k);
		else if(cmp > 0) x.right = delete(x.right, k);
		else{
			/**
			 * 1. 将指向即将被删除的节点的链接保存为 t
			 * 2. 将x指向它的后继节点min(t.right)
			 * 3. 将x的右链接指向 deleteMin(t.right)
			 * 4. 将x的左链接设为t.left
			 */
			if(x.right == null) return x.left;
			if(x.left == null) return x.right;
			Node t = x;
			x = min(t.right); // 原 x 节点被删除了
			x.right = deleteMin(t.right);
			x.left = t.left;
		}
		x.N = size(x.left) + size(x.right) + 1;
		return x;
	}
	/**
	 * 返回以x为根的子树的最小节点
	 * @param x
	 * @return
	 */
	public Node min(Node x){
		if(x.left == null) return x;
		return min(x.left);
	}
	
	/**
	 * 中序遍历
	 */
	public void infix(Node x){
		if(x == null) return;
		// 中序遍历左子树
		infix(x.left);
		// 输出根节点
		StdOut.print(x.key + ", ");
		// 中序遍历右子树
		infix(x.right);
	}

	public Iterable<Key> keys(){
		//keys(min(), max());
		return null;
	}
	public Iterable<Key> keys(Key lo, Key hi){
		Queue<Key> queue = new Queue<Key>();
		keys(root, queue, lo, hi);
		return queue;
	}
	public void keys(Node x, Queue<Key> queue, Key lo, Key hi){
		if(x == null) return;
		int cmplo = lo.compareTo(x.key);
		int cmphi = hi.compareTo(x.key);
		// lo < x.key
		if(cmplo < 0) keys(x.left, queue, lo, hi);
		if(cmplo <= 0 && cmphi >= 0) queue.enqueue(x.key);
		if(cmphi > 0) keys(x.right, queue, lo, hi);
	}
	
	public static void main(String[] args) {
		BST<String, Integer> bst = new BST();
		bst.put("b1", 1);
		bst.put("a1", 1);
		bst.put("a2", 1);
		bst.put("c3", 1);
		bst.infix(bst.root);
	}
}

