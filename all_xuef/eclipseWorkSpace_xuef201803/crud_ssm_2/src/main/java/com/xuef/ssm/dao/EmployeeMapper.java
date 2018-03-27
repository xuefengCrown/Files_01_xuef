package com.xuef.ssm.dao;

import com.xuef.ssm.domain.Employee;
import java.util.List;
import org.apache.ibatis.annotations.Param;

public interface EmployeeMapper {
    long countByExample(Employee example);

    int deleteByExample(Employee example);

    int deleteByPrimaryKey(Integer eNo);

    int insert(Employee record);

    int insertSelective(Employee record);

    List<Employee> selectByExample(Employee example);

    Employee selectByPrimaryKey(Integer eNo);
    
    List<Employee> selectByExampleWithDept(Employee example);

    Employee selectByPrimaryKeyWithDept(Integer eNo);

    int updateByExampleSelective(@Param("record") Employee record, @Param("example") Employee example);

    int updateByExample(@Param("record") Employee record, @Param("example") Employee example);

    int updateByPrimaryKeySelective(Employee record);

    int updateByPrimaryKey(Employee record);
}