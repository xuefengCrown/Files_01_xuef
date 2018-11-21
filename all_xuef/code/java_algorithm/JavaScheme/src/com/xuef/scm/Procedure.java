package com.xuef.scm;

/**
 * @author Peter Norvig, peter@norvig.com http://www.norvig.com Copyright 1998
 *         Peter Norvig, see http://www.norvig.com/license.html
 **/

public abstract class Procedure extends SchemeUtils {

	public String name = "anonymous procedure";

	public String toString() {
		return "{" + name + "}";
	}

	/**
	 * 能被调用的(apply)对象就是一个 Procedure
	 * 至于过程的形式如何以及如何调用，可以自己定义;
	 * @param interpreter
	 * @param args
	 * @return
	 */
	public abstract Object apply(Scheme interpreter, Object args);

	/** 
	 * Coerces a Scheme object to a procedure. 
	 */
	static Procedure proc(Object x) {
		if (x instanceof Procedure)
			return (Procedure) x;
		else
			return proc(error("Not a procedure: " + stringify(x)));
	}

}
