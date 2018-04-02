package com.xuef201803.cglibProxy;

import java.lang.reflect.Method;

import net.sf.cglib.proxy.Enhancer;
import net.sf.cglib.proxy.MethodInterceptor;
import net.sf.cglib.proxy.MethodProxy;

public class CGLibProxy implements MethodInterceptor {
	/**
	 * CGLibProxy 是单例的
	 */
	private static CGLibProxy cgproxy = new CGLibProxy();
	public CGLibProxy() {}
	public static CGLibProxy getInstance(){
		return cgproxy;
	}

	@SuppressWarnings("unchecked")
	public <T> T getProxy(Class<?> cls){
		return (T)Enhancer.create(cls, this);
	}

	/**
	 * 横切逻辑
	 * obj ?
	 * method ?
	 * args 参数列表
	 * proxy ?
	 */
	@Override
	public Object intercept(Object obj, Method method, Object[] args,
			MethodProxy proxy) throws Throwable {
		before();
		Object result = proxy.invokeSuper(obj, args);
		after();
		return result;
	}

	public void before(){
		System.out.println("before...");
	}
	
	public void after(){
		System.out.println("after...");
	}
}
