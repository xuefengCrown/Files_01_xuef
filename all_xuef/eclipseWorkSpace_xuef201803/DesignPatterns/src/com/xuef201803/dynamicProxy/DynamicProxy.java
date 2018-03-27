package com.xuef201803.dynamicProxy;

import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;
import java.lang.reflect.Proxy;

/**
 * JDK ��̬����
 * ; ȱ��: �޷�����û���κνӿڵ���
 * @author moveb
 *
 */
public class DynamicProxy implements InvocationHandler {

	private Object target; // ����������
	public DynamicProxy(Object target){
		this.target = target;
	}
	@Override
	public Object invoke(Object proxy, Method method, Object[] args)
			throws Throwable {
		before();
		Object result = method.invoke(target, args);
		after();
		return result;
	}
	/**
	 * ���ش�����ʵ��
	 * @return
	 */
	@SuppressWarnings("unchecked")
	public <T> T getProxy(){
		return (T) Proxy.newProxyInstance(target.getClass().getClassLoader(), 
				target.getClass().getInterfaces(), // �����Ǳ�������������нӿ�
				this);
	}
	public void before(){
		System.out.println("before...");
	}
	
	public void after(){
		System.out.println("after...");
	}
}