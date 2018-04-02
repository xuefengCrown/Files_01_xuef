package org.smart4j.framework.proxy;

import java.lang.reflect.Method;
/**
 * 切面代理
 * @author moveb
 *
 */
public abstract class AspectProxy implements Proxy {
	
	@Override
	public Object doProxy(ProxyChain proxyChain) throws Throwable {
		Object result = null;
		
		// 目标类
		Class<?> cls = proxyChain.getTargetClass();
		// 目标方法
		Method method = proxyChain.getTargetMethod();
		// 方法参数
		Object[] params = proxyChain.getMethodParams();
		
		begin();
		
		// 实现调用框架
		try{
			if(intercept(cls, method, params)){
				// 依次执行 每个before
				before(cls, method, params);
				
				// 代理链 使得一个目标类可以有多个切面（代理对象），增强了框架的功能
				result = proxyChain.doProxyChain();
				
				// 依次执行 每个after
				after(cls, method, params, result);
			}else{
				result = proxyChain.doProxyChain();
			}
		} catch(Exception e){
			throw e;
		} finally{
			end();
		}
		return result;
	}
	public void begin(){
		
	}
	
	public boolean intercept(Class<?> clz, Method method, 
			Object[] params) throws Throwable{
		return true;
	}
	public void before(Class<?> clz, Method method, 
			Object[] params) throws Throwable{
		
	}
	
	public void after(Class<?> clz, Method method, 
			Object[] params, Object result) throws Throwable{
		
	}
	public void error(Class<?> clz, Method method, 
			Object[] params) throws Throwable{
		
	}
	public void end(){
		
	}
}
