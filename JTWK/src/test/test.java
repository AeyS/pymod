package test;
import textCan.Can;
public class test {
	public static void main(String[] args){
		Can pdf = new Can();
		pdf.htmlwrite("D:/Helloworld.html", "Hello World");
		pdf.write("D:/Helloworld.pdf","Hello World");
	}
}