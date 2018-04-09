package multi_thread.thread.runnable.strategy;

public interface TaxCalcStrategy {
	// 可以使用泛型和Object... 来改进
	/**
	 * 根据工资和奖金 来计算个人所得税
	 * @param salary 工资
	 * @param bonus 奖金
	 * @return
	 */
	double calcTax(double salary, double bonus);
}
