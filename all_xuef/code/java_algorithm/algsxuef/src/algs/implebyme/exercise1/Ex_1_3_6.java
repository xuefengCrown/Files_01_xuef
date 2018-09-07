package algs.implebyme.exercise1;

import algs.base.StdOut;
import algs.implebyme.Queue;
import algs.implebyme.Statck_byLinkedList;
//reverse the order of the queue q
public class Ex_1_3_6 {

	public static void main(String[] args) {
		Queue<Integer> q = new Queue<>();
		Statck_byLinkedList<Integer> stack = new Statck_byLinkedList<>();
		
		q.enqueue(1);
		q.enqueue(2);
		q.enqueue(3);
		while (!q.isEmpty())
			stack.push(q.dequeue());
		while (!stack.isEmpty())
			q.enqueue(stack.pop());
		StdOut.println(q.dequeue());
		StdOut.println(q.dequeue());
		StdOut.println(q.dequeue());
	}

}
