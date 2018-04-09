package com.xuef201803.book_dp.simpleFactory;

/**
 * 对于客户端来说，只有工厂和接口是可见的。
 * @author moveb
 */
public class Client {
	public static void main(String[] args) {
		Api impl = SimpleFac.getInstance(2);
		impl.operate();
	}
}
