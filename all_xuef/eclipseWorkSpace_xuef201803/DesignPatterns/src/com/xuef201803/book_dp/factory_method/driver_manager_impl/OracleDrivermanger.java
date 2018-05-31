package com.xuef201803.book_dp.factory_method.driver_manager_impl;

import com.xuef201803.book_dp.factory_method.DriveManager_;

public class OracleDrivermanger implements DriveManager_ {

	@Override
	public String getConnection(String url, String user, String passwd) {
		System.out.println("return oracle conn");
		return "oracle driver conn";
	}
}