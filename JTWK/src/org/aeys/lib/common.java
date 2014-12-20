package org.aeys.lib;

import java.io.IOException;

/**
 * 这个类负责将数组内容转换成字符串
 */
public class common {

	public static void main(String[] args) {
		String[] res = {"1","2"};
		System.out.print(sa2s(res));
	}


    /**
     * 将数组字符串转换为纯字符串
     * @param args
     * @return
     */
	public static String sa2s(String[] args){
		String result = "";
		for (int i=0; i<args.length; i++){
			result += args[i];
		}
		return result;
	}
	/**
	 * 调用命令行执行｛代码不可用｝
	 * @param args
	 */
	public static void cmd(String args){
		Runtime rt = Runtime.getRuntime();
		 try {
			Process p = rt.exec(args);
			if(p != null){
				p.destroy();
				p = null;
			}
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

}
