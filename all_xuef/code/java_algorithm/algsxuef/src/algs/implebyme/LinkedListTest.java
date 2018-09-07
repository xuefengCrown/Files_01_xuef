package algs.implebyme;

import algs.base.StdOut;

public class LinkedListTest {
	public static void main(String[] args) {
		LinkedList<String> ll=new LinkedList<>();
		ll.addNode("aaa");
		ll.addNode("ccc");
		ll.addNode("eee");
		for(String s:ll){
			StdOut.println(s);
		}
		StdOut.print(ll.find("ddd"));
	}
}
