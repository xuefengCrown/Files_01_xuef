package com.xuef2018.bookstore.dao;

import com.xuef2018.bookstore.domain.User;

public interface UserDao {
	/**
	 * 根据用户名查找
	 */
	public User getUser(String username);
}
