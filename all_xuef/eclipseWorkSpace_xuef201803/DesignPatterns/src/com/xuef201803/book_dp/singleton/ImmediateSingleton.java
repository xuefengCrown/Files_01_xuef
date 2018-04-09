package com.xuef201803.book_dp.singleton;

public class ImmediateSingleton {
	// static 变量在类装载的时候进行初始化
	private static ImmediateSingleton singleton = 
			new ImmediateSingleton();
	
	private ImmediateSingleton(){}
	
	public static ImmediateSingleton getInsance(){
		return singleton;
	}
}
