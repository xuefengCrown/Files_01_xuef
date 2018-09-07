package algs.implebyme.exercise1;

import algs.base.StdOut;
import algs.implebyme.Statck_byLinkedList;

public class Ex_1_3_4_Parentheses {
	public static void main(String[] args) {
		StdOut.println(isParenthes("[()]{}{[()()]()}"));
		StdOut.println(isParenthes("[(]) "));
	}
	public static boolean isParenthes(String s){
		Statck_byLinkedList<Character> stack = new Statck_byLinkedList<>();
		char[] ca = s.toCharArray();
		
		for (char c:ca){
			//StdOut.println(c);
			if(c=='(' || c=='[' || c=='{') stack.push(c);
			else if(c==')'){
				if(!stack.isEmpty() && stack.pop()== '(') ;
				else return false;
			}else if(c==']'){
				if(!stack.isEmpty() && stack.pop()== '[') ;
				else return false;
			}else if(c=='}'){
				if(!stack.isEmpty() && stack.pop()== '{') ;
				else return false;
			}
		}
		return true;
	}
}
