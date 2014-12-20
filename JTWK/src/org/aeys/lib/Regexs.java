package org.aeys.lib;
import java.util.regex.*;

public class Regexs {
	public static void main(String[] args){
		reset();
	}
	
	public static void reset(){
		System.out.println("this is Regex class");
	}
	/**
	 * 正则字符串
	 * @param patt 表达式
	 * @param strs 字符串
	 * @return
	 */
	public static String[] Regs(String patt,String strs)
    {
        Pattern pattern = Pattern.compile(patt); /* 编译 */
        Matcher matcher = pattern.matcher(strs); /* 匹配 */
        boolean found = false;
        String res = "";
        while (matcher.find()) {
            //输出匹配位置
            //System.out.println(String.format("satrt:%d,end:%d",matcher.start(),matcher.end()));
            /* 匹配截取字符串 */
            String result = strs.substring(matcher.start(),matcher.end());
            res += result+"|";
        }
        if (!found){
        	res = "No match found.\n";
        }
        /* 将结果分割成数组，由于split接受正则表达式，因此在使用|之前先将其转义 */
        String[] arar = res.split("\\|");
        for (int i=0;i<arar.length;i++){
            System.out.println(arar[i]);
        }
        return arar;
    }

}
