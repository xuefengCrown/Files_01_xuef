package com.xuef.architect.customermgr.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Service;

import com.xuef.architect.common.service.BaseService;
import com.xuef.architect.customermgr.dao.CustomerDAO;
import com.xuef.architect.customermgr.vo.CustomerModel;
import com.xuef.architect.customermgr.vo.CustomerQueryModel;

@Service
public class CustomerService extends 
	BaseService<CustomerModel, CustomerQueryModel> implements ICustomerService {
	
	private CustomerDAO customerDAO;
	
	public CustomerService(){
		System.out.println("CustomerService construct...");
	}
	
	/**
	 * @Autowired 标在这里，没搞懂! Spring 还是没理解啊
	 * @param customerDAO
	 */
	@Autowired // 默认应该是根据类型注入
	public void setCustomerDAO(@Qualifier("customerDAO")CustomerDAO customerDAO) {
		System.out.println("Set CustomerDAO");
		this.customerDAO = customerDAO;
		super.setBaseDAO(customerDAO);
	}
}
