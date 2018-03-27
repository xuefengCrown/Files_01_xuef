package com.xuef2018.bookstore.dao.daoImpl;

import java.util.Collection;

import org.hibernate.Session;
import org.hibernate.SessionFactory;

import com.xuef2018.bookstore.dao.TradeItemDao;
import com.xuef2018.bookstore.domain.TradeItem;

public class TradeItemDaoHibImpl implements TradeItemDao {
	private SessionFactory sessionFactory;
	public void setSessionFactory(SessionFactory sessionFactory) {
		this.sessionFactory = sessionFactory;
	}
	public Session getSession(){
		return sessionFactory.getCurrentSession();
	}
	
	@Override
	public void insertAny(Collection<TradeItem> items) {
		for(TradeItem ti:items){
			getSession().save(ti);
		}
	}

}
