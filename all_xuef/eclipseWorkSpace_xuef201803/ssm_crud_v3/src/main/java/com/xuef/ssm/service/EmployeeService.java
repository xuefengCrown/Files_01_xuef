package com.xuef.ssm.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.xuef.ssm.dao.DepartmentMapper;
import com.xuef.ssm.dao.EmployeeMapper;
import com.xuef.ssm.domain.Department;
import com.xuef.ssm.domain.Employee;

@Service("employeeService")
public class EmployeeService {
	public EmployeeService(){
		System.out.println("serveice new....");
	}
	
	@Autowired
	private EmployeeMapper employeeMapper;
	
	@Autowired
	private DepartmentMapper departmentMapper;
	public List<Employee> getEmps() {
		return employeeMapper.getEmps();
	}
	/**
	 * 查询所有部门
	 * @return
	 */
	public List<Department> getDepts() {
		return departmentMapper.getDepts();
	}

}
