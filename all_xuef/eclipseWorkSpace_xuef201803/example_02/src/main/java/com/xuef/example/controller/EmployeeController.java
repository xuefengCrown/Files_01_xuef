package com.xuef.example.controller;

import java.util.List;
import java.util.Map;

import org.smart4j.framework.annotation.Action;
import org.smart4j.framework.annotation.Controller;
import org.smart4j.framework.annotation.Inject;
import org.smart4j.framework.bean.Data;
import org.smart4j.framework.bean.Param;
import org.smart4j.framework.bean.View;

import com.xuef.example.domain.Employee;
import com.xuef.example.service.EmployeeService;

/**
 * ����Ա�������������
 * @author moveb
 */
@Controller
public class EmployeeController {
	@Inject
	private EmployeeService employeeService;
	
	/**
	 * ����Ա���б�ҳ��
	 * @param param
	 * @return
	 */
	@Action("get:/emps")
	public View index(Param param){
		List<Employee> empList = employeeService.getEmpList();
		return new View("emps.jsp").addModel("emp-list", empList);
	}
	
	/**
	 * ��ʾԱ����ϸ��Ϣ
	 * @param param
	 * @return
	 */
	@Action("get:/emp_show")
	public View show(Param param){
		long id = param.getLong("id");
		Employee emp = employeeService.getEmp(id);
		return new View("emp-detail.jsp").addModel("emp", emp);
	}
	
	/**
	 * ����Ա������ ҳ��
	 * @param param
	 * @return
	 */
	@Action("get:/emp_create")
	public View create(Param param){
		return new View("emp-create.jsp");
	}
	
	/**
	 * ���� ����Ա�� ����
	 * @param param
	 * @return
	 */
	@Action("post:/emp_create")
	public Data createSubmit(Param param){
		Map<String, Object> fieldMap = param.getMap();
		boolean result = employeeService.createEmp(fieldMap);
		
		// ��ͨ����£��ɷ���JSPҳ��; �� Ajax����ʱ����Ҫ����JSON����
		return new Data(result);
	}
}