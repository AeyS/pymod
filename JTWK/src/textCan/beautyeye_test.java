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
	 * �������Ե�¼���ڵĴ���
	 */
	private static final long serialVersionUID = 1L;
	public beautyeye_test(){
		System.out.println("��ʼ����");
		JTextField  jTextField = new JTextField(12);//�����ı������
		JLabel jLabel1 = new JLabel("�û���");
		JLabel jLabel2 = new JLabel("  ���� ");
		JButton jb1 = new JButton("ȷ��");
		JButton jb2 = new JButton("ȡ��");
		JPasswordField jPasswordField = new JPasswordField(13);
		JPanel jp1 = new JPanel();
		JPanel jp2 = new JPanel();
		JPanel jp3 = new JPanel();
		
		setLayout(new GridLayout(3,1));
		
		 jp1.add(jLabel1);
		 jp1.add(jTextField);//��һ���������û������ı��� 
		 jp2.add(jLabel2);
		 jp2.add(jPasswordField);//�ڶ���������������ı��� 
		 jp3.add(jb1);
		 jp3.add(jb2);//������������ȷ��ȡ����ť
		 
		 this.add(jp1);
		 this.add(jp2);
		 this.add(jp3);
		 setSize(400,300);
//		 setResizable(false);
		 setVisible(true);
		 System.out.println("���ü���");
		 setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		 setTitle("��javaд�Ľ���");

	}
	public static void main(String[] args){
		//��װbeautyeyeƤ��
		try{
			org.jb2011.lnf.beautyeye.BeautyEyeLNFHelper.launchBeautyEyeLNF();
		}catch(Exception e){
			System.out.print(e);
		}
		new beautyeye_test();
	}
}
