package algs.xuef201806.chap05.re;

import algs.base.Bag;
import algs.base.Digraph;
import algs.base.DirectedDFS;
import algs.xuef201806.chap01.Stack;

/**
 * 非确定有限状态自动机 实现的正则表达式引擎
 * 
 * 一个正则表达式 === 表示re的字母表(匹配转换) + 有向图(epsilon转换)
 * @author moveb
 *
 */
public class NFA {
	private char[] re; // 匹配转换
	private Digraph G; // epsilon 转换
	private int M; // 状态数量
	
	// 根据给定的正则表达式构造NFA
	public NFA(String regexp){
		// 保存左括号和"或"运算符的索引的栈
		Stack<Integer> ops = new Stack<Integer>();
		re = regexp.toCharArray();
		M = re.length;
		// 有向图, 来表示epsilon转换; 为什么 M+1个结点
		G = new Digraph(M+1);
		
		for(int i=0; i<M; i++){
			int lp = i;
			if(re[i] == '(' || re[i] == '|')
				ops.push(i);
			else if(re[i] == ')'){
				int or = ops.pop();
				if(re[or] == '|'){
					lp = ops.pop();
					G.addEdge(lp, or+1);
					G.addEdge(or, i);
				}else{ // 如re[or]=='(' 说明遇到闭包表达式
					lp = or;
				}
			}
			// 单字符的闭包 or 闭包表达式
			if(i < M-1 && re[i+1] == '*'){ // lookahead
				G.addEdge(lp, i+1);
				G.addEdge(i+1, lp);
			}
			if(re[i] == '(' || re[i] == '*' || re[i] == ')')
				G.addEdge(i, i+1);
		}
	}
	/**
	 * 使用NFA模拟的模式匹配
	 * @param txt
	 * @return
	 */
	public boolean recognizes(String txt){
		// Does the NFA recognize txt?
		Bag<Integer> pc = new Bag<Integer>();
		DirectedDFS dfs = new DirectedDFS(G, 0);
		// 从起始状态(0)开始通过epsilon转换能够到达的所有状态的集合
		for (int v = 0; v < G.V(); v++)
			if (dfs.marked(v)) pc.add(v);
		
		// 遍历文本串
		for (int i = 0; i < txt.length(); i++){ 
			// Compute possible NFA states for txt[i+1].
			Bag<Integer> match = new Bag<Integer>();
			/**
			 * pc包含前一状态的集合(最初是起始状态的集合);
			 * 下面操作得到的是: 匹配 txt.charAt(i)之后能到达的状态的集合(match);
			 */
			for (int v : pc)
				if (v < M)
					if (re[v] == txt.charAt(i) || re[v] == '.')
						match.add(v+1);
			
			// 清空 pc
			pc = new Bag<Integer>();
			// 匹配 txt.charAt(i)之后通过epsilon转换能够到达的所有状态的集合
			dfs = new DirectedDFS(G, match);
			for (int v = 0; v < G.V(); v++)
				if (dfs.marked(v)) pc.add(v);
		}
		for (int v : pc) 
			if (v == M) return true;
		
		return false;
	}
}
