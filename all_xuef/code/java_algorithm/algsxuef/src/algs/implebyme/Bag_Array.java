package algs.implebyme;

import java.util.Iterator;

public class Bag_Array<Item> implements Iterable<Item>{
	private Item[] a;
	private int N;
	public Bag_Array(int cap){
		a = (Item[]) new Object[cap];
		N=0;
	}
	public void add(Item i){
		a[N]=i;
		N++;
	}
	@Override
	public Iterator<Item> iterator() {
		// TODO Auto-generated method stub
		return new BagScanIterator();
	}
	private class BagScanIterator implements Iterator<Item>{
		Item[] t = a;
		@Override
		public boolean hasNext() {
			return N>0;
		}

		@Override
		public Item next() {
			return null;
		}

		@Override
		public void remove() {}
	}
}
