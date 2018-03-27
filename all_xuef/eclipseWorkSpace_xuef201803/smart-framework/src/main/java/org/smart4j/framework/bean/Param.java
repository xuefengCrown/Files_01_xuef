package org.smart4j.framework.bean;

import java.util.Map;

/**
 * 请求参数对象
 * @author moveb
 *
 */
public class Param {
	private Map<String, Object> paramMap;

	public Param(Map<String, Object> paramMap) {
		this.paramMap = paramMap;
	}
	/**
	 * 根据参数名获取 lonh 型参数值
	 * @param name
	 * @return
	 */
	public long getLong(String name){
		return (long) paramMap.get(name);
	}
	/**
	 * 获取所有字段信息
	 */
	public Map<String, Object> getMap(){
		return paramMap;
	}
}
