package algs.implebyme;

import algs.base.StdIn;
import algs.base.StdOut;
//因为表达式的特殊结构，（每次运算都加了括号）所以程序逻辑才这么简单
public class InfixToPostfix {
	public static void main(String[] args) {
		Statck_byLinkedList<String> stack = new Statck_byLinkedList<String>();
        while (!StdIn.isEmpty()) {
            String s = StdIn.readString();
            if      (s.equals("+")) stack.push(s);
            else if (s.equals("*")) stack.push(s);
            else if (s.equals(")")) StdOut.print(stack.pop() + " ");
            else if (s.equals("(")) StdOut.print("");
            else                    StdOut.print(s + " ");
        }
        StdOut.println();
    }
}
