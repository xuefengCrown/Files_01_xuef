package algs.xuef2018.priorityQueue;

public class Red_Black_BST<Key extends Comparable<Key>, Value> {
	private static final boolean RED = true;
	private static final boolean BLACK = false;
	
	private class Node{
		Key key;
		Value value;
		Node left, right;
		boolean color; // color of parent link 
	}
	
	private boolean isRed(Node x){
		if(x == null) return false;
		return x.color == RED;
	}
}
