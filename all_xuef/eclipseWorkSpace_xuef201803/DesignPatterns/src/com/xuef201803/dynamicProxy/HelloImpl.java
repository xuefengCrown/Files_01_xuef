package com.xuef201803.dynamicProxy;

public class HelloImpl implements Hello {

	@Override
	public void say(String name) {
		System.out.println("hello " + name + "-_-");
	}

}
