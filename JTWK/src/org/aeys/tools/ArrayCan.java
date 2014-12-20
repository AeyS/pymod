package org.aeys.tools;

import java.util.*;


/**
 * Created by Aeys on 2014/11/14.
 * 鏁扮粍鍒楄〃鎿嶄綔鏂规硶搴�
 * @author Aey
 *
 */
public class ArrayCan{
    /**
     * 杩囨护鏁扮粍鍏冪礌
     * @param ls 鏁扮粍
     * @param key 杩囨护鍏抽敭璇�
     * @return
     */
    public String[] FilterKeyWord(String[] ls,String key){
        List result = new ArrayList();
        for (int i = 0; i < ls.length; i++) {
            if (ls[i].contains(key))
                result.add(ls[i]);
        }
        return trans_StrArr(result);
    }

    /**
     * 鏁扮粍闅忔満鎺掑簭
     * @param ls 鏁扮粍
     * @return ls
     */
    public String[] RandomSort(String[] ls){
        Random rd = new Random();
        int r = ls.length;
        int ort;
        String nowstr;
        for (int i = 0; i < r; i++) {
            ort = rd.nextInt(r);// 鍙栭殢鏈哄�煎湪0鍒皉涔嬮棿
            nowstr = ls[i];
            ls[i] = ls[ort];
            ls[ort] = nowstr;
        }
        return ls;
    }

    /**
     * 鍒楄〃鍘婚噸,骞跺幓闄ょ┖鐧借
     * @param ls 鏁扮粍
     * @return newList
     */
    public List lsord(List ls){
        Set set = new HashSet();
        List newList = new ArrayList();
        for (Iterator iter = ls.iterator(); iter.hasNext();) {
            Object element = iter.next();
            if (set.add(element))
                if (!element.toString().isEmpty()) newList.add(element);
        }
        return newList;
    }

    /**
     * 灏嗗瓧绗︿覆鏁扮粍杞崲鎴愬垪琛�
     * @param StrArr 瀛楃涓叉暟缁�
     */
    public List trans_ListArr(String[] StrArr){
        return Arrays.asList(StrArr);
    }

    /**
     * 灏嗗垪琛ㄨ浆鎹㈡垚瀛楃涓叉暟缁�
     * @param list 鍒楄〃
     * @return StrArr
     */
    public String[] trans_StrArr(List list) {
        String[] StrArr = new String[list.size()];
        list.toArray(StrArr);
        return StrArr;
    }

    /**
     * 鎵撳嵃瀛楃涓叉暟缁�
     * @param ls 鏁扮粍
     */
    public void prls(String[] ls){
        for (int i = 0; i < ls.length; i++) {
            System.out.println(ls[i]);
        }
    }

    /**
     * 鍒ゆ柇鍒楄〃鏄惁瀛樺湪xx鍏冪礌
     * @param arr
     * @param a
     * @return boolean
     */
    public boolean existIn(String[] arr,String a){
        return Arrays.asList(arr).contains(a);
    }

    /**
     * 鍒犻櫎绱㈠紩椤�
     * @param index
     * @param Arraysite
     * @return
     */
    public List removeIndex(int index,String[] Arraysite){
        List result = new ArrayList();
        for (int i = 0; i < Arraysite.length; i++) {
            if (i==index) continue;
            result.add(Arraysite[i]);
        }
        return result;
    }

    /**
     * 绱㈠紩闃熷垪鎸囧畾鍏冪礌浣嶇疆
     * @param arr
     * @param str
     * @return
     */
    public int indexOf(String[] arr,String str){
        return trans_ListArr(arr).indexOf(str);
    }

    /**
     * 绫讳技python鍜宩s鐨勫瓧绗︿覆join鍑芥暟
     * @param arr
     * @param str
     * @return
     */
    public String join(String[] arr,String str){
        String result="";
        for (int i = 0; i < arr.length; i++) {
            System.out.println(arr[i]);
            result = result + arr[i] + str;
        }
        return result;
    }

}

