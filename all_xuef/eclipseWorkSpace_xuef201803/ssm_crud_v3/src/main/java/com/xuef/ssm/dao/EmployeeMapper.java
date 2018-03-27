package com.xuef.ssm.dao;

import java.util.List;

import com.xuef.ssm.domain.Employee;

public interface EmployeeMapper {
	/**
	 * 根据员工ID搜索
	 * @param empId
	 * @return
	 */
	public Employee getEmpById(Integer empId);
	/**
	 * 返回所有员工
	 * @return
	 */
	public List<Employee> getEmps();
}
