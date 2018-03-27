package com.xuef2018.bookstore.dao.daoImpl;

import org.hibernate.Query;
import org.hibernate.Session;
import org.hibernate.SessionFactory;

import com.xuef2018.bookstore.dao.BaseDao;
import com.xuef2018.bookstore.dao.UserDao;
import com.xuef2018.bookstore.domain.User;

public class UserDaoHibImpl extends BaseDao<User> implements UserDao {
	private SessionFactory sessionFactory;
	public void setSessionFactory(SessionFactory sessionFactory) {
		this.sessionFactory = sessionFactory;
	}
	public Session getSession(){
		return sessionFactory.getCurrentSession();
	}
	
	@Override
	public User getUser(String username) {
		String hql = "FROM User where username = ?";
		Query query = getSession().createQuery(hql).setString(0, username);
		User result = (User)query.uniqueResult();
		return result;
	}
}
