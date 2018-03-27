package com.xuef2018.bookstore.dao.impl;

import com.xuef2018.bookstore.dao.AccountDAO;
import com.xuef2018.bookstore.domain.Account;

public class AccountDaoImpl extends BaseDao<Account> implements AccountDAO {

	@Override
	public Account get(Integer accountId) {
		String sql = "select accountid, balance from "
				+ " account where accountid = ?";
		return query(sql, accountId);
	}

	@Override
	public void updateBalance(Integer accountId, float amount) {
		String updateSql = "update account set balance = balance - "
				+ " ? where accountid = ?"; 
		update(updateSql, amount, accountId);
	}

}
