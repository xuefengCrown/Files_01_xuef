package com.xuef2018.bookstore.dao.daoImpl;

import org.hibernate.Query;
import org.hibernate.Session;
import org.hibernate.SessionFactory;

import com.xuef2018.bookstore.dao.AccountDao;

public class AccounDaoHibImpl implements AccountDao{
	private SessionFactory sessionFactory;
	public void setSessionFactory(SessionFactory sessionFactory) {
		this.sessionFactory = sessionFactory;
	}
	public Session getSession(){
		return sessionFactory.getCurrentSession();
	}
	@Override
	public void updateBalance(int accountid, float amount) {
		String hql = "update Account set balance = balance - ?"
				+ " where accountid = ?";
		Query query = getSession().createQuery(hql).setFloat(0, amount)
									 .setInteger(1, accountid);
		query.executeUpdate();
	}

}
