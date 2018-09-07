package algs.implebyme.exercise1;

import algs.base.Transaction;

public class Ex1_2_13_transaction implements Comparable<Ex1_2_13_transaction>{
	private String who;
	private Date when;
	private double amount;
	private String desc;
	public Ex1_2_13_transaction(String who, Date when, double amount) {
		if (Double.isNaN(amount) || Double.isInfinite(amount))
            throw new IllegalArgumentException("Amount cannot be NaN or infinite");
		this.who = who;
		this.when = when;
		this.amount = amount;
	}
	
	public String getWho() {
		return who;
	}

	public void setWho(String who) {
		this.who = who;
	}

	public Date getWhen() {
		return when;
	}

	public void setWhen(Date when) {
		this.when = when;
	}

	public double getAmount() {
		return amount;
	}

	public void setAmount(double amount) {
		this.amount = amount;
	}

	public String getDesc() {
		return desc;
	}

	public void setDesc(String desc) {
		this.desc = desc;
	}

	@Override
	public String toString() {
		return "Ex1_2_13_transaction [who=" + who + ", when=" + when
				+ ", amount=" + amount + ", desc=" + desc + "]";
	}
	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		long temp;
		temp = Double.doubleToLongBits(amount);
		result = prime * result + (int) (temp ^ (temp >>> 32));
		result = prime * result + ((when == null) ? 0 : when.hashCode());
		result = prime * result + ((who == null) ? 0 : who.hashCode());
		return result;
	}
	@Override
	public boolean equals(Object other) {
        if (other == this) return true;
        if (other == null) return false;
        if (other.getClass() != this.getClass()) return false;
        Ex1_2_13_transaction that = (Ex1_2_13_transaction) other;
        return (this.amount == that.getAmount()) && (this.who.equals(that.getWho()))
                                            && (this.when.equals(that.getWhen()));
    }

	@Override
	public int compareTo(Ex1_2_13_transaction o) {
		// TODO Auto-generated method stub
		return Double.compare(this.amount, o.amount);
	}
	
}
class Date
{
	private final int month;
	private final int day;
	private final int year;
	public Date(int m, int d, int y)
	{ month = m; day = d; year = y; }
	public int month()
	{ return month; }
	public int day()
	{ return day; }
	public int year()
	{ return day; }
	public String toString()
	{ return month() + "/" + day()
	+ "/" + year(); }
	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = prime * result + day;
		result = prime * result + month;
		result = prime * result + year;
		return result;
	}
	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Date other = (Date) obj;
		if (day != other.day)
			return false;
		if (month != other.month)
			return false;
		if (year != other.year)
			return false;
		return true;
	}
	
}