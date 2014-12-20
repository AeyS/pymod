package textCan;

import java.io.File;
import java.io.IOException;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

public class Go_jsoup {
	public static void main(String[] args){
		String myj = myjsoup("asdg");
		System.out.println("输出结果:"+myj);
	}
	/**
	 * 处理html文档，返回所要信息
	 * @param html
	 * @return
	 */
	public static String myjsoup(String html){
		File input = new File("D:/input.html");
		
		String result=null;
		if(html == null) return result;
		Document doc = null;
		try {
			doc = Jsoup.parse(input, "utf-8", "http://www.baidu.com/");
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		Element content = doc.getElementById("head");
		Elements links = content.getElementsByTag("a");
		for (Element link : links){
			String linkHref = link.attr("href");
			System.out.println(linkHref);
			String linkText = link.text();
			System.out.println(linkText);
		}
		return result;
	}
}
