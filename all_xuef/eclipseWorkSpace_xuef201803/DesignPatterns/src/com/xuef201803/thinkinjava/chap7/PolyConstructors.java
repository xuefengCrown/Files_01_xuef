package com.xuef201803.thinkinjava.chah7;
public class PolyConstructors {
	public static void main(String[] args) {
		/*
		 * ǰһ�ڽ����ĳ�ʼ��˳�򲢲�ʮ�������������ǽ������Ĺؼ����ڡ���ʼ����ʵ�ʹ����������ģ�
			(1) �ڲ�ȡ�����κβ���֮ǰ��Ϊ�������Ĵ洢�ռ��ʼ���ɶ������㡣
			(2) ����ǰ�����������������û����๹��������ʱ�������ǵ�draw()������õ����ã���ȷ����
			RoundGlyph����������֮ǰ������ʱ�ᷢ�� radius��ֵΪ 0���������ڲ���(1)��ɵġ�
			(3) ����ԭ��������˳����ó�Ա��ʼ�����롣
			(4) ���������๹���������塣
		 */
		new RoundGlyph(5);
	}
}
abstract class Glyph {
	abstract void draw();
	/**
	 * ��ˣ���ƹ�����ʱһ���ر���Ч�Ĺ����ǣ��þ����ܼ򵥵ķ���ʹ����������״̬��������ܣ������
		���κη������ڹ�������Ψһ�ܹ���ȫ���õ����ڻ������о���final ���Ե���Щ������Ҳ������private
		�����������Զ�����final ���ԣ�����Щ�������ܱ����ǣ����Բ����������Ǳ�ڵ����⡣
	 */
	Glyph() {
		System.out.println("Glyph() before draw()");
		draw();
		System.out.println("Glyph() after draw()");
	}
}
class RoundGlyph extends Glyph {
	int radius = 1;
	RoundGlyph(int r) {
		radius = r;
		System.out.println("RoundGlyph.RoundGlyph(), radius = " + radius);
	}
	void draw() {
		System.out.println("RoundGlyph.draw(), radius = " + radius);
	}
}