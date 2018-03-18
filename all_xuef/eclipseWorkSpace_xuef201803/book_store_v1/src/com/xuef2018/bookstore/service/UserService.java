package com.xuef2018.bookstore.service;

import com.xuef2018.bookstore.dao.UserDAO;
import com.xuef2018.bookstore.dao.impl.UserDaoImpl;
import com.xuef2018.bookstore.domain.User;

public class UserService {
	private UserDAO userDaoImpl = new UserDaoImpl();
	public User getUser(String username) {
		return userDaoImpl.getUser(username);
	}

}
