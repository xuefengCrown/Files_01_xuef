package algs.xuef201806.chap01.exercise;

import java.io.File;
import java.io.UnsupportedEncodingException;

import algs.base.StdOut;
import algs.xuef201806.chap01.Queue;

/**
 * 文件列表
 * @author moveb
 *
 */
public class Ex_1_3_43_list_files {
	public static void main(String[] args) {
		String folderPath = "C:\\code_dxf\\xuefgit\\Files_01_xuef\\all_xuef\\code\\design_of_computer_program";
		Queue<String> q = new Queue<String>();
		listFiles("  ", folderPath, q);
		for(String fname:q){
			System.out.println(fname);
		}
	}
	
	public static void listFiles(String tab, String folder, Queue q) {
		/**
		 * "file.encoding"影响的是文件内容的编码，而不是文件名的编码，影响文件名编码的是“sun.jnu.encoding”这个属性，
		 * 用getProperty("sun.jnu.encoding")可以获取文件名编码。而且这个"file.encoding"用的时候也容易出问题，因为
		 * 它是跟运行环境编码设置有关系。
		 */
		//String fileCode=(String)System.getProperties().get("sun.jnu.encoding");
		//fileCode = "utf-8";
		tab = tab + "  ";
		File file = new File(folder);
		File[] files = file.listFiles();
		for (File f:files){
			//String fname = new String(f.getName().getBytes(), fileCode);
			//System.out.println(f.getName());
			if(f.isFile()){
				q.enqueue(tab + f.getName());
			}else if(f.isDirectory()){
				q.enqueue(tab + f.getName());
				listFiles(tab, f.getAbsolutePath(), q);
			}
		}
	}
}
