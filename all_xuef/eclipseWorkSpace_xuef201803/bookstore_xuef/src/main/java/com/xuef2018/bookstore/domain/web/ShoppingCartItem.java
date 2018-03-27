package com.xuef2018.bookstore.domain.web;

import com.xuef2018.bookstore.domain.Book;

/**
 * 购物车中的单条记录
 * @author moveb
 *
 */
public class ShoppingCartItem {
	private Book book;
	private int bookNum; // 数量
	
	public ShoppingCartItem(Book book){
		this.book = book;
		bookNum = 1;
	}

	
	public Book getBook() {
		return book;
	}
	public void setBook(Book book) {
		this.book = book;
	}
	public int getBookNum() {
		return bookNum;
	}
	public void setBookNum(int bookNum) {
		this.bookNum = bookNum;
	}
	// 计算单条记录 的 钱数
	public float getItemMoney(){
		return book.getPrice() * bookNum;
	}
	public void increBookNum(){
		bookNum += 1;
	}
}
