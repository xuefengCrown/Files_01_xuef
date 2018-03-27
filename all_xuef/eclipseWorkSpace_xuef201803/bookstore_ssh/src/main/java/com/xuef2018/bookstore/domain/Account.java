package com.xuef2018.bookstore.domain;

public class Account {
	private int accountid;
	private float balance;
	public int getAccountid() {
		return accountid;
	}
	public void setAccountid(int accountid) {
		this.accountid = accountid;
	}
	public float getBalance() {
		return balance;
	}
	public void setBalance(float balance) {
		this.balance = balance;
	}
	@Override
	public String toString() {
		return "Account [accountid=" + accountid + ", balance=" + balance + "]";
	}
	
}
