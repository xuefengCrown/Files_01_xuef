package multi_thread.thread.runnable.strategy;
// ����
public class Calculator {
	public static void main(String[] args) {
		// ����������
		TaxCalcStrategy taxCalcS = new SimpleTaxCalcStrategy();
		// ������˰��
		Target t = new Target(10000d, 4000d);

		// ע��������
		t.setTaxCalcStrategy(taxCalcS);
		
		System.out.println(t.calcTax());
	}
}