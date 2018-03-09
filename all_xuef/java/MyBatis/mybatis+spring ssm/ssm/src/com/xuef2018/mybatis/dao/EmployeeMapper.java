package com.xuef2018.mybatis.dao;

import java.util.List;

import com.xuef2018.mybatis.beans.Employee;

public interface EmployeeMapper {
	// 接口规定的方法有更强的类型检查(返回值和参数)
	// 接口是个规范，至于其实现，你可以用 hibernate，或mybatis
	// 接口与实现分离，方便开发和维护
	public Employee getEmployeeById(Integer id);
	public List<Employee> getEmps();
	public Integer addEmployee(Employee e);
	
	public Integer updateEmployee(Employee e);
	
	public Integer deleteEmployeeById(Employee e);
}
