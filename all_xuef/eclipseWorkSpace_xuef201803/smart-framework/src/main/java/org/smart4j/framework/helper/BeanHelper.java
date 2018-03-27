package org.smart4j.framework.helper;

import java.util.HashMap;
import java.util.Map;
import java.util.Set;

import org.smart4j.framework.utils.ReflectionUtil;

/**
 * �൱��һ�� Bean ����
 * @author moveb
 *
 */
public class BeanHelper {
	/**
	 * ���� Bean ӳ�䣨���ڴ�� Bean ���� Bean ʵ����ӳ���ϵ��
	 */
	private static final Map<Class<?>, Object> BEAN_MAP=
			new HashMap<Class<?>, Object>();
	static{
		Set<Class<?>> beanClassSet = ClassHelper.getBeanClassSet();
		for(Class<?> beanClass:beanClassSet){
			Object object = ReflectionUtil.newInstance(beanClass);
			BEAN_MAP.put(beanClass, object);
		}
	}
	/**
	 * ��ȡ Bean ӳ��
	 * @return
	 */
	public static Map<Class<?>, Object> getBeanMap(){
		return BEAN_MAP;
	}
	/**
	 * ��ȡ Bean ʵ��
	 * @param cls
	 * @return
	 */
	@SuppressWarnings("unchecked")
	public static <T> T getBean(Class<T> cls){
		if(!BEAN_MAP.containsKey(cls)){
			throw new RuntimeException("can not get bean by class: "+cls);
		}
		return (T) BEAN_MAP.get(cls);
	}
}