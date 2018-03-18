package com.xuef2018.bookstore.test;

import static org.junit.Assert.*;

import org.junit.Test;

import com.xuef2018.bookstore.dao.BaseDao;

public class TestBaseDao {

	@Test
	public void testInsert() {
		String sql = "insert into userinfo(userid, username, accountid)"
				+ " values(?, ?, ?)";
		BaseDao bd = new BaseDao<>();
		long insertId = bd.insert(sql, 7, "xuef", 1);
		System.out.println("insertId " + insertId);
	}

}
