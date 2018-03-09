package com.xuef2018.mybatis.controller;

import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

import com.xuef2018.mybatis.beans.Employee;
import com.xuef2018.mybatis.service.EmployeeService;

@Controller
public class EmployeeController {
	@Autowired
	EmployeeService employeeService;
	
	@RequestMapping("/emps")
	public String emps(Map<String, Object> map){
		List<Employee> emps = employeeService.getEmps();
		map.put("allemp", emps);
		return "list";
	}
}
