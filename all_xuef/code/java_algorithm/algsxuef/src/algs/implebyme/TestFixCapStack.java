package algs.implebyme;

import algs.base.StdOut;

public class TestFixCapStack {

	public static void main(String[] args) {
		//FixCapacityStack<String> s = new FixCapacityStack<>(20);
		Statck_byLinkedList<String> s = new Statck_byLinkedList<>();
		s.push("aaa");
		s.push("ccc");
		s.push("sss");
		StdOut.println(s.size());
		s.pop();
		s.pop();
		StdOut.println(s.pop());
		StdOut.print(s.pop());
	}

}
