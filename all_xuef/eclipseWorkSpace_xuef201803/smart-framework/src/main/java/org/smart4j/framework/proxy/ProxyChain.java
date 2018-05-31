package org.smart4j.framework.proxy;

import net.sf.cglib.proxy.MethodProxy;
import java.lang.reflect.Method;
import java.util.ArrayList;
import java.util.List;

/**
 * ������
 * @author moveb
 */
public class ProxyChain {
	private final Class<?> targetClass;
	private final Object targetObject;
	private final Method targetMethod;
	private final MethodProxy methodProxy;
	private final Object[] methodParams;
	
	private List<Proxy> proxyList = new ArrayList<Proxy>();
	private int proxyIndex = 0;
	public ProxyChain(Class<?> targetClass, Object targetObject,
			Method targetMethod, MethodProxy methodProxy,
			Object[] methodParams, List<Proxy> proxyList) {
		super();
		this.targetClass = targetClass;
		this.targetObject = targetObject;
		this.targetMethod = targetMethod;
		this.methodProxy = methodProxy;
		this.methodParams = methodParams;
		this.proxyList = proxyList;
	}
	
	public Object doProxyChain() throws Throwable{
		Object methodResult;
		if(proxyIndex < proxyList.size()){
			methodResult = proxyList.get(proxyIndex++).doProxy(this);
		}else{
			// ִ��Ŀ�귽��
			methodResult = methodProxy.invokeSuper(targetObject, methodParams);
		}
		return methodResult;
	}
	public List<Proxy> getProxyList() {
		return proxyList;
	}
	public void setProxyList(List<Proxy> proxyList) {
		this.proxyList = proxyList;
	}
	public int getProxyIndex() {
		return proxyIndex;
	}
	public void setProxyIndex(int proxyIndex) {
		this.proxyIndex = proxyIndex;
	}
	public Class<?> getTargetClass() {
		return targetClass;
	}
	public Object getTargetObject() {
		return targetObject;
	}
	public Method getTargetMethod() {
		return targetMethod;
	}
	public MethodProxy getMethodProxy() {
		return methodProxy;
	}
	public Object[] getMethodParams() {
		return methodParams;
	}
}