package org.smart4j.framework.proxy;

import java.lang.reflect.Method;
import java.util.List;

import net.sf.cglib.proxy.Enhancer;
import net.sf.cglib.proxy.MethodInterceptor;
import net.sf.cglib.proxy.MethodProxy;

/**
 * 代理管理器(切面类调用)
 * 
 * @author moveb
 *
 */
public class ProxyManager {
	/**
	 * 创建代理对象
	 * 
	 * 输入一个目标类和一组Proxy接口实现，输出一个代理对象
	 * 
	 * @param targetClass
	 * @param proxyList
	 * @return
	 */
	@SuppressWarnings("unchecked")
	public static <T> T createProxy(final Class<?> targetClass,
			final List<Proxy> proxyList){
		return (T)Enhancer.create(targetClass, new MethodInterceptor() {
			
			// 何时这个方法被调用? 
			// 目标方法被调用时，会转到代理对象，调用这个方法???
			@Override
			public Object intercept(Object targetObject, 
									Method targetMethod, 
									Object[] methodParams,
									MethodProxy methodProxy) throws Throwable {
				// 切面类(代理对象)的调用逻辑、次序 在这里
				// 切面动作的 切入点
				// 很多切面被封装在 代理链(ProxyChain)中，然后包在cglib生成的代理对象中
				// 最后就是一个 targetClass 对应一个 proxy
				return new ProxyChain(targetClass, targetObject, 
									  targetMethod, methodProxy, 
									  methodParams, proxyList)
							.doProxyChain();
			}
		});
	}
}
