package multi_thread.thread.runnable.strategy;
/**
 * �ø�������˰�������������˵��Runnable�ӿڵ����
 * Target: ��˰�� 
 * @author moveb
 */
public class Target {
	private double salary;
	private double bonus;
	
	// ��������˰�Ĳ��� ��Ҫ��Ƴɾ�̬��������???
	private TaxCalcStrategy taxCalcStrategy;
	public Target(double salary, double bonus) {
		this.salary = salary;
		this.bonus = bonus;
	}
	// ע�����ļ������
	public void setTaxCalcStrategy(TaxCalcStrategy taxCalcStrategy) {
		this.taxCalcStrategy = taxCalcStrategy;
	}
	/**
	 * ��������񽻸�������ʵ��
	 * ����ͬ���߳��߼�ͨ����дrun()��������д
	 * @return
	 */
	public double calcTax(){
		return this.taxCalcStrategy.calcTax(salary, bonus);
	}
}