package com.xuef.string;
/**
 * 字符串类维护了一个字符串常量池
 * 
 * 
 * 
 * 
 * @author moveb
 *
 */
public class StringTest {

	public static void main(String[] args) {
		// s1拿到的直接是字面量地址 new String("hello").intern()
		String s1 = "hello";
		String s2 = "hello";
		System.out.println(s1 == s2); // true
		// 运行期会在堆中创建一个字符串对象，而字符串字面量存在字符串常量池中；
		// s3存在栈中，其值是堆中字符串对象的引用，== 比较的是堆中的地址，equals比较的是字面量
		String s3 = new String("world");
		String s4 = new String("world");
		System.out.println(s3 == s4); // 比较堆中的引用 
		System.out.println(s3.equals(s4)); // 比较字面量
	}
}
