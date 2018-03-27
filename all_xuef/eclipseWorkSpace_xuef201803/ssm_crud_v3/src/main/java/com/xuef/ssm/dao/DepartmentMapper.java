package com.xuef.ssm.dao;

import java.util.List;

import com.xuef.ssm.domain.Department;

public interface DepartmentMapper {
	public Department getDeptById(Integer deptNo);
	
	public List<Department> getDepts();
}
