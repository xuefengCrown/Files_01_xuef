package algs.xuef201806.chap03;

import algs.base.SequentialSearchST;

/**
 * 算法3.5 基于拉链法的散列表
 * 让我想起了《c程序设计语言》中的 字符串数组
 * @author moveb
 *
 */
public class SeparateChainingHashST<Key, Value> {
	private int N; // 键值对总数
	private int M; // 散列表的大小
	private SequentialSearchST<Key, Value>[] st; // 存放链表对象的数组
	public SeparateChainingHashST(){
		
	}
	public SeparateChainingHashST(int M){
		// 创建 M 条链表
		this.M = M;
		st = (SequentialSearchST<Key, Value>[])new SequentialSearchST[M];
		// 初始化每条链表
		for(int i=0; i<M; i++){
			st[i] = new SequentialSearchST();
		}
	}
	
	private int hash(Key key){
		return (key.hashCode() &0x7fffffff) % M;
	}
	public Value get(Key key){
		return (Value)st[hash(key)].get(key);
	}
	public void put(Key k, Value v){
		st[hash(k)].put(k, v);
	}
	// TODO
	public Iterable<Key> keys(){
		return null;
	}
}
