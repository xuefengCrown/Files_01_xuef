package com.xuef.ssm.dao;

import java.util.List;

import com.xuef.ssm.domain.Employee;

public interface EmployeeMapper {
	/**
	 * ����Ա��ID����
	 * @param empId
	 * @return
	 */
	public Employee getEmpById(Integer empId);
	/**
	 * ��������Ա��
	 * @return
	 */
	public List<Employee> getEmps();
}