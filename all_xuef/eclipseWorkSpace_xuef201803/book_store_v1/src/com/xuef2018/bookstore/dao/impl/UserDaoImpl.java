package com.xuef2018.bookstore.dao.impl;

import com.xuef2018.bookstore.dao.BaseDao;
import com.xuef2018.bookstore.dao.UserDAO;
import com.xuef2018.bookstore.domain.User;

public class UserDaoImpl extends BaseDao<User> implements UserDAO{
	@Override
	public User getUser(String username) {
		String sql = "select userid, username, accountid from"
				+ " userinfo where username = ?";
		User user = query(sql, username);
		return user;
	}

}
