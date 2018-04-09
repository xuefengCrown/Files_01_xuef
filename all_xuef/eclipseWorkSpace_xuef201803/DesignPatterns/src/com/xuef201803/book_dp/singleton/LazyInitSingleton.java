package com.xuef201803.book_dp.singleton;

public class LazyInitSingleton {
	// 体现了缓存的思想; 这个属性就是用来缓存实例的
	private volatile static LazyInitSingleton singleton = null;
	// 构造器 私有化
	private LazyInitSingleton(){}
	
	// 其实只有第一次也即对象为空时，才有必要加锁
	/*
	public synchronized static LazyInitSingleton getInstance(){
		if(singleton==null){
			singleton = new LazyInitSingleton();
		}
		return singleton;
	}*/
	
	public static LazyInitSingleton getInstance(){
		// 为空时，才执行同步代码
		if(singleton==null){
			synchronized(LazyInitSingleton.class){
				if(singleton==null)
					singleton = new LazyInitSingleton();
			}
		}
		
		return singleton;
	}
}
