package com.xuef201803.book_dp.factoryMethod;

public class ExportDBOperate extends ExportOperate {

	@Override
	protected ExportFileApi factoryMethod() {
		return new ExportDB();
	}

}
