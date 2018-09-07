package algs.implebyme;

import java.util.Iterator;
import java.util.NoSuchElementException;

// 链表 包含头节点first 和尾结点 last
public class LinkedList<Item> implements Iterable<Item>{
	private Node first; //指向第一个节点 或说（保存第一个节点的地址）
	private Node last;
	public void addNode(Item i){
		Node node = new Node();
		node.item=i;
		node.next=null;
		if(first==null){
			first=node;
			last=node;
		}else{
			last.next=node;
			last=node;
		}
	}
	public boolean find(Item key){
		for(Item i:this){
			if(i.equals(key)) return true; //什么叫相等？这是个问题（不过这应该由client来定义）
		}
		return false;
	}
	// 寻找最大元素 递归实现 ex 1.3.18
	
	private class Node{
		Item item;
		Node next;
	}

	@Override
	public Iterator<Item> iterator() {
		return new LinkedListIterator();
	}
	private class LinkedListIterator implements Iterator<Item>{
		private Node current=first;
		@Override
		public boolean hasNext() {
			return current!=null;
		}

		@Override
		public Item next() {
			if(!hasNext()) throw new NoSuchElementException();
			Item i = current.item;
			current = current.next;
			return i;
		}

		@Override
		public void remove() {
			
		}
		
	}
}
