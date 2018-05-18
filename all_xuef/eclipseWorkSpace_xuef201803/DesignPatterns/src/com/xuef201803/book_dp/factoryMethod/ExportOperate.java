package com.xuef201803.book_dp.factoryMethod;
/**
 * 实现导出数据的业务功能对象
 * @author moveb
 *
 */
public abstract class ExportOperate {
	/**
	 * 使用产品对象来实现导出功能
	 * @param data
	 * @return
	 */
	public boolean export(String data){
		// api 由具体的子类来提供(通过工厂方法)
		ExportFileApi api = factoryMethod();
		
		return api.export(data);
	}

	/**
	 * 工厂方法为子类提供了挂钩
	 * 和子类的约定；类似于一个注入对象的途径
	 * @return
	 */
	protected abstract ExportFileApi factoryMethod();
}
