package com.xuef.example.domain;

import java.util.Date;

public class Employee {
	private Integer eNo;

    private String eName;

    private String eGender;

    private Integer deptNo;

    private String eJob;

    private Short eSalary;

    private Date hiredate;
    private Department department;
	public Integer geteNo() {
		return eNo;
	}
	public void seteNo(Integer eNo) {
		this.eNo = eNo;
	}
	public String geteName() {
		return eName;
	}
	public void seteName(String eName) {
		this.eName = eName;
	}
	public String geteGender() {
		return eGender;
	}
	public void seteGender(String eGender) {
		this.eGender = eGender;
	}
	public Integer getDeptNo() {
		return deptNo;
	}
	public void setDeptNo(Integer deptNo) {
		this.deptNo = deptNo;
	}
	public String geteJob() {
		return eJob;
	}
	public void seteJob(String eJob) {
		this.eJob = eJob;
	}
	public Short geteSalary() {
		return eSalary;
	}
	public void seteSalary(Short eSalary) {
		this.eSalary = eSalary;
	}
	public Date getHiredate() {
		return hiredate;
	}
	public void setHiredate(Date hiredate) {
		this.hiredate = hiredate;
	}
	public Department getDepartment() {
		return department;
	}
	public void setDepartment(Department department) {
		this.department = department;
	}
	@Override
	public String toString() {
		return "Employee [eNo=" + eNo + ", eName=" + eName + ", eGender="
				+ eGender + ", deptNo=" + deptNo + ", eJob=" + eJob
				+ ", eSalary=" + eSalary + ", hiredate=" + hiredate
				+ ", department=" + department + "]";
	}
    
}
