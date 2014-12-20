package textCan;

import com.alibaba.fastjson.JSON;
import org.aeys.keyword.nearSort.Entry;
import org.aeys.tools.ArrayCan;

public class fastjson_test {
	public static void main(String[] args){
		
		Group group = new Group();
		group.setId(0L);
		group.setName("admin");

		User guestUser = new User();
		guestUser.setId(2L);
		guestUser.setName("guest");


		Entry et = new Entry();
		et.setId(3L);
		et.setEntry("head");
        String[] str = {"body","asdg"};
        ArrayCan arc = new ArrayCan();
		et.setEntryArr(arc.trans_ListArr(str));
//		User rootUser = new User();
//		rootUser.setId(3L);
//		rootUser.setName("root");

		group.getUsers().add(guestUser);
//		group.getUsers().add(rootUser);

		String jsonString = JSON.toJSONString(et);

		System.out.println(jsonString);
		
	}
}
