package org.smart4j.framework.helper;

import java.util.HashSet;
import java.util.Set;

import org.smart4j.framework.annotation.Controller;
import org.smart4j.framework.annotation.Service;
import org.smart4j.framework.utils.ClassUtil;
import org.smart4j.framework.utils.ConfigHelper;
/**
 * 获取所加载的类;
 * @author moveb
 *
 */
public class ClassHelper {
	/**
	 * 定义类集合（用于存放所加载的类）
	 */
	private static final Set<Class<?>> CLASS_SET;
	static{
		String basePackage = ConfigHelper.getAppBasePackage();
		System.out.println("basePackage: " + basePackage);
		CLASS_SET = ClassUtil.getClassSet(basePackage);
	}
	/**
	 * 获取应用包下的所有类
	 * @return
	 */
	public static Set<Class<?>> getClassSet(){
		return CLASS_SET;
	}
	/**
	 * 获取包下的所有Service类
	 * @return
	 */
	public static Set<Class<?>> getServiceClassSet(){
		Set<Class<?>> classSet = new HashSet<Class<?>>();
		for(Class<?> cls:CLASS_SET){
			if(cls.isAnnotationPresent(Service.class)){
				classSet.add(cls);
			}
		}
		return classSet;
	}
	public static Set<Class<?>> getControllerClassSet(){
		Set<Class<?>> classSet = new HashSet<Class<?>>();
		for(Class<?> cls:CLASS_SET){
			if(cls.isAnnotationPresent(Controller.class)){
				classSet.add(cls);
			}
		}
		return classSet;
	}
	/**
	 * 获取应用包名下所有Bean类（包括： Service, Controller）
	 * @return
	 */
	public static Set<Class<?>> getBeanClassSet(){
		Set<Class<?>> beanClassSet = new HashSet<Class<?>>();
		beanClassSet.addAll(getServiceClassSet());
		beanClassSet.addAll(getControllerClassSet());
		return beanClassSet;
	}
}
