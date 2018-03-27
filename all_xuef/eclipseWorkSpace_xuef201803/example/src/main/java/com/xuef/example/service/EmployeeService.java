package com.xuef.example.service;

import java.util.List;
import java.util.Map;

import org.smart4j.framework.annotation.Service;

import com.xuef.example.domain.Employee;

@Service
public class EmployeeService {
	public EmployeeService(){
		System.out.println("EmployeeService Construct...");
	}
	public List<Employee> getEmpList() {
		return null;
	}

	public Employee getEmp(long id) {
		return null;
	}

	public boolean createEmp(Map<String, Object> fieldMap) {
		return false;
	}

}
