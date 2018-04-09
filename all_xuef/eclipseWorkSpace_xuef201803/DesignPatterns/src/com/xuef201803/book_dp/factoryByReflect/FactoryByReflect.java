package com.xuef201803.book_dp.factoryByReflect;

import java.io.IOException;
import java.io.InputStream;
import java.util.Properties;

import com.xuef201803.book_dp.simpleFactory.Api;

/**
 * 反射 + 配置文件
 * 据说反射的性能比较低 
 * @author moveb
 */
public class FactoryByReflect {
	public static Api getInstance(){
		Properties properties = new Properties();
		InputStream in = null;
		try{
			// 加载配置文件
			/**
			 * classpath下的配置文件;
			 * 项目，右键properties，左边选择Java buildpath，右边source下可以看到
			 * source folder on build path
			 * 这里只有src在。所以配置文件必须放在src下。当然你也可以add folder
			 */
			in = FactoryByReflect.class.getClassLoader()
								  .getResourceAsStream("factory.properties");
			properties.load(in);
		} catch(IOException e){
			e.printStackTrace();
			System.out.println("装载配置文件出错...");
		} finally{
			try {
				in.close();
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
		Api api = null;
		// 获得类名
		String className = properties.getProperty("impleClass");
		try {
			// 利用反射生成类实例
			api = (Api) Class.forName(className).newInstance();
		} catch (Exception e) {
			e.printStackTrace();
		}
		return api;
	}
}
