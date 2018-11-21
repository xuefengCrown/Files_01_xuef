package com.xuef.scm;

import java.util.HashMap;
import java.util.Map;

/**
 * Environments allow you to look up the value of a variable, given its name.
 * Keep a list of variables and values, and a pointer to the parent environment.
 * If a variable list ends in a symbol rather than null, it means that symbol is
 * bound to the remainder of the values list.
 * 
 * @author Peter Norvig, peter@norvig.com http://www.norvig.com Copyright 1998
 *         Peter Norvig, see http://www.norvig.com/license.html
 */

public class Frame extends SchemeUtils {
	/**
	 * bindings is a dictionary that maps Scheme symbol keys (represented as Java Strings) to Scheme values.
	 * parent is the parent Frame instance. The parent of the Global Frame is None.
	 */
	public Map<String, Object> bindings;
	public Frame parent;

	public Frame(Frame parent) {
		this.bindings = new HashMap<>();
		this.parent = parent;
	}
	
	public Frame(Map<String, Object> bindings, Frame parent){
		this.bindings = bindings;
		this.parent = parent;
	}
	/** 
	 * Construct an empty environment: no bindings. 
	 */
	public Frame() {}
	/**
	 * 
	 * @param vars (a Pair)
	 * @param vals (a Pair)
	 * @param parent
	 */
	public Frame(Object vars, Object vals, Frame parent){
		/**
		 * 这里的 formals 是一个 Pair, 而Frame的bindings 却是一个 Map, 于是不得不来回转换, 很麻烦!
		 */
		// binding formal parameters to argument values
		Map<String, Object> formal_valList = new HashMap<String, Object>();
		Object restFormals = vars;
		Object restArgs = vals;
		while(restFormals != null){
			formal_valList.put((String)first(restFormals), first(restArgs));
			restFormals = rest(restFormals);
			restArgs = rest(restArgs);
		}
		this.bindings = formal_valList;
		this.parent = parent;
	}

	/** 
	 * Return the value bound to SYMBOL. Errors if SYMBOL is not found.
	 * Hint: 
	 * 	Recall that an environment is defined as a frame, its parent frame,
     * 	and all its ancestor frames, including the Global Frame. Therefore
	 */
	public Object lookup(String symbol) {
		if(this.bindings.containsKey(symbol)){
			return this.bindings.get(symbol);
		}
		// If not, try to look for the parent
		if (parent != null)
			return parent.lookup(symbol);
		else
			return error("Unbound variable: " + symbol);
	}
	/**
	 * define takes a symbol (represented by a Java string) && value 
	 * and binds the value to that symbol in the frame.
	 */
	public String define(String symbol, Object val){
		this.bindings.put(symbol, val);
		if(val instanceof Procedure){
			((Procedure)val).name = "#[" + symbol + "]";
		}
		return "#[" + symbol + "]";
	}
	
	public Frame defPrim(String name, int id, int minArgs) {
		define(name, new Primitive(id, minArgs, minArgs));
		return this;
	}

	/**
	 * 将基本过程注册进当前环境
	 * 
	 * 对于 可以把函数当做对象(函数作为第一级元素)的语言来说(如 Scheme, Python),
     * 将 函数 + 注册进环境 globalEnv 中， 只需要添加一个 '+'-->#[+] 的绑定即可;
     * Java中如何做?
	 * @param name: primitive-procedure name
	 * @param id: 过程 id
	 * @param minArgs: 参数个数最小值 
	 * @param maxArgs:
	 * @return
	 */
	public Frame defPrim(String name, int id, int minArgs, int maxArgs) {
		define(name, new Primitive(id, minArgs, maxArgs));
		return this;
	}
}
