package org.smart4j.framework.utils;

import java.net.URLDecoder;
import java.net.URLEncoder;
/**
 * 编码与解码操作工具类
 * @author moveb
 *
 */
public class CodecUtil {
	/**
	 * 将 URL 编码
	 */
	public static String encodeURL(String source){
		String target = "";
		try{
			target = URLEncoder.encode(source, "UTF-8");
		} catch(Exception e){
			e.printStackTrace();
		}
		return target;
	}
	/**
	 * 将 URL 解码
	 */
	public static String decodeURL(String source){
		String target = "";
		try{
			target = URLDecoder.decode(source, "UTF-8");
		} catch(Exception e){
			e.printStackTrace();
		}
		return target;
	}
}
