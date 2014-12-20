package org.aeys.keyword.nearSort;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.serializer.SerializerFeature;
import org.aeys.tools.ArrayCan;


/**
 * Created by XIN on 2008/1/1.
 */
public class keylayer_test {
    public static void main(String[] argv){
        String arg = "as|er|sdf";
        String[] ar = arg.split("\\|");
        Entry et = new Entry();
        et.setId(0);
        et.setEntry(ar[0]);
        ArrayCan arc = new ArrayCan();
        et.setEntryArr(arc.trans_ListArr(ar));
        System.out.println(et.getEntry());
        System.out.println(et.getEntryArr());
        // 恢复class
        SerializerFeature[] features = {SerializerFeature.WriteClassName};
        String js = JSON.toJSONString(et, features);
        System.out.println(js);
        Entry obj =(Entry) JSON.parse(js);
        System.out.println(obj.getEntryArr()+"------------");

        // 索引id
        String[] string = {"我的名字是李", "我爱某某某哦"};
//        String str = keylayer.IKAsisToJson(string[0]);
        String[] strarr = keylayer.IKAsisArrayToJson(string);
    }
}
