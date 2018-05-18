package com.xuef201803.book_dp.factoryMethod;

public class ExportTxtFileOperate extends ExportOperate {

	@Override
	protected ExportFileApi factoryMethod() {
		return new ExportTxtFile();
	}

}
