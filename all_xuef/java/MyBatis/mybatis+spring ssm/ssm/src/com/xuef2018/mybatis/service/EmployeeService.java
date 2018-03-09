package com.xuef2018.mybatis.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.xuef2018.mybatis.beans.Employee;
import com.xuef2018.mybatis.dao.EmployeeMapper;

@Service("employeeService")
public class EmployeeService {

	@Autowired
	private EmployeeMapper employeeMapper;
	
	public List<Employee> getEmps(){
		return employeeMapper.getEmps();
	}
}
