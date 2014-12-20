package org.aeys.keyword.nearSort;

import org.aeys.tools.ArrayCan;
import org.aeys.tools.systool;

/**
 * 排序
 * Created by Aeys on 2014/11/18.
 */
public class AvgSort {
    public int widenum=3;//字符串最大组成员个数
    public int maxLenght=53;//字符串最大宽度

    /**
     * 宽度计算排序
     * @param strarr
     * @return
     */
    public String sortcolumn(String[] strarr){
        String[] arr;
        String lines,line,Successlist;
        ArrayCan arc = new ArrayCan();
        arr = arc.RandomSort(arc.trans_StrArr(arc.lsord(arc.trans_ListArr(strarr))));
        lines = line = Successlist = "";
        for (int i = 0; i < arr.length; i++) {
            lines = line;
            String[] valueStrings = {line,arr[i]}; 
            line = systool.getformat("%s%s ", valueStrings);
            if (line.length()>this.maxLenght){
                Successlist = Successlist + lines + "\r\n";
            }else if (line.trim().split(" ").length == this.widenum){//此处通过widenum的大小限制每行词数个数
                Successlist = Successlist + line+"\r\n";
                line = "";
            }
        }
        if (line.length()>1){Successlist = Successlist + line + "\r\n";}
        return Successlist;
    }
}
