package algs.xuef201806.chap05;

import algs.xuef201806.chap01.Queue;

/**
 * 基于单词查找树的符号表
 * @author moveb
 *
 * @param <Value>
 */
public class TrieST<Value> {
	private static int R = 256; // 基数
	private Node root; //
	
	private static class Node{
		private Object val;
		private Node[] next = new Node[R];
	}
	// 结合put, 才能理解get
	public Value get(String key){
		Node x = get(root, key, 0);
		if(x == null) return null;
		return (Value)x.val;
	}
	private Node get(Node x, String key, int d){
		// 返回以x作为根结点的子单词查找树中与key相关联的值
		if(x == null) return null;
		if(d == key.length()) return x;
		char c = key.charAt(d); // 找到第d个字符所对应的子单词查找树
		return get(x.next[c], key, d+1);
	}
	public void put(String key, Value val){
		root = put(root, key, val, 0);
	}
	private Node put(Node x, String key, Value val, int d){
		// 如果key存在于以x为根结点的子单词树中则更新与它相关联的值
		if(x == null) return new Node();
		if(d == key.length()){
			x.val = val;
			return x;
		}
		char c = key.charAt(d); // 找到第d个字符所对应的子单词查找树
		// 如果c是s, next[c]会先将's'转为对应的int值, ord('s')-->115
		// x.next[c]-->结点x的第ord(c)个链接
		x.next[c] = put(x.next[c], key, val, d+1);
		return x;
	}
	public int size(){
		return size(root);
	}
	/**
	 * 以x作为根节点的子单词查找树的键的数量
	 * 学习递归的好例子
	 * @param x
	 * @return
	 */
	public int size(Node x){
		// 空结点自然没有键
		if(x == null) return 0;
		int cnt = 0;
		// 如果该结点的val不为空, 那么遇到了一个键
		if(x.val != null) cnt++;
		for(char c=0; c<R; c++){
			cnt += size(x.next[c]);
		}
		return cnt++;
	}
	public Iterable<String> keys(){
		return keysWithPrefix("");
	}
	public Iterable<String> keysWithPrefix(String pre){
		Queue<String> q = new Queue<String>();
		collect(get(root, pre, 0), pre, q);
		return q;
	}
	/**
	 * 从 以x为根结点的子单词查找树中 收集以pre开头的键
	 * @param x
	 * @param pre
	 * @param q
	 */
	private void collect(Node x, String pre, Queue<String> q){
		if(x == null) return;
		if(x.val != null) q.enqueue(pre);
		for(char c=0; c<R; c++){
			collect(x.next[c], pre + c, q);
		}
	}
}
