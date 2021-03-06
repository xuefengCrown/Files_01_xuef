package org.smart4j.framework.annotation;

import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

@Target(ElementType.METHOD) // 加在方法上
@Retention(RetentionPolicy.RUNTIME)
public @interface Action {
	/**
	 * 请求类型与路径
	 */
	String value();
}
