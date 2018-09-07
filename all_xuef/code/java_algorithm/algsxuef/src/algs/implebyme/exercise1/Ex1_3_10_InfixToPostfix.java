package algs.implebyme.exercise1;

import algs.base.StdIn;
import algs.base.StdOut;
import algs.implebyme.Statck_byLinkedList;

// 中序表达式 转 后序
public class Ex1_3_10_InfixToPostfix {

	public static void main(String[] args) {
		//23 + 34 * 45 / 5 + 6
		infix2postfix();
	}
	//将中序表达式( 23 + 34 * 45 / ( 5 + 6 + 7 ) )转换成后序表达式23 34 45 * 5 6 + 7 + / +
	public static void infix2postfix(){
		Statck_byLinkedList<String> s2 = new Statck_byLinkedList<>();
		
		while (!StdIn.isEmpty())
		{ // Read token, push if operator.
			String s = StdIn.readString();
			if(s.equals("+") || s.equals("-")){
				while(true){
					if(s2.isEmpty()) {
						s2.push(s);
						break;
					}
					else {
						StdOut.print(s2.pop()+" ");
						//s2.push(s);
					}
				}
			}else if(s.equals("*") || s.equals("/")){
				while(true){
					if("*".equals(s2.peek())||"/".equals(s2.peek())){
						StdOut.print(s2.pop()+" ");
						//s2.push(s);
					}else {
						s2.push(s);
						break;
					}
				}
				
			}else StdOut.print(s +" ");
		}
		while(!s2.isEmpty()){
			StdOut.print(s2.pop());
		}
	}
}
