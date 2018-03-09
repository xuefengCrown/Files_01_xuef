package com.xuef2018.mybatis.beans;

public class Employee {
	private int e_no;
	private String e_name;
	private char e_gender; // 0 female, 1 male
	private int dept_no;
	private String e_job;
	private float e_salary;
	private String hireDate;
	
	public static class Builder{
		private int e_no;
		private String e_name;
		private char e_gender; // 0 female, 1 male
		private int dept_no;
		private String e_job;
		private float e_salary;
		private String hireDate;
		
		public Builder(int e_no){
			this.e_no = e_no;
		}
		public Builder e_name(String val){
			e_name = val;
			return this;
		}
		/**
		 * @param val 0 female, 1 male
		 * @return
		 */
		public Builder e_gender(char val){
			e_gender = val;
			return this;
		}
		public Builder dept_no(int val){
			dept_no = val;
			return this;
		}
		public Builder e_job(String val){
			e_job = val;
			return this;
		}
		public Builder e_salary(float val){
			e_salary = val;
			return this;
		}
		public Builder hireDate(String val){
			hireDate = val;
			return this;
		}
		public Employee build(){
			return new Employee(this);
		}
	}
	private Employee(Builder builder){
		e_no = builder.e_no;
		e_name = builder.e_name;
		e_gender = builder.e_gender;
		dept_no = builder.dept_no;
		e_job = builder.e_job;
		e_salary = builder.e_salary;
		hireDate = builder.hireDate;
	}
	// 无参构造器
	public Employee(){}
	
	public int getE_no() {
		return e_no;
	}
	public void setE_no(int e_no) {
		this.e_no = e_no;
	}
	public String getE_name() {
		return e_name;
	}
	public void setE_name(String e_name) {
		this.e_name = e_name;
	}
	public char getE_gender() {
		return e_gender;
	}
	public void setE_gender(char e_gender) {
		this.e_gender = e_gender;
	}
	public int getDept_no() {
		return dept_no;
	}
	public void setDept_no(int dept_no) {
		this.dept_no = dept_no;
	}
	public String getE_job() {
		return e_job;
	}
	public void setE_job(String e_job) {
		this.e_job = e_job;
	}
	public float getE_salary() {
		return e_salary;
	}
	public void setE_salary(float e_salary) {
		this.e_salary = e_salary;
	}
	
	public String getHireDate() {
		return hireDate;
	}

	public void setHireDate(String hireDate) {
		this.hireDate = hireDate;
	}

	@Override
	public String toString() {
		return "Employee [e_no=" + e_no + ", e_name=" + e_name + ", e_gender="
				+ e_gender + ", dept_no=" + dept_no + ", e_job=" + e_job
				+ ", e_salary=" + e_salary + ", hireDate=" + hireDate + "]";
	}
	
}
