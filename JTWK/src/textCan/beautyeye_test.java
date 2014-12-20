package textCan;
import java.awt.*;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JPasswordField;
import javax.swing.JTextField;
public class beautyeye_test extends JFrame{
	/**
	 * 这份是针对登录窗口的创建
	 */
	private static final long serialVersionUID = 1L;
	public beautyeye_test(){
		System.out.println("开始运行");
		JTextField  jTextField = new JTextField(12);//定义文本框组件
		JLabel jLabel1 = new JLabel("用户名");
		JLabel jLabel2 = new JLabel("  密码 ");
		JButton jb1 = new JButton("确认");
		JButton jb2 = new JButton("取消");
		JPasswordField jPasswordField = new JPasswordField(13);
		JPanel jp1 = new JPanel();
		JPanel jp2 = new JPanel();
		JPanel jp3 = new JPanel();
		
		setLayout(new GridLayout(3,1));
		
		 jp1.add(jLabel1);
		 jp1.add(jTextField);//第一块面板添加用户名和文本框 
		 jp2.add(jLabel2);
		 jp2.add(jPasswordField);//第二块面板添加密码和文本框 
		 jp3.add(jb1);
		 jp3.add(jb2);//第三块面板添加确认取消按钮
		 
		 this.add(jp1);
		 this.add(jp2);
		 this.add(jp3);
		 setSize(400,300);
//		 setResizable(false);
		 setVisible(true);
		 System.out.println("设置监听");
		 setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		 setTitle("用java写的界面");

	}
	public static void main(String[] args){
		//安装beautyeye皮肤
		try{
			org.jb2011.lnf.beautyeye.BeautyEyeLNFHelper.launchBeautyEyeLNF();
		}catch(Exception e){
			System.out.print(e);
		}
		new beautyeye_test();
	}
}
