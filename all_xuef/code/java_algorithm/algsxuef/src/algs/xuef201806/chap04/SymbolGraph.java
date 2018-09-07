package algs.xuef201806.chap04;

import algs.base.In;
import algs.base.ST;

/**
 * 符号图的数据类型
 * @author moveb
 *
 */
public class SymbolGraph {
	private ST<String, Integer> st; // 符号名-->索引
	private String[] keys; // 索引-->符号名
	private UndirectGraph G; // 图
	/**
	 * @param stream
	 * @param sp 分隔符
	 */
	public SymbolGraph(String stream, String sp){
		st = new ST();
		In in = new In(stream);
		while(in.hasNextLine()){ // 构造索引
			String[] a = in.readLine().split(sp); // 读取字符串
			// 为每个不同的字符串关联一个索引
			for(int i=0; i<a.length; i++){
				if(!st.contains(a[i])){
					st.put(a[i], st.size());
				}
			}
		}
		keys = new String[st.size()];
		for(String name:st.keys()){
			keys[st.get(name)] = name;
		}
		G = new UndirectGraph(st.size());
		in = new In(stream);
		while(in.hasNextLine()){
			String[] a = in.readLine().split(sp);
			int v = st.get(a[0]);
			for(int i=1; i<a.length; i++){
				G.addEdge(v, st.get(a[i]));
			}
		}
	}
}
