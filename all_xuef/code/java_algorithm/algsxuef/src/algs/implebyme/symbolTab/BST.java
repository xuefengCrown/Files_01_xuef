package algs.implebyme.symbolTab;

import java.util.Queue;
import java.util.concurrent.LinkedBlockingQueue;

public class BST<Key extends Comparable<Key>, Value> {
	private Node root; // 二叉查找树 的 根
	private class Node{
		private Key key;
		private Value value;
		private Node left, right;
		private int N; // 以该结点为根的子树的结点树
		public Node(Key key, Value value, int n) {
			super();
			this.key = key;
			this.value = value;
			N = n;
		}
	}
	private int size(Node x){
		if(x==null) return 0;
		else return x.N;
	}
	public int size(){
		return size(root);
	}
	
	public void put(Key key, Value value){
		root = insert(key, value, root);
	}
	// put 的辅助函数
	private Node insert(Key key, Value value, Node b_tree){
		if(b_tree == null) return new Node(key, value, 1);
		int cmp = key.compareTo(b_tree.key);
		if(cmp < 0) b_tree.left = insert(key, value, b_tree.left);
		if(cmp > 0) b_tree.right = insert(key, value, b_tree.right);
		else b_tree.value = value;
		b_tree.N = size(b_tree.left) + size(b_tree.right) + 1;
		return b_tree;
	}
	public Value get(Key key){
		return get(key, root);
	}
	// get 的辅助函数
	private Value get(Key key, Node b_tree){
		if(b_tree == null) return null;
		int cmp = key.compareTo(b_tree.key);
		if(cmp == 0) return b_tree.value;
		if(cmp < 0) return get(key, b_tree.left);
		else return get(key, b_tree.right);
	}
	//中序遍历二叉查找树
	public void inorder(){
		inorder(root);
	}
	public void inorder(Node b_tree){
		if(b_tree == null) return;
		inorder(b_tree.left);
		System.out.println(b_tree.key + " " + b_tree.value);
		inorder(b_tree.right);
	}
	// 返回最小键
	public Key min(){
		return min(root);
	}
	public Key min(Node b_tree){
		if(b_tree != null && b_tree.left == null) return b_tree.key;
		return min(b_tree.left);
	}
	// 返回最大键
	public Key max(){
		return max(root);
	}
	public Key max(Node b_tree){
		if(b_tree != null && b_tree.right == null) return b_tree.key;
		return max(b_tree.right);
	}
	// 返回某范围的键组合（放置在队列中）
	public Iterable<Key> keys(){
		return keys(min(), max());
	}
	public Iterable<Key> keys(Key lo, Key hi){
		Queue<Key> queue = new LinkedBlockingQueue<Key>();
		keys(root, queue, lo, hi);
		return queue;
	}
	private void keys(Node b_tree, Queue<Key> queue, Key lo, Key hi){
		if(b_tree == null) return;
		int cmplo = lo.compareTo(b_tree.key);
		int cmphi = hi.compareTo(b_tree.key);
		if (cmplo < 0) keys(b_tree.left, queue, lo, hi);
		if (cmplo <= 0 && cmphi >= 0) queue.add(b_tree.key);
		if (cmphi > 0) keys(b_tree.right, queue, lo, hi);
	}
	public void levelorder(){
		Queue<Node> queue = new LinkedBlockingQueue<Node>();
		queue.add(root);
		Node tNode;
		while(!queue.isEmpty()){
			tNode = queue.poll();
			System.out.println(tNode.key);
			if(tNode.left != null) queue.add(tNode.left);
			if(tNode.right != null) queue.add(tNode.right);
		}
	}
}
