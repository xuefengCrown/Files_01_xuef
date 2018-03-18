package com.xuef2018.bookstore.test;

import static org.junit.Assert.*;

import org.junit.Test;

import com.xuef2018.bookstore.dao.AccountDAO;
import com.xuef2018.bookstore.dao.impl.AccountDaoImpl;

public class TestAccountDao {
	private AccountDAO accountDao = new AccountDaoImpl();
	@Test
	public void testGetBook() {
		accountDao.updateBalance(1, 120);;
	}

}
