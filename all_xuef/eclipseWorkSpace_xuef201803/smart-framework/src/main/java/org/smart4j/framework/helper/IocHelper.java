package org.smart4j.framework.helper;

import java.lang.reflect.Field;
import java.util.Collection;
import java.util.Map;

import org.apache.commons.collections.CollectionUtils;
import org.apache.commons.lang3.ArrayUtils;
import org.smart4j.framework.annotation.Inject;
import org.smart4j.framework.utils.ReflectionUtil;

/**
 * ����ע�� ������
 * ��ʱIocHelper �������Ķ��󻹶��ǵ�����
 * @author moveb
 *
 */
public class IocHelper {
	static{
		System.out.println("IocHelper static code...");
		// ��ȡ���е� Bean ���� Bean ʵ��֮���ӳ���ϵ����� Bean Map��
		Map<Class<?>, Object> beanMap = BeanHelper.getBeanMap();
		if(!beanMap.isEmpty()){
			// ���� Bean Map
			for(Map.Entry<Class<?>, Object> beanEntry:beanMap.entrySet()){
				// �� BeanMap �л�ȡBean����Beanʵ��
				Class<?> beanClass = beanEntry.getKey();
				Object beanInstance = beanEntry.getValue();
				// ��ȡBean�ඨ������г�Ա����
				Field[] fields = beanClass.getDeclaredFields();
				if(ArrayUtils.isNotEmpty(fields)){
					// ���� fields
					for(Field field:fields){
						// �ж���ǰBean Field �Ƿ����Injectע��
						if(field.isAnnotationPresent(Inject.class)){
							// ��BeanMap �л�ȡBean Field��Ӧ��ʵ��
							Class<?> beanFieldClass = field.getType();
							Object beanFieldInstance = beanMap.get(beanFieldClass);
							if(beanFieldInstance != null){
								// ͨ�������ʼ�� BeanField ��ֵ
								ReflectionUtil.setField(beanInstance, field, beanFieldInstance);
							}
						}
					}
				}
			}
		}
	}
}