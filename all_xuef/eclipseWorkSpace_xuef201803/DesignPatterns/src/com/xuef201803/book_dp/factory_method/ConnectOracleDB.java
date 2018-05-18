package com.xuef201803.book_dp.factory_method;

import com.xuef201803.book_dp.factory_method.driver_manager_impl.OracleDrivermanger;

public class ConnectOracleDB extends ConnectDatabase {

	@Override
	protected DriveManager_ factoryMathod() {
		return new OracleDrivermanger();
	}

}
