package org.aeys.tools;

public class systool {
	
	/**
	 * ��ʽ�����ַ���
	 * @param content
	 * @param arg
	 * @return
	 */
	public static String getformat(String content,String arg) {
    	Object[] printObj = new Object[0];
    	printObj[0] = arg;
		return getformat(content, arg);	
	}

	/**
	 * ��ʽ�����ַ�������
	 * @param content
	 * @param argv
	 * @return
	 */
	public static String getformat(String content,String[] argv) {
		String result=null;
		Object[] printObj = new Object[argv.length];
    	for (int j = 0; j < printObj.length; j++) {
    		printObj[j] = argv[j];
		}
    	result = String.format(content, printObj);
		return result;
	}
}
