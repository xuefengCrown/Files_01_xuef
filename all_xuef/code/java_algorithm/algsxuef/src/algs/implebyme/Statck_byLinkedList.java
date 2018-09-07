package algs.implebyme;

import java.util.Iterator;
import java.util.NoSuchElementException;

public class Statck_byLinkedList<Item> implements Iterable<Item>{
	private Node first; // 指向最近添加的元素
	private int N;
	public Statck_byLinkedList(){
		N=0;
		first=null;//?
	}
	public int size(){ return N; }
	public boolean isEmpty(){ return first==null;}
	public void push(Item item){
		Node node=new Node();
		node.i = item;
		node.next=first;
		first=node;
		N++;
	}
	public Item pop(){
		Item item=null;
		if(!isEmpty()){ //如果栈为空？这里的处理很不好，因为用户完全不知道问题在哪。
			item = first.i;
			first = first.next;
		}
		N--;
		return item;
	}
	public Item peek(){
		return first.i;
	}
	private class Node{
		Item i;
		Node next;
	}
	@Override
	public Iterator<Item> iterator() {
		return new StackIterator();
	}
	private class StackIterator implements Iterator<Item>{
		private Node current = first;
		@Override
		public boolean hasNext() {
			return current!=null;
		}

		@Override
		public Item next() {
			if(!hasNext()) throw new NoSuchElementException();
			Item i = current.i;
			current = current.next;
			return i;
		}

		@Override
		public void remove() {
			throw new UnsupportedOperationException();
		}
		
	}
}
