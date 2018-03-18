package com.xuef2018.bookstore.dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.SQLException;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.apache.commons.dbutils.QueryRunner;
import org.apache.commons.dbutils.handlers.BeanHandler;
import org.apache.commons.dbutils.handlers.BeanListHandler;
import org.apache.commons.dbutils.handlers.ScalarHandler;

import com.mysql.jdbc.Statement;
import com.xuef2018.bookstore.db.JDBCUtils;
import com.xuef2018.bookstore.utils.ReflectionUtils;

public class BaseDao<T> implements Dao<T> {
	private QueryRunner queryRunner = new QueryRunner();
	private Class<T> clazz;
	public BaseDao(){
		clazz = ReflectionUtils.getSuperGenericType(getClass());
	}
	/**
	 * 插入对象，并返回主键; 可以改用queryRunner实现
	 */
	@Override
	public long insert(String sql, Object... args) {
		long id = -1;
		Connection conn = null;
		PreparedStatement preparedStatement = null;
		ResultSet rs = null;
		
		try {
			conn = JDBCUtils.getConnection();
			// 设定 返回主键
			preparedStatement = conn.prepareStatement(sql, Statement.RETURN_GENERATED_KEYS);
			
			if(args != null){
				for(int i=0; i<args.length; i++){
					preparedStatement.setObject(i+1, args[i]);
				}
			}
			preparedStatement.executeUpdate();
			
			// 获取生成的主键
			rs = preparedStatement.getGeneratedKeys();
			if(rs.next()){
				id = rs.getLong(1);
			}
		} catch (SQLException e) {
			e.printStackTrace();
		} finally{
			// 由内向外关闭
			JDBCUtils.release(rs, preparedStatement);
			JDBCUtils.release(conn);
		}
		return 0;
	}

	@Override
	public void update(String sql, Object... args) {
		Connection conn = JDBCUtils.getConnection();
		try {
			queryRunner.update(conn, sql, args);
		} catch (SQLException e) {
			e.printStackTrace();
		} finally{
			JDBCUtils.release(conn);
		}
	}

	@Override
	public T query(String sql, Object... args) {
		Connection connection = null;
		
		try {
			connection = JDBCUtils.getConnection();
			return queryRunner.query(connection, sql, new BeanHandler<>(clazz), args);
		} catch (Exception e) {
			e.printStackTrace();
		} finally{
			JDBCUtils.release(connection);
		}
		return null;
	}

	@Override
	public List<T> queryForList(String sql, Object... args) {
		Connection connection = null;
		try {
			connection = JDBCUtils.getConnection();
			return queryRunner.query(connection, sql, new BeanListHandler<>(clazz), args);
		} catch (Exception e) {
			e.printStackTrace();
		} finally{
			JDBCUtils.release(connection);
		} 
		return null;
	}

	@Override
	public <V> V getSingleVal(String sql, Object... args) {
		Connection connection = null;
		
		try {
			connection = JDBCUtils.getConnection();
			Object query = queryRunner.query(connection, sql, new ScalarHandler(), args);
			return (V)query;
		} catch (Exception e) {
			e.printStackTrace();
		} finally{
			JDBCUtils.release(connection);
		}
		return null;
	}

	@Override
	public void batch(String sql, Object[]... params) {
		Connection connection = null;
		
		try {
			connection = JDBCUtils.getConnection();
			queryRunner.batch(connection, sql, params);
		} catch (Exception e) {
			e.printStackTrace();
		} finally{
			JDBCUtils.release(connection);
		}
	}
}
