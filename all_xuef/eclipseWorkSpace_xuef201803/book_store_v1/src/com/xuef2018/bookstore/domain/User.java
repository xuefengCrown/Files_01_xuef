package com.xuef2018.bookstore.domain;

public class User {
	private int userid;
	private String username;
	private int accountid;
	public int getUserid() {
		return userid;
	}
	public void setUserid(int userid) {
		this.userid = userid;
	}
	public String getUsername() {
		return username;
	}
	public void setUsername(String username) {
		this.username = username;
	}
	public int getAccountid() {
		return accountid;
	}
	public void setAccountid(int accountid) {
		this.accountid = accountid;
	}
	@Override
	public String toString() {
		return "User [userid=" + userid + ", username=" + username
				+ ", accountid=" + accountid + "]";
	}
	
}
