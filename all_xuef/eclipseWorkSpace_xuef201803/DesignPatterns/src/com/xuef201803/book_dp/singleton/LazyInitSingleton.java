package com.xuef201803.book_dp.singleton;

public class LazyInitSingleton {
	// �����˻����˼��; ������Ծ�����������ʵ����
	private volatile static LazyInitSingleton singleton = null;
	// ������ ˽�л�
	private LazyInitSingleton(){}
	
	// ��ʵֻ�е�һ��Ҳ������Ϊ��ʱ�����б�Ҫ����
	/*
	public synchronized static LazyInitSingleton getInstance(){
		if(singleton==null){
			singleton = new LazyInitSingleton();
		}
		return singleton;
	}*/
	
	public static LazyInitSingleton getInstance(){
		// Ϊ��ʱ����ִ��ͬ������
		if(singleton==null){
			synchronized(LazyInitSingleton.class){
				if(singleton==null)
					singleton = new LazyInitSingleton();
			}
		}
		
		return singleton;
	}
}