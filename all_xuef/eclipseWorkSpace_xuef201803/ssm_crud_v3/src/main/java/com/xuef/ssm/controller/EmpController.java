package com.xuef.ssm.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestAttribute;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

import com.github.pagehelper.PageHelper;
import com.github.pagehelper.PageInfo;
import com.xuef.ssm.domain.Department;
import com.xuef.ssm.domain.Employee;
import com.xuef.ssm.domain.ResWithMSG;
import com.xuef.ssm.service.EmployeeService;

@Controller
public class EmpController {
	@Autowired
	private EmployeeService employeeService;
	
	public EmpController(){
		System.out.println("EmpController new......");
	}
	
	@ResponseBody // 返回数据自动转为JSON
	@RequestMapping("/emps")
	public ResWithMSG getEmpsJSON(
			@RequestParam(value="pageNo", defaultValue="1")Integer pageNo){
		PageHelper.startPage(pageNo, 3);
		List<Employee> emps = employeeService.getEmps();
		// 包装查询后的结果。只需要将 pageInfo交给页面就可以
		PageInfo pageInfo = new PageInfo(emps, 5);// 5为连续显示的页数
		ResWithMSG success = ResWithMSG.success().add("pageInfo", pageInfo);
		return success;
	}
	
	/**
	 * 修改后保存员工信息
	 * @param emp
	 * @return
	 */
	@ResponseBody
	@RequestMapping(value="/emp/{eNo}", method=RequestMethod.PUT)
	public ResWithMSG saveEmp(Employee emp){
		System.out.println("save emp: " + emp);
		employeeService.saveEmp(emp);
		return ResWithMSG.success();
	}
	/**
	 * 查询部门信息
	 * @return
	 */
	@ResponseBody // 返回数据自动转为JSON
	@RequestMapping("/depts")
	public ResWithMSG getDeptsJSON(){
		List<Department> depts = employeeService.getDepts();
		ResWithMSG success = ResWithMSG.success().add("depts", depts);
		return success;
	}
	/**
	 * 查询所有员工数据(分页)
	 * 使用 pageHelper 插件
	 * @return
	 */
	//@RequestMapping("/emps")
	public String getEmps(
			@RequestParam(value="pageNo", defaultValue="1")Integer pageNo,
			Model model){
		System.out.println("get /emps");
		PageHelper.startPage(pageNo, 3);
		List<Employee> emps = employeeService.getEmps();
		// 包装查询后的结果。只需要将 pageInfo交给页面就可以
		PageInfo pageInfo = new PageInfo(emps, 5);// 5为连续显示的页数
		model.addAttribute("pageInfo", pageInfo);
		return "emps-list";
	}
}
