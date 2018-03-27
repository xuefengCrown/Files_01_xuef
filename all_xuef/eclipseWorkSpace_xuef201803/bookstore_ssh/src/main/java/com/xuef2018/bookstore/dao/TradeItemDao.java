package com.xuef2018.bookstore.dao;

import java.util.Collection;

import com.xuef2018.bookstore.domain.TradeItem;

public interface TradeItemDao {
	/**
	 * 插入n条记录
	 */
	public void insertAny(Collection<TradeItem> items);
}
