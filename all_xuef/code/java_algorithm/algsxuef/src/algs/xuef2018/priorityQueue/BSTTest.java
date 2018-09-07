package algs.xuef2018.priorityQueue;

import algs.base.StdOut;

public class BSTTest {
	public static void main(String[] args) {
		BST st = new BST<String, String>();
		st.put("1", "one");
		st.put("2", "two");
		st.put("3", "three");
		st.put("4", "four");
		st.put("5", "five");
		//StdOut.print(st.get("6"));
		for(Object k : st.keys()){ // Object? not String?
			StdOut.println(k);
		}
	}
}
