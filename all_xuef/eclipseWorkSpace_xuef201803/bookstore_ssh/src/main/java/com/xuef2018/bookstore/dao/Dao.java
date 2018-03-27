package com.xuef2018.bookstore.dao;

import java.util.List;

/**
 * ���� Dao ͨ�ò���, BaseDao �ṩʵ��
 * @author moveb
 *
 * @param <T>
 */
public interface Dao<T> {
	/**
	 * @param sql: ��ִ�е� SQL
	 * @param args: ���ռλ���Ŀɱ����
	 * @return: ������¼�¼�� id
	 */
	public long insert(String sql, Object ... args);
	
	/**
	 * ִ�� UPDATE ����, ���� INSERT(��û�з���ֵ), UPDATE, DELETE
	 * @param sql: ��ִ�е� SQL
	 * @param args: ���ռλ���Ŀɱ����
	 */
	void update(String sql, Object ... args);
	
	/**
	 * ��ѯ������¼, �������¼��Ӧ�����һ������
	 * @param sql: ��ִ�е� SQL
	 * @param args: ���ռλ���Ŀɱ����
	 * @return: ���¼��Ӧ�����һ������
	 */
	T query(String sql, Object ... args);
	
	/**
	 * ��ѯ������¼, ����һ������� List
	 * @param sql: ��ִ�е� SQL
	 * @param args: ���ռλ���Ŀɱ����
	 * @return: ������������һ�� List
	 */
	List<T> queryForList(String sql, Object ... args);
	
	/**
	 * ִ��һ�����Ի�ֵ�Ĳ�ѯ����, �����ѯĳһ����¼��һ���ֶ�, ���ѯĳ��ͳ����Ϣ, ����Ҫ��ѯ��ֵ
	 * @param sql: ��ִ�е� SQL
	 * @param args: ���ռλ���Ŀɱ����
	 * @return: ִ��һ�����Ի�ֵ�Ĳ�ѯ����, �����ѯĳһ����¼��һ���ֶ�, ���ѯĳ��ͳ����Ϣ, ����Ҫ��ѯ��ֵ
	 */
	<V> V getSingleVal(String sql, Object ... args);
	
	/**
	 * ִ���������²���
	 * @param sql: ��ִ�е� SQL
	 * @param args: ���ռλ���Ŀɱ����
	 */
	void batch(String sql, Object[]... params);
}