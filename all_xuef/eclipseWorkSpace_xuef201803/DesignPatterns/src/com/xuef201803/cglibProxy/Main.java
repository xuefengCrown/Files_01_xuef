package com.xuef201803.cglibProxy;

import com.xuef201803.dynamicProxy.Hello;
import com.xuef201803.dynamicProxy.HelloImpl;

public class Main {
	public static void main(String[] args) {
		Hello helloProxy = CGLibProxy.
				getInstance().
				getProxy(HelloImpl.class);
		helloProxy.say("Rose");
	}
}
