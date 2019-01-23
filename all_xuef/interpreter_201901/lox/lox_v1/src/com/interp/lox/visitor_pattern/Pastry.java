package com.interp.lox.visitor_pattern;

public abstract class Pastry {
	abstract void accept(PastryVisitor visitor);
}

class Beignet extends Pastry {

	@Override
	void accept(PastryVisitor visitor) {
		visitor.visitBeignet(this); 
	}
}                             

class Cruller extends Pastry {

	@Override
	void accept(PastryVisitor visitor) {
		visitor.visitCruller(this);
	}
}
