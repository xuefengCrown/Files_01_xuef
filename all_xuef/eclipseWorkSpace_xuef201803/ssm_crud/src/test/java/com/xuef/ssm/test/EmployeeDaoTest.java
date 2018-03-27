package com.xuef.ssm.test;

import java.util.List;

import org.junit.Before;
import org.junit.Test;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

import com.xuef.ssm.dao.DepartmentMapper;
import com.xuef.ssm.dao.EmployeeMapper;
import com.xuef.ssm.domain.Department;
import com.xuef.ssm.domain.Employee;
import com.xuef.ssm.domain.EmployeeExample;

public class EmployeeDaoTest {
	private ApplicationContext ioc;
	private EmployeeMapper employeeMapper;
	private DepartmentMapper departmentMapper;
	@Before
	public void init(){
		// ��ȡIOC����
		ioc = new ClassPathXmlApplicationContext("applicationContext.xml");
		// �õ�mapper��ʵ��
		employeeMapper = ioc.getBean(EmployeeMapper.class);
		departmentMapper = ioc.getBean(DepartmentMapper.class);
	}
	@Test
	public void testselectByExample() {
		// ??? EmployeeExample ��ôʹ��
		List<Employee> list = employeeMapper.selectByExample(new EmployeeExample());
		System.out.println(list);
	}
	@Test
	public void test(){
		List<Department> list = departmentMapper.selectByExample(null);
		System.out.println(list);
	}
	@Test
	public void test1(){
		Employee e = employeeMapper.selectByPrimaryKey(1001);
		System.out.println(e);
	}
}