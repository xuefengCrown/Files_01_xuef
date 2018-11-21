package com.xuef.scm;

/**
 * A Pair has two fields, first and rest (or car and cdr). The empty list is
 * represented by null. The methods that you might expect here, like first,
 * second, list, etc. are instead static methods in class SchemeUtils.
 * 
 * Pair 相当于 Scheme中的 cons, 它表示一个具有两个指针的盒子(car, cdr)
 * 几乎可以用来表示任意结构的数据, 其表达能力让人惊讶!
 * @author Peter Norvig, peter@norvig.com http://www.norvig.com Copyright 1998
 *         Peter Norvig, see http://www.norvig.com/license.html
 */

public class Pair extends SchemeUtils {

	/** The first element of the pair. **/
	public Object first;

	/** The other element of the pair. **/
	public Object rest;

	public Pair(Object first, Object rest) {
		this.first = first;
		this.rest = rest;
	}
	public Pair(){}

	/** 
	 * Two pairs are equal if their first and rest fields are equal. 
	 * pair1.equals(pair2)
	 */
	public boolean equals(Object x) {
		// 同一个对象(同一引用)
		if (x == this) return true;
		else if (!(x instanceof Pair))
			return false;
		else {
			Pair that = (Pair) x;
			// 在 SICP 中经常写这种递归函数
			return equal(this.first, that.first) && equal(this.rest, that.rest);
		}
	}
	/**
	 * Pair 内部构造的字符串形式
	 * @return
	 * xuef 180912
	 */
	public String repr4pair(){
		Object car = this.first;
		Object cdr = this.rest;
		
		String carStr = "nil";
		String cdrStr = "nil";
		if(car == null){
			;
		}else if(!(car instanceof Pair)){
			carStr = car.toString();
		}else{
			carStr = ((Pair)car).repr4pair();
		}
		
		if(cdr == null){
			;
		}else if(!(cdr instanceof Pair)){
			cdrStr = cdr.toString();
		}else{
			cdrStr = ((Pair)cdr).repr4pair();
		}
		return String.format("Pair(%s, %s)", carStr, cdrStr);
	}

	/** 
	 * Return a String representation of the pair. 
	 */
	public String toString() {
		return stringify(this, true);
	}

	/** 
	 * Build up a String representation of the Pair in a StringBuffer.
	 * 一种典型的返回值的方式: 通过改变对象的内容来传递值
	 *  buf 相当于对象指针，这是c语言中常见的返回值的方式
	 */
	void stringifyPair(boolean quoted, StringBuffer buf) {
		String special = null;
		if ((rest instanceof Pair) && rest(rest) == null)
			special = (first == "quote") ? "'" : (first == "quasiquote") ? "`"
					: (first == "unquote") ? ","
							: (first == "unquote-splicing") ? ",@" : null;

		if (special != null) {
			buf.append(special);
			stringify(second(this), quoted, buf);
		} else {
			buf.append('(');
			stringify(first, quoted, buf);
			Object tail = rest;
			while (tail instanceof Pair) {
				buf.append(' ');
				stringify(((Pair) tail).first, quoted, buf);
				tail = ((Pair) tail).rest;
			}
			if (tail != null) {
				buf.append(" . ");
				stringify(tail, quoted, buf);
			}
			buf.append(')');
		}
	}

}
