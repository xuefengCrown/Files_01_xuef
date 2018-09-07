package algs.xuef2018.priorityQueue;

import java.util.LinkedList;
import java.util.Queue;

/**
 * BST 二叉搜索树实现symbol table
 *
 * @author moveb
 *
 * @param <Key>
 * @param <Value>
 */
public class BST<Key extends Comparable<Key>, Value> {
	private Node root; // root of BST
	private class Node{
		private Key key;
		private Value value;
		private Node left, right;
		public Node(Key k, Value v){
			key = k;
			value = v;
		}
	}
	
	// put 递归实现
	public void put_recur(Key k, Value v){
		root = put_recur(root, k, v);
	}
	public Node put_recur(Node x, Key k, Value v){
		if (x == null) return new Node(k, v);
		int cmp = x.key.compareTo(k);
		if (cmp > 0) x.left = put_recur(x.left, k, v);
		else if (cmp < 0) x.right = put_recur(x.right, k, v);
		else  x.value = v;
		return x;
	}
	
	public void put(Key k, Value v){
		Node tempNode = root;
		Node newNode = new Node(k, v);
		while (true){
			if (root==null) { 
				root = newNode;
				break; 
			}else{
				Key key = tempNode.key;
				if (key.compareTo(k) > 0){
					if(tempNode.left == null){
						tempNode.left =newNode;
						break;
					}
					tempNode = tempNode.left;
				}else{
					if(tempNode.right == null){
						tempNode.right =newNode;
						break;
					}
					tempNode = tempNode.right;
				}
			}
		}
	}
	public Value get(Key k){
		Node tempNode = root;
		while(true){
			if (tempNode == null) return null;
			
			int cmp = tempNode.key.compareTo(k);
			if (cmp > 0){
				tempNode = tempNode.left;
			}else if(cmp < 0){
				tempNode = tempNode.right;
			}else{
				return tempNode.value;
			}
		}
	}
	public void delete(Key k){
		
	}
	public Iterable<Key> keys(){
		Queue<Key> q = new LinkedList<Key>();
		inorder(root, q);
		return q;
	}
	
	public void inorder(Node x, Queue<Key> q){
		if (x == null) return;
		inorder(x.left, q);
		q.add(x.key);
		inorder(x.right, q);
	}
}
