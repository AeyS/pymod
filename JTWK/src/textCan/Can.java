package textCan;
import com.lowagie.text.Document;
import com.lowagie.text.DocumentException;
import com.lowagie.text.Paragraph;
import com.lowagie.text.pdf.PdfWriter;
import com.lowagie.text.html.HtmlWriter;

import java.io.FileNotFoundException;
import java.io.FileOutputStream;


public class Can {
	/**
	 * д��pdf�ļ�
	 * @param path �����ļ�·����
	 * @param content ����
	 */
	public void write(String path,String content)
	{
		Document document = new Document();
		try {
			PdfWriter.getInstance(document, new FileOutputStream(path));
			document.open();
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (DocumentException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		try {
			document.add(new Paragraph(content));
		} catch (DocumentException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		document.close();
	}

	/**
	 * ����html�ļ�
	 * @param path �����ļ�·����
	 * @param content ����
	 */
	public void htmlwrite(String path,String content)
	{
		Document document = new Document();
		try {
			HtmlWriter.getInstance(document, new FileOutputStream(path));
			document.open();
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		try {
			document.add(new Paragraph(content));
		} catch (DocumentException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		document.close();
	}
}
